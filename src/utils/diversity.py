import ast


def analyze_test_diversity(test_code: str) -> dict:
    try:
        tree = ast.parse(test_code)
    except SyntaxError:
        return {
            "unique_inputs_count": 0,
            "edge_case_count": 0,
            "test_type_count": 0,
            "duplication_ratio": 1.0,
            "diversity_score": 0.0,
        }

    test_functions = [
        node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test")
    ]

    unique_inputs: set[str] = set()
    edge_cases: set[str] = set()
    test_types: set[str] = set()
    normalized_tests: list[str] = []

    for func in test_functions:
        normalized_tests.append(_normalize_test_body(func))
        _collect_test_types(func, test_types)

        for node in ast.walk(func):
            if isinstance(node, ast.Call):
                for arg in list(node.args) + [kw.value for kw in node.keywords]:
                    literal = _literal_key(arg)
                    if literal is not None:
                        unique_inputs.add(literal)
                    edge_cases.update(_classify_edge_cases(arg))
            elif isinstance(node, ast.Assert):
                test_types.add("assertion")
            elif isinstance(node, ast.Compare):
                test_types.add("comparison")

    duplicate_tests = len(normalized_tests) - len(set(normalized_tests)) if normalized_tests else 0
    duplication_ratio = round(duplicate_tests / len(normalized_tests), 3) if normalized_tests else 1.0

    unique_inputs_count = len(unique_inputs)
    edge_case_count = len(edge_cases)
    test_type_count = len(test_types)
    diversity_score = round(
        min(
            1.0,
            (
                min(unique_inputs_count / 10, 1.0)
                + min(edge_case_count / 6, 1.0)
                + min(test_type_count / 5, 1.0)
                + (1.0 - duplication_ratio)
            ) / 4,
        ),
        3,
    )

    return {
        "unique_inputs_count": unique_inputs_count,
        "edge_case_count": edge_case_count,
        "test_type_count": test_type_count,
        "duplication_ratio": duplication_ratio,
        "diversity_score": diversity_score,
    }


def _collect_test_types(func: ast.AST, test_types: set[str]) -> None:
    decorator_names = [_expr_name(dec) for dec in getattr(func, "decorator_list", [])]
    if any("parametrize" in name for name in decorator_names):
        test_types.add("parameterized")

    for node in ast.walk(func):
        if isinstance(node, ast.With):
            context_names = [_expr_name(item.context_expr) for item in node.items]
            if any("raises" in name for name in context_names):
                test_types.add("exception")
        elif isinstance(node, ast.Call):
            call_name = _expr_name(node.func)
            if "raises" in call_name:
                test_types.add("exception")
            elif "approx" in call_name:
                test_types.add("approximate")
            elif call_name.endswith(".mark.parametrize"):
                test_types.add("parameterized")
        elif isinstance(node, ast.Assert):
            if isinstance(node.test, ast.Compare):
                test_types.add("equality")
            elif isinstance(node.test, (ast.BoolOp, ast.UnaryOp)):
                test_types.add("boolean")


def _classify_edge_cases(node: ast.AST) -> set[str]:
    categories: set[str] = set()

    if isinstance(node, ast.Constant):
        value = node.value
        if value is None:
            categories.add("none")
        elif value == "":
            categories.add("empty_string")
        elif value == 0:
            categories.add("zero")
        elif value is False:
            categories.add("false")
        elif value is True:
            categories.add("true")
        elif isinstance(value, (int, float)) and value < 0:
            categories.add("negative")
    elif isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        if len(node.elts) == 0:
            categories.add("empty_collection")
        if _contains_duplicate_literals(node.elts):
            categories.add("duplicates")
    elif isinstance(node, ast.Dict):
        if len(node.keys) == 0:
            categories.add("empty_collection")

    return categories


def _contains_duplicate_literals(nodes: list[ast.AST]) -> bool:
    seen: set[str] = set()
    for node in nodes:
        key = _literal_key(node)
        if key is None:
            continue
        if key in seen:
            return True
        seen.add(key)
    return False


def _literal_key(node: ast.AST) -> str | None:
    try:
        value = ast.literal_eval(node)
    except Exception:
        return None
    return repr(value)


def _normalize_test_body(func: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    body = [ast.dump(stmt, include_attributes=False) for stmt in func.body]
    return "|".join(body)


def _expr_name(node: ast.AST) -> str:
    if isinstance(node, ast.Attribute):
        return f"{_expr_name(node.value)}.{node.attr}"
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Call):
        return _expr_name(node.func)
    return ""
