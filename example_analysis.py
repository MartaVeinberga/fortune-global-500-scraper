import matplotlib.pyplot as plt
from fortune_scraper import scrape_fortune_global, filter_consistent_companies

# Scrape data
years = [2024, 2023, 2022]
df = scrape_fortune_global(years)
df_filtered = filter_consistent_companies(df)

# Analyze 2024 data
df_2024 = df_filtered[df_filtered['Year'] == 2024]
top_countries = df_2024['Country'].value_counts().head(15).sort_values()

# Plot
plt.figure(figsize=(10, 6))
bars = plt.barh(top_countries.index, top_countries.values, color='#2E86AB')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.5, bar.get_y() + bar.get_height()/2, 
             str(int(width)), va='center', fontsize=10)

plt.title("Top 15 Countries in Fortune Global 500 (2024)", fontsize=14, fontweight='bold')
plt.xlabel("Number of Companies")
plt.tight_layout()
plt.show()