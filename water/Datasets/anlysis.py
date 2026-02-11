#source venv/bin/activate

#Load the required datasets
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'/Users/sudipbhandari/Desktop/DataThon-2026/DataPie-2026/water/cleaned.csv')
print(df)

# Trim first column for reuse
df.iloc[:, 0] = df.iloc[:, 0].astype(str).str[7:]
print(df)

plt.figure(figsize=(10, 6))

bars = plt.barh(
    df['DISCHARGE_TYPE'],
    df['Reuse_Volume'],
    color=plt.cm.Set2.colors  # nice color palette
)

plt.xlabel('Total Reuse Volume (MGD)', fontsize=12)
plt.ylabel('DISCHARGE Type', fontsize=12)
plt.title('Total Reuse Volume by DISCHARGE TYPE', fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Add labels inside the bars
for bar in bars:
    width = bar.get_width()
    plt.text(
        width - (0.05*width),  # slightly left from end of bar
        bar.get_y() + bar.get_height()/2,  # vertical center of bar
        f'{int(width)}',        # label text
        ha='right',             # align text to the right
        va='center',            # vertical alignment
        color='white',          # text color
        fontsize=10
    )

plt.tight_layout()
plt.savefig('reuse_volume_horizontal.png')
plt.show()