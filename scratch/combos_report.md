# Analisi Combinazioni Migliori e Peggiori per Modello

## Modello: GEMMA-12B
### 🏆 Top 10 Combinazioni
| model_family   | agent        | config_label        |   functional_correctness |   line_coverage |   branch_coverage |   mutation_score |   complexity_cc |   maintainability_mi |   total_tokens |   tasks_evaluated |
|:---------------|:-------------|:--------------------|-------------------------:|----------------:|------------------:|-----------------:|----------------:|---------------------:|---------------:|------------------:|
| gemma-12b      | actor_critic | gemma-12b:cot       |                     0.72 |           86.48 |             67.41 |             0.92 |            2.53 |                68.53 |        2874.60 |                25 |
| gemma-12b      | baseline     | gemma-12b:scot      |                     0.70 |           83.92 |             67.35 |             0.85 |            2.36 |                63.46 |        1770.52 |                25 |
| gemma-12b      | adversarial  | gemma-12b:cot       |                     0.68 |           85.17 |             70.36 |             0.89 |            2.77 |                71.09 |         890.68 |                25 |
| gemma-12b      | hybrid       | gemma-12b:cot       |                     0.62 |           85.05 |             64.32 |             0.97 |            2.81 |                68.43 |        3133.76 |                25 |
| gemma-12b      | hybrid       | gemma-12b:few_shot  |                     0.62 |           88.41 |             74.48 |             0.86 |            2.91 |                61.82 |        2667.80 |                25 |
| gemma-12b      | adversarial  | gemma-12b:scot      |                     0.59 |           85.33 |             67.57 |             0.66 |            2.31 |                70.53 |        1772.68 |                25 |
| gemma-12b      | actor_critic | gemma-12b:few_shot  |                     0.56 |           70.45 |             56.22 |             0.92 |            2.79 |                74.36 |        2317.48 |                25 |
| gemma-12b      | competitive  | gemma-12b:cot       |                     0.46 |           77.95 |             48.00 |             0.89 |            3.29 |                71.86 |           0.00 |                25 |
| gemma-12b      | actor_critic | gemma-12b:scot      |                     0.46 |           86.39 |             62.74 |             0.97 |            2.48 |                69.95 |        2281.64 |                25 |
| gemma-12b      | competitive  | gemma-12b:zero_shot |                     0.44 |           76.93 |             47.56 |             0.89 |            3.29 |                71.98 |           0.00 |                25 |

### 💔 Bottom 5 Combinazioni
| model_family   | agent   | config_label       |   functional_correctness |   line_coverage |   branch_coverage |   mutation_score |   complexity_cc |   maintainability_mi |   total_tokens |   tasks_evaluated |
|:---------------|:--------|:-------------------|-------------------------:|----------------:|------------------:|-----------------:|----------------:|---------------------:|---------------:|------------------:|
| gemma-12b      | swarm   | gemma-12b:scot     |                     0.00 |           52.63 |             17.60 |             1.00 |            1.61 |                82.46 |        1774.92 |                25 |
| gemma-12b      | coa     | gemma-12b:scot     |                     0.01 |           71.02 |             16.21 |             1.00 |            2.13 |                79.43 |        1379.92 |                25 |
| gemma-12b      | coa     | gemma-12b:few_shot |                     0.01 |           71.91 |             20.21 |             1.00 |            2.17 |                79.18 |        1214.48 |                25 |
| gemma-12b      | coa     | gemma-12b:cot      |                     0.01 |           72.03 |             20.25 |             1.00 |            2.18 |                79.17 |        1851.80 |                25 |
| gemma-12b      | swarm   | gemma-12b:cot      |                     0.02 |           56.03 |             17.44 |             1.00 |            1.65 |                84.09 |        1382.80 |                25 |

---

