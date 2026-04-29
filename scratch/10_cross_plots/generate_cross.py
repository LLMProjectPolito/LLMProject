import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_cross_plots(results_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    models = ["gemma-1b", "gemma-4b", "gemma-12b", "gemma-27b", "gemma-31b", "gemma-4-2b", "gemma-4-4b", "gemma-4-26b"]
    
    for model in models:
        model_path = os.path.join(results_dir, model)
        csv_path = os.path.join(model_path, 'results.csv')
        if not os.path.exists(csv_path):
            continue
            
        df = pd.read_csv(csv_path)
        df['prompt'] = df['config_label'].apply(lambda x: str(x).split(':')[-1])
        
        # Aggregate to mean functional correctness for specific combinations
        combo_group = df.groupby(['agent', 'prompt'])['functional_correctness'].mean().reset_index()
        
        # 1. Center: baseline + zero_shot
        center_row = combo_group[(combo_group['agent'] == 'baseline') & (combo_group['prompt'] == 'zero_shot')]
        if center_row.empty:
            continue
        center_score = center_row.iloc[0]['functional_correctness']
        
        # 2. Horizontal: Best and Worst Prompt (averaged across ALL agents)
        prompt_avg = df.groupby('prompt')['functional_correctness'].mean()
        best_prompt = prompt_avg.idxmax()
        best_prompt_score = prompt_avg.max()
        worst_prompt = prompt_avg.idxmin()
        worst_prompt_score = prompt_avg.min()
        
        # 3. Vertical: Best and Worst Agent (averaged across ALL prompts)
        agent_avg = df.groupby('agent')['functional_correctness'].mean()
        best_agent = agent_avg.idxmax()
        best_agent_score = agent_avg.max()
        worst_agent = agent_avg.idxmin()
        worst_agent_score = agent_avg.min()
        
        def perc(score):
            if center_score == 0: return "+0.0%"
            val = ((score - center_score) / center_score) * 100
            return f"{val:+.1f}%"

        # Coordinate mapping
        points = {
            'Center': {'x': 0, 'y': 0, 'label': f"Baseline (zero_shot)\nFC: {center_score:.3f}", 'score': center_score, 'color': '#2E75B6'},
            'Left': {'x': -1, 'y': 0, 'label': f"Worst Prompt: {worst_prompt}\nAvg FC: {worst_prompt_score:.3f} ({perc(worst_prompt_score)})", 'score': worst_prompt_score, 'color': '#8B1A1A'},
            'Right': {'x': 1, 'y': 0, 'label': f"Best Prompt: {best_prompt}\nAvg FC: {best_prompt_score:.3f} ({perc(best_prompt_score)})", 'score': best_prompt_score, 'color': '#1B3A5C'},
            'Bottom': {'x': 0, 'y': -1, 'label': f"Worst Agent: {worst_agent}\nAvg FC: {worst_agent_score:.3f} ({perc(worst_agent_score)})", 'score': worst_agent_score, 'color': '#8B1A1A'},
            'Top': {'x': 0, 'y': 1, 'label': f"Best Agent: {best_agent}\nAvg FC: {best_agent_score:.3f} ({perc(best_agent_score)})", 'score': best_agent_score, 'color': '#1B3A5C'}
        }
        
        # Plot
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Draw lines (Cross)
        ax.plot([points['Left']['x'], points['Right']['x']], [points['Left']['y'], points['Right']['y']], color='gray', linestyle='-', linewidth=2, zorder=1)
        ax.plot([points['Bottom']['x'], points['Top']['x']], [points['Bottom']['y'], points['Top']['y']], color='gray', linestyle='-', linewidth=2, zorder=1)
        
        # Draw points
        for key, pt in points.items():
            ax.scatter(pt['x'], pt['y'], color=pt['color'], s=1500, zorder=2, edgecolors='white', linewidth=3)
            
            # Annotate
            if key == 'Top':
                offset_x, offset_y = 0, 0.18
            elif key == 'Bottom':
                offset_x, offset_y = 0, -0.18
            elif key == 'Left':
                offset_x, offset_y = -0.05, -0.18
            elif key == 'Right':
                offset_x, offset_y = 0.05, -0.18
            else: # Center
                offset_x, offset_y = 0.15, 0.15
                
            ax.text(pt['x'] + offset_x, pt['y'] + offset_y, pt['label'], 
                    ha='center', va='center', fontsize=11, fontweight='bold',
                    bbox=dict(facecolor='white', alpha=0.9, edgecolor=pt['color'], boxstyle='round,pad=0.5'))

        # Add text explanations
        ax.text(0, 1.35, "AGENT EVOLUTION\n(Averaged across all Prompts)", ha='center', va='center', fontsize=13, fontweight='bold', color='#333333')
        ax.text(1.35, 0, "PROMPT EVOLUTION\n(Averaged across all Agents)", ha='center', va='center', fontsize=13, fontweight='bold', color='#333333', rotation=-90)

        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.axis('off') # Hide axes
        
        plt.title(f'Macroscopic Evolution Cross - {model.upper()}', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        
        plot_path = os.path.join(output_dir, f"{model}_cross.png")
        plt.savefig(plot_path, dpi=150, facecolor='white')
        plt.close()
        print(f"Created macroscopic cross plot for {model}")

if __name__ == "__main__":
    generate_cross_plots('results', 'scratch/10_cross_plots/plots')
