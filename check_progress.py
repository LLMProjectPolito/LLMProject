import csv
from collections import defaultdict

rows = list(csv.DictReader(open(r'results\turbo_start_139_n_145602\results.csv')))
print(f'Totale righe: {len(rows)} / 2000')
print()

by_label = defaultdict(list)
for r in rows:
    by_label[r['config_label']].append((float(r['functional_correctness']), int(r['total_tokens']), float(r['elapsed_s'])))

print(f"{'Config':<32} {'N':>4} {'FC avg':>8} {'Tokens avg':>12} {'Time avg':>10}")
print('-' * 72)
for k, vals in sorted(by_label.items()):
    fc_avg   = sum(v[0] for v in vals) / len(vals)
    tok_avg  = sum(v[1] for v in vals) / len(vals)
    time_avg = sum(v[2] for v in vals) / len(vals)
    print(f"{k:<32} {len(vals):>4} {fc_avg:>8.3f} {tok_avg:>12.0f} {time_avg:>10.1f}s")