## Modello: GEMMA-1B
### 🏆 Top 10 Combinazioni
| model_family   | agent        | config_label       |   functional_correctness |   line_coverage |   branch_coverage |   mutation_score |   complexity_cc |   maintainability_mi |   total_tokens |   tasks_evaluated |
|:---------------|:-------------|:-------------------|-------------------------:|----------------:|------------------:|-----------------:|----------------:|---------------------:|---------------:|------------------:|
| gemma-1b       | actor_critic | gemma-1b:few_shot  |                     0.55 |           63.45 |             59.40 |             0.66 |            2.84 |                77.26 |        5292.56 |                25 |
| gemma-1b       | hybrid       | gemma-1b:few_shot  |                     0.41 |           64.32 |             49.45 |             0.74 |            1.79 |                61.11 |        4812.56 |                25 |
| gemma-1b       | adversarial  | gemma-1b:few_shot  |                     0.39 |           51.13 |             45.31 |             0.71 |            2.41 |                73.38 |         888.92 |                25 |
| gemma-1b       | actor_critic | gemma-1b:zero_shot |                     0.25 |           61.90 |             47.77 |             1.00 |            3.34 |                66.53 |        3927.96 |                25 |
| gemma-1b       | adversarial  | gemma-1b:scot      |                     0.23 |           51.22 |             38.20 |             0.96 |            3.70 |                70.57 |        1123.96 |                25 |
| gemma-1b       | adversarial  | gemma-1b:zero_shot |                     0.23 |           55.45 |             38.62 |             1.00 |            2.83 |                74.53 |        1901.72 |                25 |
| gemma-1b       | hybrid       | gemma-1b:zero_shot |                     0.22 |           56.62 |             41.47 |             0.96 |            2.89 |                64.40 |        5550.28 |                25 |
| gemma-1b       | hybrid       | gemma-1b:scot      |                     0.21 |           57.62 |             46.88 |             1.00 |            3.22 |                67.84 |        3171.04 |                25 |
| gemma-1b       | actor_critic | gemma-1b:scot      |                     0.18 |           52.53 |             42.83 |             1.00 |            4.55 |                72.67 |        6083.96 |                25 |
| gemma-1b       | baseline     | gemma-1b:zero_shot |                     0.18 |           40.60 |             25.69 |             1.00 |            2.49 |                68.68 |        2167.20 |                25 |

### 💔 Bottom 5 Combinazioni
| model_family   | agent        | config_label       |   functional_correctness |   line_coverage |   branch_coverage |   mutation_score |   complexity_cc |   maintainability_mi |   total_tokens |   tasks_evaluated |
|:---------------|:-------------|:-------------------|-------------------------:|----------------:|------------------:|-----------------:|----------------:|---------------------:|---------------:|------------------:|
| gemma-1b       | atomic_swarm | gemma-1b:few_shot  |                     0.00 |           14.86 |              0.67 |             1.00 |            4.59 |                66.93 |        1499.88 |                25 |
| gemma-1b       | atomic_swarm | gemma-1b:cot       |                     0.00 |           15.27 |              0.69 |             1.00 |            3.74 |                65.37 |        2008.48 |                25 |
| gemma-1b       | atomic_swarm | gemma-1b:scot      |                     0.00 |           15.53 |              0.67 |             1.00 |            3.96 |                68.05 |        3477.12 |                25 |
| gemma-1b       | atomic_swarm | gemma-1b:zero_shot |                     0.00 |           15.57 |              0.62 |             1.00 |            3.84 |                68.27 |        2454.64 |                25 |
| gemma-1b       | baseline     | gemma-1b:cot       |                     0.00 |           18.07 |              2.28 |             1.00 |            2.54 |                73.21 |        2034.64 |                25 |

---

## Modello: GEMMA-27B
### 🏆 Top 10 Combinazioni
| model_family   | agent        | config_label        |   functional_correctness |   line_coverage |   branch_coverage |   mutation_score |   complexity_cc |   maintainability_mi |   total_tokens |   tasks_evaluated |
|:---------------|:-------------|:--------------------|-------------------------:|----------------:|------------------:|-----------------:|----------------:|---------------------:|---------------:|------------------:|
| gemma-27b      | hybrid       | gemma-27b:scot      |                     0.81 |           82.16 |             64.57 |             0.62 |            2.33 |                72.49 |        3003.72 |                25 |
| gemma-27b      | baseline     | gemma-27b:scot      |                     0.79 |           81.91 |             61.13 |             0.66 |            2.38 |                74.17 |        2548.56 |                25 |
| gemma-27b      | adversarial  | gemma-27b:scot      |                     0.77 |           81.70 |             64.95 |             0.67 |            2.31 |                71.01 |        1224.36 |                25 |
| gemma-27b      | baseline     | gemma-27b:zero_shot |                     0.75 |           83.07 |             64.10 |             0.78 |            2.45 |                72.22 |        1547.44 |                25 |
| gemma-27b      | actor_critic | gemma-27b:zero_shot |                     0.75 |           85.23 |             70.84 |             0.86 |            2.59 |                68.50 |        2862.12 |                25 |
| gemma-27b      | adversarial  | gemma-27b:zero_shot |                     0.75 |           83.68 |             65.45 |             0.86 |            2.46 |                71.38 |        1602.44 |                25 |
| gemma-27b      | hybrid       | gemma-27b:few_shot  |                     0.74 |           87.38 |             71.75 |             0.93 |            2.43 |                58.61 |        4199.48 |                25 |
| gemma-27b      | adversarial  | gemma-27b:few_shot  |                     0.73 |           83.92 |             66.50 |             0.82 |            2.55 |                70.57 |        2612.20 |                25 |
| gemma-27b      | hybrid       | gemma-27b:zero_shot |                     0.73 |           85.12 |             63.13 |             0.89 |            2.63 |                61.54 |        3842.88 |                25 |
| gemma-27b      | actor_critic | gemma-27b:scot      |                     0.68 |           82.30 |             61.88 |             0.77 |            2.17 |                69.03 |        2481.68 |                25 |

