# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load dataset
# file_path = r"D:\Python small codes_01\Song Popularity Analysis\songs.csv"  # Adjust to your actual path
# df = pd.read_csv(file_path)

# # Drop unnecessary columns
# df = df[['Track Name', 'Singer_Name', 'Track_Popularity', 'Playlist_Genre']]

# # Clean "Track_Popularity" column (remove '%' and convert to float)
# df["Track_Popularity"] = df["Track_Popularity"].str.replace("%", "").astype(float)

# # Check for missing values
# df = df.dropna(subset=['Track Name', 'Track_Popularity'])

# # Sorting top 15 songs by popularity
# top_15_songs = df.sort_values(by='Track_Popularity', ascending=False).head(15)

# # Visualization
# plt.figure(figsize=(12, 6))
# sns.barplot(x='Track_Popularity', y='Track Name', hue='Track Name', data=top_15_songs, palette='viridis', legend=False)
# plt.xlabel('Popularity')
# plt.ylabel('Song Name')
# plt.title('Top 15 Songs by Popularity')
# plt.show()

# # Save the cleaned and sorted dataset
# output_file = r"D:\Python small codes_01\Song Popularity Analysis\top_15_songs.csv"
# top_15_songs.to_csv(output_file, index=False)
# print(f'Top 15 songs saved to {output_file}')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "Song Popularity Analysis/songs.csv"  
df = pd.read_csv(file_path)

# Convert 'Track_Popularity' to numeric (if needed)
df['Track_Popularity'] = df['Track_Popularity'].str.replace('%', '').astype(float)

# Get top 15 songs by popularity
top_15_songs = df.sort_values(by='Track_Popularity', ascending=False).head(15)

# Set plot style
sns.set_style("darkgrid")
plt.figure(figsize=(12, 6))

# Create barplot with color gradient
colors = sns.color_palette("coolwarm", len(top_15_songs))
ax = sns.barplot(
    x="Track_Popularity", 
    y="Track Name", 
    data=top_15_songs, 
    palette=colors
)

# Add titles and labels
plt.xlabel("Popularity (%)", fontsize=12, fontweight="bold")
plt.ylabel("Song Name", fontsize=12, fontweight="bold")
plt.title("🎵 Top 15 Songs by Popularity 🎶", fontsize=14, fontweight="bold")

# Display popularity values on bars
for i, (value, name) in enumerate(zip(top_15_songs["Track_Popularity"], top_15_songs["Track Name"])):
    ax.text(value + 1, i, f"{value:.0f}%", color="black", va="center", fontsize=10, fontweight="bold")

plt.show()
