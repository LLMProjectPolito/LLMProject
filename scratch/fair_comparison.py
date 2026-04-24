import pandas as pd
import os

agents_intersect = ['baseline', 'adversarial', 'consensus', 'hybrid', 'actor_critic']
styles_intersect = ['zero_shot', 'scot', 'few_shot']

def get_fair_avg(model_name):
    path = os.path.join('results', model_name, 'results.csv')
    if not os.path.exists(path): return None
    
    df = pd.read_csv(path)
    # Extract style from config_label
    df['style'] = df['config_label'].apply(lambda x: x.split(':')[-1])
    
    # Filter for intersection
    mask = (df['agent'].isin(agents_intersect)) & (df['style'].isin(styles_intersect))
    fair_df = df[mask]
    
    if fair_df.empty: return None
    return fair_df['functional_correctness'].mean()

models = [
    ('gemma-1b', 'Gen 3'),
    ('gemma-4b', 'Gen 3'),
    ('gemma-27b', 'Gen 3'),
    ('gemma-4-2b', 'Gen 4'),
    ('gemma-4-4b', 'Gen 4'),
    ('gemma-4-26b', 'Gen 4')
]

print(f"{'Model':<15} | {'Generation':<10} | {'Fair Avg Score':<15}")
print("-" * 45)
for m, gen in models:
    score = get_fair_avg(m)
    if score is not None:
        print(f"{m:<15} | {gen:<10} | {score:.4f}")
    else:
        print(f"{m:<15} | {gen:<10} | N/A")