### 💔 Bottom 5 Combinazioni
| model_family   | agent       | config_label        |   functional_correctness |   line_coverage |   branch_coverage |   mutation_score |   complexity_cc |   maintainability_mi |   total_tokens |   tasks_evaluated |
|:---------------|:------------|:--------------------|-------------------------:|----------------:|------------------:|-----------------:|----------------:|---------------------:|---------------:|------------------:|
| gemma-27b      | adversarial | gemma-27b:cot       |                     0.00 |           64.52 |             11.88 |             1.00 |            2.71 |                69.28 |        2014.56 |                25 |
| gemma-27b      | competitive | gemma-27b:cot       |                     0.03 |           73.34 |             20.29 |             1.00 |            2.18 |                71.66 |           0.00 |                25 |
| gemma-27b      | competitive | gemma-27b:scot      |                     0.03 |           73.48 |             20.12 |             1.00 |            2.40 |                70.58 |           0.00 |                25 |
| gemma-27b      | competitive | gemma-27b:few_shot  |                     0.04 |           73.39 |             20.17 |             1.00 |            2.41 |                70.50 |           0.00 |                25 |
| gemma-27b      | competitive | gemma-27b:zero_shot |                     0.04 |           73.48 |             20.17 |             1.00 |            2.39 |                70.39 |           0.00 |                25 |

---

## Modello: GEMMA-31B
### 🏆 Top 10 Combinazioni
| model_family   | agent        | config_label        |   functional_correctness |   line_coverage |   branch_coverage |   mutation_score |   complexity_cc |   maintainability_mi |   total_tokens |   tasks_evaluated |
|:---------------|:-------------|:--------------------|-------------------------:|----------------:|------------------:|-----------------:|----------------:|---------------------:|---------------:|------------------:|
| gemma-31b      | hybrid       | gemma-31b:zero_shot |                     0.98 |           81.09 |             61.62 |             0.33 |            2.49 |                77.51 |        8447.92 |                25 |
| gemma-31b      | hybrid       | gemma-31b:cot       |                     0.96 |           99.04 |             98.65 |             0.57 |            2.69 |                83.10 |       10841.08 |                25 |
| gemma-31b      | adversarial  | gemma-31b:scot      |                     0.96 |           98.18 |             99.01 |             0.62 |            2.38 |                83.14 |        6934.76 |                25 |
| gemma-31b      | swarm        | gemma-31b:cot       |                     0.96 |           95.23 |             91.07 |             0.40 |            2.00 |                93.02 |        5575.96 |                25 |
| gemma-31b      | baseline     | gemma-31b:few_shot  |                     0.96 |           99.57 |             99.33 |             0.56 |            2.79 |                75.54 |        6044.84 |                25 |
| gemma-31b      | hybrid       | gemma-31b:scot      |                     0.95 |           99.53 |             99.33 |             0.69 |            2.49 |                79.67 |       10545.80 |                25 |
| gemma-31b      | actor_critic | gemma-31b:zero_shot |                     0.95 |           75.71 |             59.81 |             0.21 |            2.49 |                84.96 |        8348.04 |                25 |
| gemma-31b      | coa          | gemma-31b:cot       |                     0.94 |           98.33 |             96.65 |             0.57 |            2.59 |                76.85 |        7618.40 |                25 |
| gemma-31b      | swarm        | gemma-31b:scot      |                     0.93 |           94.07 |             87.33 |             0.40 |            2.00 |                85.58 |        6534.04 |                25 |
| gemma-31b      | consensus    | gemma-31b:few_shot  |                     0.93 |           99.07 |             98.26 |             0.60 |            2.59 |                79.82 |        8128.48 |                25 |

