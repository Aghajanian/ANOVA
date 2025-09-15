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

## Usage
```python
# Run the script directly
python anova_analysis.py

# Requirements
	•	pandas
	•	numpy
	•	scipy
	•	statsmodels

# License

This code is provided for research and educational purposes.
