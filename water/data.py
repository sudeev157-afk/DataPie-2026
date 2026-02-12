#source venv/bin/activate

#Load the required datasets
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Load the discharges datase and filter it for only reuse water
df = pd.read_csv(r'/Users/sudipbhandari/Desktop/DataThon-2026/DataPie-2026/water/Datasets/DISCHARGES.csv')
filtered_df = df[df["DISCHARGE_TYPE"].str.contains("Reuse", case=False, na=False)]
#print(filtered_df)

#Load facilities dataset
df1 = pd.read_csv("/Users/sudipbhandari/Desktop/DataThon-2026/DataPie-2026/water/Solution/FACILITIES.csv", encoding="latin1")
#print(df1)

#Load flow dataset and filter for flow type as Total Flow
df2 = pd.read_csv("/Users/sudipbhandari/Desktop/DataThon-2026/DataPie-2026/water/Solution/FLOW.csv", encoding="latin1")
filtered_df2 = df2[df2['FLOW_TYPE'] == 'Total Flow']
#print(filtered_df2)

#Join the datasets
# Replace 'JOIN_COLUMN' with the common ID (e.g., 'Site_ID' or 'Date')
merged_df = pd.merge(filtered_df, filtered_df2, on='CWNS_ID', how='left')
pd.set_option('display.max_columns', None)
print(merged_df)

#Removing data type conflicts from string to numeric
merged_df['CURRENT_DESIGN_FLOW'] = pd.to_numeric(merged_df['CURRENT_DESIGN_FLOW'], errors='coerce')
merged_df['PRESENT_DISCHARGE_PERCENTAGE'] = pd.to_numeric(merged_df['PRESENT_DISCHARGE_PERCENTAGE'], errors='coerce')
#print(merged_df['DISCHARGE_TYPE'].unique())

#Applying the formula
merged_df['Reuse_Volume'] = merged_df['CURRENT_DESIGN_FLOW'] * (merged_df['PRESENT_DISCHARGE_PERCENTAGE'] / 100)
#print(merged_df[['CURRENT_DESIGN_FLOW', 'PRESENT_DISCHARGE_PERCENTAGE', 'Reuse_Volume']].describe())
print(merged_df[['CURRENT_DESIGN_FLOW', 'PRESENT_DISCHARGE_PERCENTAGE', 'Reuse_Volume']])
#print(merged_df['DISCHARGE_TYPE'].unique())

merged_df.to_csv('water_data.csv', index=False)

# Group by the existing labels and sum the volume 
#final_summary = merged_df.groupby('DISCHARGE_TYPE')['Reuse_Volume'].sum().reset_index()

# Sort by volume so the biggest categories are at the top
#final_summary = final_summary.sort_values(by='Reuse_Volume', ascending=False)
#print(final_summary)

# Create a 'Total' row
#total_row = pd.DataFrame({
    #'DISCHARGE_TYPE': ['Total'], 
   # 'Reuse_Volume': [final_summary['Reuse_Volume'].sum()]})

# Append the total row to the bottom
#final_summary = pd.concat([final_summary, total_row], ignore_index=True)
#print(final_summary)

# Save to the same folder as your script
#final_summary.to_csv('cleaned.csv', index=False)