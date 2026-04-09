# Gemma 176-row Analysis

This report summarizes the 176 aggregated combinations (4 models x 11 agents x 4 prompts) computed as the mean over the 25 HumanEval problems in the detailed `results.csv` blocks.

## Model Summary

| model | combos | passed_mean | functional_correctness_mean | line_coverage_mean | mutation_score_mean | prompt_tokens_mean | completion_tokens_mean | total_tokens_mean | fc_per_1k_tokens | passed_per_1k_tokens | coverage_per_1k_tokens | mutation_per_1k_tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gemma-27b | 44 | 7.2284 | 0.6498 | 75.2548 | 0.7828 | 1015.9695 | 234.1583 | 2134.7710 | 0.6768 | 7.1328 | 74.2675 | 0.7336 |
| gemma-4b | 44 | 6.0032 | 0.6272 | 79.4373 | 0.8504 | 820.7973 | 141.8091 | 1741.2382 | 0.8218 | 7.4021 | 98.5326 | 1.0088 |
| gemma-12b | 44 | 2.9109 | 0.2529 | 73.0317 | 0.9514 | 842.1723 | 29.7918 | 868.5305 | 57.7314 | 562.4098 | 10810.5449 | 128.1087 |
| gemma-1b | 44 | 0.6273 | 0.0992 | 33.8493 | 0.9704 | 835.2264 | 506.9686 | 1341.2214 | 0.0847 | 0.4962 | 7804.0162 | 407.3522 |

## Main Takeaways

- Best overall by correctness: `gemma-27b`.
- Best average coverage and coverage per token: `gemma-4b`.
- Highest raw mutation score: `gemma-1b`.
- Highest mutation per 1k tokens: `gemma-12b`.

## Win Counts Across the 44 Agent/Prompt Combinations

- passed_mean: `gemma-27b` 29, `gemma-4b` 14, `gemma-12b` 1
- functional_correctness_mean: `gemma-27b` 27, `gemma-4b` 12, `gemma-12b` 5
- line_coverage_mean: `gemma-27b` 21, `gemma-4b` 12, `gemma-12b` 11
- mutation_score_mean: `gemma-1b` 22, `gemma-12b` 21, `gemma-4b` 1
- fc_per_1k_tokens: `gemma-4b` 23, `gemma-27b` 15, `gemma-12b` 6
- passed_per_1k_tokens: `gemma-4b` 19, `gemma-27b` 17, `gemma-12b` 8
- coverage_per_1k_tokens: `gemma-4b` 26, `gemma-27b` 9, `gemma-12b` 8, `gemma-1b` 1
- mutation_per_1k_tokens: `gemma-12b` 28, `gemma-4b` 10, `gemma-1b` 5, `gemma-27b` 1
