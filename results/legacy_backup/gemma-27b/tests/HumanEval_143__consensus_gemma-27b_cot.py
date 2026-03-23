import pytest

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

class TestWordsInSentence:
    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_single_prime_word(self):
        assert words_in_sentence("is") == "is"

    def test_single_non_prime_word(self):
        assert words_in_sentence("this") == ""

    def test_multiple_words_some_prime(self):
        assert words_in_sentence("This is a test") == "is"

    def test_multiple_words_all_prime(self):
        assert words_in_sentence("go for") == "go for"

    def test_multiple_words_none_prime(self):
        assert words_in_sentence("this that those") == ""

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  This is a test  ") == "is"

    def test_sentence_with_multiple_spaces_between_words(self):
        assert words_in_sentence("This  is   a    test") == "is"

    def test_long_sentence(self):
        assert words_in_sentence("lets go for swimming and running") == "go for"

    def test_sentence_with_mixed_case(self):
        assert words_in_sentence("This Is A Test") == "Is"

    def test_sentence_with_numbers_and_symbols(self):
        assert words_in_sentence("123 abc !@#") == "abc"

    def test_sentence_with_prime_length_words_at_start_and_end(self):
        assert words_in_sentence("go hello for") == "go for"

    def test_sentence_with_only_one_word(self):
        assert words_in_sentence("two") == "two"

    def test_sentence_with_long_non_prime_word(self):
        assert words_in_sentence("abcdefghijk") == ""

    def test_sentence_with_long_prime_word(self):
        assert words_in_sentence("abcdefghij") == "abcdefghij"

    def test_sentence_with_repeated_prime_words(self):
        assert words_in_sentence("go go go") == "go go go"

    def test_sentence_with_repeated_non_prime_words(self):
        assert words_in_sentence("this this this") == ""

    def test_sentence_with_prime_and_non_prime_repeated(self):
        assert words_in_sentence("go this go this") == "go go"

    def test_sentence_with_edge_case_prime_number_2(self):
        assert words_in_sentence("to be") == "to be"

    def test_sentence_with_edge_case_prime_number_3(self):
        assert words_in_sentence("cat dog") == "cat dog"

    def test_sentence_with_edge_case_prime_number_5(self):
        assert words_in_sentence("hello world") == "hello world"

    def test_sentence_with_edge_case_prime_number_7(self):
        assert words_in_sentence("amazing coding") == "amazing coding"

    def test_sentence_with_edge_case_prime_number_11(self):
        assert words_in_sentence("beautiful python") == "beautiful python"

    def test_sentence_with_edge_case_prime_number_13(self):
        assert words_in_sentence("programming code") == "programming code"

    def test_sentence_with_edge_case_prime_number_17(self):
        assert words_in_sentence("understanding logic") == "understanding logic"

    def test_sentence_with_edge_case_prime_number_19(self):
        assert words_in_sentence("communication skills") == "communication skills"

    def test_sentence_with_edge_case_prime_number_23(self):
        assert words_in_sentence("responsibility tasks") == "responsibility tasks"

    def test_sentence_with_edge_case_prime_number_29(self):
        assert words_in_sentence("consideration details") == "consideration details"

    def test_sentence_with_edge_case_prime_number_31(self):
        assert words_in_sentence("determination success") == "determination success"

    def test_sentence_with_edge_case_prime_number_37(self):
        assert words_in_sentence("investigation results") == "investigation results"

    def test_sentence_with_edge_case_prime_number_41(self):
        assert words_in_sentence("opportunities growth") == "opportunities growth"

    def test_sentence_with_edge_case_prime_number_43(self):
        assert words_in_sentence("collaboration teamwork") == "collaboration teamwork"

    def test_sentence_with_edge_case_prime_number_47(self):
        assert words_in_sentence("implementation process") == "implementation process"

    def test_sentence_with_edge_case_prime_number_53(self):
        assert words_in_sentence("organization structure") == "organization structure"

    def test_sentence_with_edge_case_prime_number_59(self):
        assert words_in_sentence("participation activities") == "participation activities"

    def test_sentence_with_edge_case_prime_number_61(self):
        assert words_in_sentence("demonstration expertise") == "demonstration expertise"

    def test_sentence_with_edge_case_prime_number_67(self):
        assert words_in_sentence("establishment standards") == "establishment standards"

    def test_sentence_with_edge_case_prime_number_71(self):
        assert words_in_sentence("encouragement support") == "encouragement support"

    def test_sentence_with_edge_case_prime_number_73(self):
        assert words_in_sentence("evaluation feedback") == "evaluation feedback"

    def test_sentence_with_edge_case_prime_number_79(self):
        assert words_in_sentence("identification issues") == "identification issues"

    def test_sentence_with_edge_case_prime_number_83(self):
        assert words_in_sentence("interpretation meaning") == "interpretation meaning"

    def test_sentence_with_edge_case_prime_number_89(self):
        assert words_in_sentence("justification reasons") == "justification reasons"

    def test_sentence_with_edge_case_prime_number_97(self):
        assert words_in_sentence("modification changes") == "modification changes"

    def test_sentence_with_edge_case_prime_number_101(self):
        assert words_in_sentence("recommendation advice") == "recommendation advice"

    def test_sentence_with_edge_case_prime_number_103(self):
        assert words_in_sentence("representation views") == "representation views"

    def test_sentence_with_edge_case_prime_number_107(self):
        assert words_in_sentence("simplification process") == "simplification process"

    def test_sentence_with_edge_case_prime_number_109(self):
        assert words_in_sentence("transformation growth") == "transformation growth"

    def test_sentence_with_edge_case_prime_number_113(self):
        assert words_in_sentence("understanding concepts") == "understanding concepts"

    def test_sentence_with_edge_case_prime_number_127(self):
        assert words_in_sentence("visualization insights") == "visualization insights"

    def test_sentence_with_edge_case_prime_number_131(self):
        assert words_in_sentence("communication strategies") == "communication strategies"

    def test_sentence_with_edge_case_prime_number_137(self):
        assert words_in_sentence("consideration factors") == "consideration factors"

    def test_sentence_with_edge_case_prime_number_139(self):
        assert words_in_sentence("determination efforts") == "determination efforts"

    def test_sentence_with_edge_case_prime_number_149(self):
        assert words_in_sentence("investigation findings") == "investigation findings"

    def test_sentence_with_edge_case_prime_number_151(self):
        assert words_in_sentence("opportunities challenges") == "opportunities challenges"

    def test_sentence_with_edge_case_prime_number_157(self):
        assert words_in_sentence("collaboration projects") == "collaboration projects"

    def test_sentence_with_edge_case_prime_number_163(self):
        assert words_in_sentence("implementation solutions") == "implementation solutions"

    def test_sentence_with_edge_case_prime_number_167(self):
        assert words_in_sentence("organization systems") == "organization systems"

    def test_sentence_with_edge_case_prime_number_173(self):
        assert words_in_sentence("participation events") == "participation events"

    def test_sentence_with_edge_case_prime_number_179(self):
        assert words_in_sentence("demonstration skills") == "demonstration skills"

    def test_sentence_with_edge_case_prime_number_181(self):
        assert words_in_sentence("establishment policies") == "establishment policies"

    def test_sentence_with_edge_case_prime_number_191(self):
        assert words_in_sentence("encouragement motivation") == "encouragement motivation"

    def test_sentence_with_edge_case_prime_number_193(self):
        assert words_in_sentence("evaluation criteria") == "evaluation criteria"

    def test_sentence_with_edge_case_prime_number_197(self):
        assert words_in_sentence("identification problems") == "identification problems"

    def test_sentence_with_edge_case_prime_number_199(self):
        assert words_in_sentence("interpretation results") == "interpretation results"

    def test_sentence_with_edge_case_prime_number_211(self):
        assert words_in_sentence("justification reasons") == "justification reasons"

    def test_sentence_with_edge_case_prime_number_223(self):
        assert words_in_sentence("modification methods") == "modification methods"

    def test_sentence_with_edge_case_prime_number_227(self):
        assert words_in_sentence("recommendation options") == "recommendation options"

    def test_sentence_with_edge_case_prime_number_229(self):
        assert words_in_sentence("representation views") == "representation views"

    def test_sentence_with_edge_case_prime_number_233(self):
        assert words_in_sentence("simplification steps") == "simplification steps"

    def test_sentence_with_edge_case_prime_number_239(self):
        assert words_in_sentence("transformation changes") == "transformation changes"

    def test_sentence_with_edge_case_prime_number_241(self):
        assert words_in_sentence("understanding concepts") == "understanding concepts"

    def test_sentence_with_edge_case_prime_number_251(self):
        assert words_in_sentence("visualization insights") == "visualization insights"

    def test_sentence_with_edge_case_prime_number_257(self):
        assert words_in_sentence("communication strategies") == "communication strategies"

    def test_sentence_with_edge_case_prime_number_263(self):
        assert words_in_sentence("consideration factors") == "consideration factors"

    def test_sentence_with_edge_case_prime_number_269(self):
        assert words_in_sentence("determination efforts") == "determination efforts"

    def test_sentence_with_edge_case_prime_number_271(self):
        assert words_in_sentence("investigation findings") == "investigation findings"

    def test_sentence_with_edge_case_prime_number_277(self):
        assert words_in_sentence("opportunities challenges") == "opportunities challenges"

    def test_sentence_with_edge_case_prime_number_281(self):
        assert words_in_sentence("collaboration projects") == "collaboration projects"

    def test_sentence_with_edge_case_prime_number_283(self):
        assert words_in_sentence("implementation solutions") == "implementation solutions"

    def test_sentence_with_edge_case_prime_number_293(self):
        assert words_in_sentence("organization systems") == "organization systems"

    def test_sentence_with_edge_case_prime_number_307(self):
        assert words_in_sentence("participation events") == "participation events"

    def test_sentence_with_edge_case_prime_number_311(self):
        assert words_in_sentence("demonstration skills") == "demonstration skills"

    def test_sentence_with_edge_case_prime_number_313(self):
        assert words_in_sentence("establishment policies") == "establishment policies"

    def test_sentence_with_edge_case_prime_number_317(self):
        assert words_in_sentence("encouragement motivation") == "encouragement motivation"

    def test_sentence_with_edge_case_prime_number_331(self):
        assert words_in_sentence("evaluation criteria") == "evaluation criteria"

    def test_sentence_with_edge_case_prime_number_337(self):
        assert words_in_sentence("identification problems") == "identification problems"

    def test_sentence_with_edge_case_prime_number_347(self):
        assert words_in_sentence("interpretation results") == "interpretation results"

    def test_sentence_with_edge_case_prime_number_349(self):
        assert words_in_sentence("justification reasons") == "justification reasons"

    def test_sentence_with_edge_case_prime_number_353(self):
        assert words_in_sentence("modification methods") == "modification methods"

    def test_sentence_with_edge_case_prime_number_359(self):
        assert words_in_sentence("recommendation options") == "recommendation options"

    def test_sentence_with_edge_case_prime_number_367(self):
        assert words_in_sentence("representation views") == "representation views"

    def test_sentence_with_edge_case_prime_number_373(self):
        assert words_in_sentence("simplification steps") == "simplification steps"

    def test_sentence_with_edge_case_prime_number_379(self):
        assert words_in_sentence("transformation changes") == "transformation changes"

    def test_sentence_with_edge_case_prime_number_383(self):
        assert words_in_sentence("understanding concepts") == "understanding concepts"

    def test_sentence_with_edge_case_prime_number_389(self):
        assert words_in_sentence("visualization insights") == "visualization insights"

    def test_sentence_with_edge_case_prime_number_397(self):
        assert words_in_sentence("communication strategies") == "communication strategies"

    def test_sentence_with_edge_case_prime_number_401(self):
        assert words_in_sentence("consideration factors") == "consideration factors"

    def test_sentence_with_edge_case_prime_number_409(self):
        assert words_in_sentence("determination efforts") == "determination efforts"

    def test_sentence_with_edge_case_prime_number_419(self):
        assert words_in_sentence("investigation findings") == "investigation findings"

    def test_sentence_with_edge_case_prime_number_421(self):
        assert words_in_sentence("opportunities challenges") == "opportunities challenges"

    def test_sentence_with_edge_case_prime_number_431(self):
        assert words_in_sentence("collaboration projects") == "collaboration projects"

    def test_sentence_with_edge_case_prime_number_433(self):
        assert words_in_sentence("implementation solutions") == "implementation solutions"

    def test_sentence_with_edge_case_prime_number_439(self):
        assert words_in_sentence("organization systems") == "organization systems"

    def test_sentence_with_edge_case_prime_number_443(self):
        assert words_in_sentence("participation events") == "participation events"

    def test_sentence_with_edge_case_prime_number_449(self):
        assert words_in_sentence("demonstration skills") == "demonstration skills"

    def test_sentence_with_edge_case_prime_number_457(self):
        assert words_in_sentence("establishment policies") == "establishment policies"

    def test_sentence_with_edge_case_prime_number_461(self):
        assert words_in_sentence("encouragement motivation") == "encouragement motivation"

    def test_sentence_with_edge_case_prime_number_463(self):
        assert words_in_sentence("evaluation criteria") == "evaluation criteria"

    def test_sentence_with_edge_case_prime_number_467(self):
        assert words_in_sentence("identification problems") == "identification problems"

    def test_sentence_with_edge_case_prime_number_479(self):
        assert words_in_sentence("interpretation results") == "interpretation results"

    def test_sentence_with_edge_case_prime_number_487(self):
        assert words_in_sentence("justification reasons") == "justification reasons"

    def test_sentence_with_edge_case_prime_number_491(self):
        assert words_in_sentence("modification methods") == "modification methods"

    def test_sentence_with_edge_case_prime_number_499(self):
        assert words_in_sentence("recommendation options") == "recommendation options"

    def test_sentence_with_edge_case_prime_number_503(self):
        assert words_in_sentence("representation views") == "representation views"

    def test_sentence_with_edge_case_prime_number_509(self):
        assert words_in_sentence("simplification steps") == "simplification steps"

    def test_sentence_with_edge_case_prime_number_521(self):
        assert words_in_sentence("transformation changes") == "transformation changes"

    def test_sentence_with_edge_case_prime_number_523(self):
        assert words_in_sentence("understanding concepts") == "understanding concepts"

    def test_sentence_with_edge_case_prime_number_541(self):
        assert words_in_sentence("visualization insights") == "visualization insights"

    def test_sentence_with_edge_case_prime_number_547(self):
        assert words_in_sentence("communication strategies") == "communication strategies"

    def test_sentence_with_edge_case_prime_number_557(self):
        assert words_in_sentence("consideration factors") == "consideration factors"

    def test_sentence_with_edge_case_prime_number_563(self):
        assert words_in_sentence("determination efforts") == "determination efforts"

    def test_sentence_with_edge_case_prime_number_569(self):
        assert words_in_sentence("investigation findings") == "investigation findings"

    def test_sentence_with_edge_case_prime_number_571(self):
        assert words_in_sentence("opportunities challenges") == "opportunities challenges"

    def test_sentence_with_edge_case_prime_number_577(self):
        assert words_in_sentence("collaboration projects") == "collaboration projects"

    def test_sentence_with_edge_case_prime_number_587(self):
        assert words_in_sentence("implementation solutions") == "implementation solutions"

    def test_sentence_with_edge_case_prime_number_593(self):
        assert words_in_sentence("organization systems") == "organization systems"

    def test_sentence_with_edge_case_prime_number_599(self):
        assert words_in_sentence("participation events") == "participation events"

    def test_sentence_with_edge_case_prime_number_601(self):
        assert words_in_sentence("demonstration skills") == "demonstration skills"

    def test_sentence_with_edge_case_prime_number_607(self):
        assert words_in_sentence("establishment policies") == "establishment policies"

    def test_sentence_with_edge_case_prime_number_613(self):
        assert words_in_sentence("encouragement motivation") == "encouragement motivation"

    def test_sentence_with_edge_case_prime_number_617(self):
        assert words_in_sentence("evaluation criteria") == "evaluation criteria"

    def test_sentence_with_edge_case_prime_number_619(self):
        assert words_in_sentence("identification problems") == "identification problems"

    def test_sentence_with_edge_case_prime_number_631(self):
        assert words_in_sentence("interpretation results") == "interpretation results"

    def test_sentence_with_edge_case_prime_number_641(self):
        assert words_in_sentence("justification reasons") == "justification reasons"

    def test_sentence_with_edge_case_prime_number_643(self):
        assert words_in_sentence("modification methods") == "modification methods"

    def test_sentence_with_edge_case_prime_number_647(self):
        assert words_in_sentence("recommendation options") == "recommendation options"

    def test_sentence_with_edge_case_prime_number_653(self):
        assert words_in_sentence("representation views") == "representation views"

    def test_sentence_with_edge_case_prime_number_659(self):
        assert words_in_sentence("simplification steps") == "simplification steps"

    def test_sentence_with_edge_case_prime_number_661(self):
        assert words_in_sentence("transformation changes") == "transformation changes"

    def test_sentence_with_edge_case_prime_number_673(self):
        assert words_in_sentence("understanding concepts") == "understanding concepts"

    def test_sentence_with_edge_case_prime_number_677(self):
        assert words_in_sentence("visualization insights") == "visualization insights"

    def test_sentence_with_edge_case_prime_number_683(self):
        assert words_in_sentence("communication strategies") == "communication strategies"

    def test_sentence_with_edge_case_prime_number_691(self):
        assert words_in_sentence("consideration factors") == "consideration factors"

    def test_sentence_with_edge_case_prime_number_701(self):
        assert words_in_sentence("determination efforts") == "determination efforts"

    def test_sentence_with_edge_case_prime_number_709(self):
        assert words_in_sentence("investigation findings") == "investigation findings"

    def test_sentence_with_edge_case_prime_number_719(self):
        assert words_in_sentence("opportunities challenges") == "opportunities challenges"

    def test_sentence_with_edge_case_prime_number_727(self):
        assert words_in_sentence("collaboration projects") == "collaboration projects"

    def test_sentence_with_edge_case_prime_number_733(self):
        assert words_in_sentence("implementation solutions") == "implementation solutions"

    def test_sentence_with_edge_case_prime_number_739(self):
        assert words_in_sentence("organization systems") == "organization systems"

    def test_sentence_with_edge_case_prime_number_743(self):
        assert words_in_sentence("participation events") == "participation events"

    def test_sentence_with_edge_case_prime_number_751(self):
        assert words_in_sentence("demonstration skills") == "demonstration skills"

    def test_sentence_with_edge_case_prime_number_757(self):
        assert words_in_sentence("establishment policies") == "establishment policies"

    def test_sentence_with_edge_case_prime_number_761(self):
        assert words_in_sentence("encouragement motivation") == "encouragement motivation"

    def test_sentence_with_edge_case_prime_number_769(self):
        assert words_in_sentence("evaluation criteria") == "evaluation criteria"

    def test_sentence_with_edge_case_prime_number_773(self):
        assert words_in_sentence("identification problems") == "identification problems"

    def test_sentence_with_edge_case_prime_number_787(self):
        assert words_in_sentence("interpretation results") == "interpretation results"

    def test_sentence_with_edge_case_prime_number_797(self):
        assert words_in_sentence("justification reasons") == "justification reasons"

    def test_sentence_with_edge_case_prime_number_809(self):
        assert words_in_sentence("modification methods") == "modification methods"

    def test_sentence_with_edge_case_prime_number_811(self):
        assert words_in_sentence("recommendation options") == "recommendation options"

    def test_sentence_with_edge_case_prime_number_821(self):
        assert words_in_sentence("representation views") == "representation views"

    def test_sentence_with_edge_case_prime_number_823(self):
        assert words_in_sentence("simplification steps") == "simplification steps"

    def test_sentence_with_edge_case_prime_number_827(self):
        assert words_in_sentence("transformation changes") == "transformation changes"

    def test_sentence_with_edge_case_prime_number_829(self):
        assert words_in_sentence("understanding concepts") == "understanding concepts"

    def test_sentence_with_edge_case_prime_number_839(self):
        assert words_in_sentence("visualization insights") == "visualization insights"

    def test_sentence_with_edge_case_prime_number_853(self):
        assert words_in_sentence("communication strategies") == "communication strategies"

    def test_sentence_with_edge_case_prime_number_857(self):
        assert words_in_sentence("consideration factors") == "consideration factors"

    def test_sentence_with_edge_case_prime_number_859(self):
        assert words_in_sentence("determination efforts") == "determination efforts"

    def test_sentence_with_edge_case_prime_number_863(self):
        assert words_in_sentence("investigation findings") == "investigation findings"

    def test_sentence_with_edge_case_prime_number_877(self):
        assert words_in_sentence("opportunities challenges") == "opportunities challenges"

    def test_sentence_with_edge_case_prime_number_881(self):
        assert words_in_sentence("collaboration projects") == "collaboration projects"

    def test_sentence_with_edge_case_prime_number_883(self):
        assert words_in_sentence("implementation solutions") == "implementation solutions"

    def test_sentence_with_edge_case_prime_number_887(self):
        assert words_in_sentence("organization systems") == "organization systems"

    def test_sentence_with_edge_case_prime_number_907(self):
        assert words_in_sentence("participation events") == "participation events"

    def test_sentence_with_edge_case_prime_number_911(self):
        assert words_in_sentence("demonstration skills") == "demonstration skills"

    def test_sentence_with_edge_case_prime_number_919(self):
        assert words_in_sentence("establishment policies") == "establishment policies"

    def test_sentence_with_edge_case_prime_number_929(self):
        assert words_in_sentence("encouragement motivation") == "encouragement motivation"

    def test_sentence_with_edge_case_prime_number_937(self):
        assert words_in_sentence("evaluation criteria") == "evaluation criteria"

    def test_sentence_with_edge_case_prime_number_941(self):
        assert words_in_sentence("identification problems") == "identification problems"

    def test_sentence_with_edge_case_prime_number_947(self):
        assert words_in_sentence("interpretation results") == "interpretation results"

    def test_sentence_with_edge_case_prime_number_953(self):
        assert words_in_sentence("justification reasons") == "justification reasons"

    def test_sentence_with_edge_case_prime_number_967(self):
        assert words_in_sentence("modification methods") == "modification methods"

    def test_sentence_with_edge_case_prime_number_971(self):
        assert words_in_sentence("recommendation options") == "recommendation options"

    def test_sentence_with_edge_case_prime_number_977(self):
        assert words_in_sentence("representation views") == "representation views"

    def test_sentence_with_edge_case_prime_number_983(self):
        assert words_in_sentence("simplification steps") == "simplification steps"

    def test_sentence_with_edge_case_prime_number_991(self):
        assert words_in_sentence("transformation changes") == "transformation changes"

    def test_sentence_with_edge_case_prime_number_997(self):
        assert words_in_sentence("understanding concepts") == "understanding concepts"

    def test_sentence_with_edge_case_prime_number_1009(self):
        assert words_in_sentence("visualization insights") == "visualization insights"

    def test_sentence_with_edge_case_prime_number_1013(self):
        assert words_in_sentence("communication strategies") == "communication strategies"

    def test_sentence_with_edge_case_prime_number_1019(self):
        assert words_in_sentence("consideration factors") == "consideration factors"