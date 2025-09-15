
# Aghajanian copyright 2025

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Example data dictionary
data = {
    'Group': ['SA-FST']*3 + ['SA-FPL']*3 + ['SA-FPP']*3 + ['SA-FSN']*3 + ['SA-C']*3,
    'Strength': [53.2, 52.9, 53.5, 48.2, 48.1, 48.4, 45.1, 45.4, 44.9, 47.1, 46.8, 47.0, 50.2, 50.0, 49.9]
}
df = pd.DataFrame(data)

# 1) Test normality per group (Shapiro-Wilk)
for grp in df['Group'].unique():
    stat, p = stats.shapiro(df[df['Group']==grp]['Strength'])
    print(f"{grp}: Shapiro-Wilk p={p:.3f}")

# 2) Test homogeneity of variances (Levene)
groups = [df[df['Group']==grp]['Strength'] for grp in df['Group'].unique()]
stat, p = stats.levene(*groups)
print(f"Levene p={p:.3f}")

# 3) If assumptions met -> One-way ANOVA
f_stat, p_value = stats.f_oneway(*groups)
print(f"ANOVA F={f_stat:.3f}, p={p_value:.4f}")

# 4) Effect size (eta squared)
ss_between = sum([len(g)*(np.mean(g)-df['Strength'].mean())**2 for g in groups])
ss_total = sum((df['Strength'] - df['Strength'].mean())**2)
eta2 = ss_between/ss_total
print(f"eta-squared = {eta2:.3f}")

# 5) Post-hoc Tukey HSD (if ANOVA significant)
if p_value < 0.05:
    tukey = pairwise_tukeyhsd(df['Strength'], df['Group'], alpha=0.05)
    print(tukey
