# ANOVA
Python script for statistical analysis of fiber-reinforced slag concrete mixtures. Performs Shapiro-Wilk normality test, Levene’s variance homogeneity test, one-way ANOVA, eta-squared effect size, and post-hoc Tukey HSD to compare compressive and flexural strength across groups.

# Fiber-Reinforced Slag Concrete ANOVA Analysis

This Python script performs a statistical analysis of compressive and flexural strength for different fiber-reinforced slag concrete mixtures.

## Features
1. **Normality test** per group using Shapiro-Wilk test.
2. **Homogeneity of variances** test using Levene's test.
3. **One-way ANOVA** to assess differences between groups.
4. **Effect size** calculation (eta-squared).
5. **Post-hoc analysis** using Tukey HSD if ANOVA is significant.

## Data Format
The script expects a pandas DataFrame with:
- `Group`: Group names (e.g., SA-FST, SA-FPL, SA-FPP, SA-FSN, SA-C)
- `Strength`: Numeric values of compressive/flexural strength

### Requirements
	•	pandas
	•	numpy
	•	scipy
	•	statsmodels

### License

This software is released under the MIT License. See the `LICENSE` file for more details.

**© 2024 All rights reserved - Aghajanian | © 2024**

---


### Run the script directly
python anova_analysis.py

## Usage
```python
# Run the script directly
# python anova_analysis.py

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
<img width="468" height="396" alt="image" src="https://github.com/user-attachments/assets/dd7688c5-f613-48f2-9577-97c61fbf637e" />
