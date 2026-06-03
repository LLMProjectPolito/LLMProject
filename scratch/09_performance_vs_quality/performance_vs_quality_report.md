# Performance vs Quality Correlation Analysis

## Correlation with Functional Correctness
- **line_coverage**: 0.7200
- **diversity_score**: 0.4207
- **mutation_score**: 0.4056
- **bloat_ratio**: 0.3121
- **maintainability_mi**: 0.1739
- **complexity_cc**: -0.0355
- **duplication_ratio**: -0.4351
- **similarity_score**: -0.5238

## Key Observations
- **Clean Code Paradox**: Check the scatter plot. High maintainability doesn't always guarantee correctness, but low maintainability almost always correlates with low correctness.
- **Diversity Impact**: High diversity scores show a positive trend with Line Coverage, confirming that 'creative' agents explore more paths.
- **Bloat Ratio Correlation**: Bloat ratio has a correlation of **0.3121** with functional correctness and **0.2656** with line coverage. A lower bloat ratio is generally better for readability and code maintainability, showing how concise solutions relate to overall model performance.