### 💔 Bottom 5 Combinazioni
| model_family   | agent        | config_label        |   functional_correctness |   line_coverage |   branch_coverage |   mutation_score |   complexity_cc |   maintainability_mi |   total_tokens |   tasks_evaluated |
|:---------------|:-------------|:--------------------|-------------------------:|----------------:|------------------:|-----------------:|----------------:|---------------------:|---------------:|------------------:|
| gemma-31b      | self_healing | gemma-31b:zero_shot |                     0.20 |           30.66 |             14.08 |             0.80 |            3.04 |                80.86 |        7783.20 |                25 |
| gemma-31b      | self_healing | gemma-31b:cot       |                     0.20 |           32.61 |             15.20 |             0.81 |            2.97 |                78.28 |        6887.68 |                25 |
| gemma-31b      | self_healing | gemma-31b:few_shot  |                     0.24 |           34.77 |             17.24 |             0.77 |            2.93 |                81.68 |        8431.96 |                25 |
| gemma-31b      | self_healing | gemma-31b:scot      |                     0.28 |           36.73 |             24.31 |             0.73 |            3.06 |                80.86 |        7823.60 |                25 |
| gemma-31b      | hybrid       | gemma-31b:few_shot  |                     0.54 |           64.87 |             48.73 |             0.71 |            1.97 |                91.63 |        9119.96 |                25 |

---

## Modello: GEMMA-4B
### 🏆 Top 10 Combinazioni
| model_family   | agent        | config_label       |   functional_correctness |   line_coverage |   branch_coverage |   mutation_score |   complexity_cc |   maintainability_mi |   total_tokens |   tasks_evaluated |
|:---------------|:-------------|:-------------------|-------------------------:|----------------:|------------------:|-----------------:|----------------:|---------------------:|---------------:|------------------:|
| gemma-4b       | baseline     | gemma-4b:few_shot  |                     0.77 |           83.56 |             71.23 |             0.82 |            2.41 |                70.31 |        1620.24 |                25 |
| gemma-4b       | adversarial  | gemma-4b:few_shot  |                     0.76 |           87.28 |             74.26 |             0.93 |            2.75 |                61.29 |        1579.40 |                25 |
| gemma-4b       | actor_critic | gemma-4b:few_shot  |                     0.75 |           85.39 |             72.18 |             0.85 |            2.41 |                64.37 |        2130.08 |                25 |
| gemma-4b       | swarm        | gemma-4b:zero_shot |                     0.72 |           77.45 |             61.61 |             0.70 |            2.07 |                74.23 |        2043.80 |                25 |
| gemma-4b       | hybrid       | gemma-4b:few_shot  |                     0.71 |           84.84 |             75.17 |             1.00 |            3.39 |                54.79 |        3613.64 |                25 |
| gemma-4b       | swarm        | gemma-4b:scot      |                     0.70 |           79.57 |             66.06 |             0.77 |            2.17 |                76.85 |        2360.28 |                25 |
| gemma-4b       | hybrid       | gemma-4b:scot      |                     0.68 |           79.97 |             66.23 |             0.82 |            2.56 |                68.31 |        2367.52 |                25 |
| gemma-4b       | competitive  | gemma-4b:zero_shot |                     0.67 |           82.97 |             67.31 |             0.86 |            2.34 |                74.05 |           0.00 |                25 |
| gemma-4b       | competitive  | gemma-4b:scot      |                     0.66 |           82.52 |             67.54 |             0.89 |            2.36 |                74.01 |           0.00 |                25 |
| gemma-4b       | competitive  | gemma-4b:cot       |                     0.64 |           82.89 |             68.22 |             0.93 |            2.39 |                74.04 |           0.00 |                25 |

### 💔 Bottom 5 Combinazioni
| model_family   | agent       | config_label       |   functional_correctness |   line_coverage |   branch_coverage |   mutation_score |   complexity_cc |   maintainability_mi |   total_tokens |   tasks_evaluated |
|:---------------|:------------|:-------------------|-------------------------:|----------------:|------------------:|-----------------:|----------------:|---------------------:|---------------:|------------------:|
| gemma-4b       | coa         | gemma-4b:few_shot  |                     0.01 |           70.16 |             21.17 |             1.00 |            1.95 |                75.54 |        1428.08 |                25 |
| gemma-4b       | coa         | gemma-4b:cot       |                     0.01 |           70.39 |             21.25 |             1.00 |            1.94 |                75.40 |        1199.08 |                25 |
| gemma-4b       | coa         | gemma-4b:scot      |                     0.01 |           70.67 |             21.25 |             1.00 |            1.92 |                75.60 |        1544.84 |                25 |
| gemma-4b       | coa         | gemma-4b:zero_shot |                     0.02 |           70.24 |             21.25 |             1.00 |            1.94 |                75.35 |        1973.24 |                25 |
| gemma-4b       | adversarial | gemma-4b:scot      |                     0.35 |           74.50 |             53.67 |             0.96 |            1.74 |                45.26 |        1646.08 |                25 |

---

