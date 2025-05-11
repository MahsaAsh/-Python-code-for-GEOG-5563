import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the folder path that contains the CSV files
folder_path = r"A:\Minnesota\Spring25\GroupProject5563\75sensors"

# Create a list to store results (sensor index and median PM2.5)
results = []

# Loop through each CSV file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)

            # Filter invalid or extreme values
            df = df[df['pm2.5_atm'].notna()]    # Remove missing values (NaN)
            df = df[df['pm2.5_atm'] > 0]        # Remove zero and negative values
            df = df[df['pm2.5_atm'] <= 500]     # Remove unrealistically high values

            # Use only sensors with at least 300 valid daily records
            if len(df) >= 300:
                median_pm25 = df['pm2.5_atm'].median()  # Calculate median
                sensor_index = int(filename.split('_')[1].replace('.csv', ''))  # Extract sensor index from filename
                results.append({'sensor_index': sensor_index, 'median_pm25': median_pm25})  # Save result

        except Exception as e:
            print(f"Error processing file {filename}: {e}")  # Print error if any file fails

# Convert results list into a DataFrame and save as CSV
output_df = pd.DataFrame(results)
output_df.to_csv(os.path.join(folder_path, "median_pm25_summary.csv"), index=False)

print("File created: median_pm25_summary.csv")


# ----------------------------
# Plot a histogram of the median PM2.5 values

# Load the summary CSV
df = pd.read_csv(r"A:\Minnesota\Spring25\GroupProject5563\75sensors\median_pm25_summary.csv")

# Plot histogram
plt.figure(figsize=(8,5))
plt.hist(df['median_pm25'], bins=15, edgecolor='black', color='skyblue')
plt.title("Distribution of Median PM2.5 (µg/m³) Across Sensors")
plt.xlabel("Median PM2.5 (µg/m³)")
plt.ylabel("Number of Sensors")
plt.grid(True)
plt.tight_layout()
plt.show()
