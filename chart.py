import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Synthetic data (same seed = reproducible)
np.random.seed(42)
channels = ['Email', 'Phone', 'Chat', 'Social Media']
n = 500
data = {
    'Channel': np.repeat(channels, n),
    'Response Time (minutes)': np.concatenate([
        np.random.lognormal(4.5, 0.8, n),
        np.random.lognormal(3.0, 0.6, n),
        np.random.lognormal(1.2, 0.7, n),
        np.random.lognormal(3.8, 0.9, n),
    ])
}
df = pd.DataFrame(data)

sns.set_style("whitegrid")
sns.set_context("talk")
plt.figure(figsize=(8, 8))
sns.violinplot(data=df, x='Channel', y='Response Time (minutes)',
               palette='Set2', inner='quartile', linewidth=1.5)
plt.title('Response Time Distribution by Support Channel', fontsize=18, pad=20)
plt.xlabel('Support Channel', fontsize=14)
plt.ylabel('Response Time (minutes)', fontsize=14)
plt.xticks(rotation=15)
plt.savefig('chart.png', dpi=64, bbox_inches='tight', facecolor='white')
