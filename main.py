#Name: Alyssia
#Date: 11-16-25
#Assignment: Lab 10


import pandas as pd
import matplotlib.pyplot as plt
import video_games
games = video_games.get_video_game()

titles = []
scores = []

# Loop through the list of game dictionaries
for game in games:
    title = game['Title']
    score = game['Metrics']['Review Score']
    
    titles.append(title)
    scores.append(score)

# Step 3 — Create DataFrame
df = pd.DataFrame({
    'Title': titles,
    'Review Score': scores
})

print("Raw Data:")
print(df.head())

# Step 4 — Clean the Data
df_clean = df[df['Review Score'] > 0]   # Remove zeros
df_clean = df_clean.sort_values(by='Review Score', ascending=False)

print("\nCleaned Data:")
print(df_clean.head())

# Step 5 — Plot: Top 20 Games
plt.figure(figsize=(12, 8))
plt.barh(df_clean['Title'].head(20), df_clean['Review Score'].head(20))
plt.xlabel('Review Score')
plt.title('Top 20 Video Games by Review Score')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top20_review_scores.png")   # <-- Saves image
plt.close()


# Plot: Distribution of All Scores
plt.figure(figsize=(10, 6))
plt.scatter(df_clean['Review Score'], range(len(df_clean)), alpha=0.6)
plt.xlabel('Review Score')
plt.ylabel('Game Index')
plt.title('Distribution of Video Game Review Scores')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig("review_score_distribution.png")  # <-- Saves image
plt.close()
