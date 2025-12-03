# Fortune Global 500 Scraper

Scrapes **Fortune Global 500** [(link)](https://fortune.com/ranking/global500/) company data for analysis and research.

This project allows you to:

- Collect company data from multiple years (e.g., 2022–2024).  
- Filter companies that appear consistently across years.  
- Save the cleaned data to CSV for further analysis.  
- Explore the website’s HTML structure to understand how data is extracted.  

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from fortune_scraper import scrape_fortune_global, filter_consistent_companies

# Scrape data for multiple years
years = [2024, 2023, 2022]
df = scrape_fortune_global(years)

# Keep only companies in all years
df_filtered = filter_consistent_companies(df)

# Save to CSV
df_filtered.to_csv('fortune500_data.csv', index=False)
```

## Data Fields

- Company Name
- Country
- Industry
- Year
- Fortune global 500 ranking
- Revenue (USD Millions)
- Profits (USD Millions)
- Assets (USD Millions)
- Employees

```
