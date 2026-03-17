DEFAULT_MODELS = {
    # Using Groq IDs updated in model_registry
    "baseline":         {"model":              "llama3-70b"},
    
    "actor_critic":     {"driver_model":       "llama3-70b",
                         "navigator_model":    "llama3-8b"},
                         
    "adversarial":      {"hacker_model":       "qwen",
                         "tester_model":       "llama3-70b"},
                         
    "competitive":      {"models":            ["llama3-70b", "qwen", "scout"]},
    
    "hybrid":           {"generate_model":     "llama3-70b",
                         "evolve_model":       "llama3-8b"},
                         
    "coa":              {"manager_model":      "llama3-70b",
                         "worker_model":       "llama3-8b"},
                         
    "soa":              {"orchestrator_model": "llama3-70b",
                         "specialist_model":   "llama3-8b"},
                         
    "swarm":            {"worker_model":       "llama3-8b",
                         "aggregator_model":   "llama3-70b",
                         "n":                 3},
                         
    "consensus":        {"generation_model":   "llama3-70b",
                         "debate_model":       "llama3-8b"},
                         
    "self_healing":     {"model":              "llama3-8b"},
    
    "atomic_swarm":     {"model":              "llama3-8b"},
}
