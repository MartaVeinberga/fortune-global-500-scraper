# Fortune Global 500 Scraper

A Python tool for scraping and analyzing **Fortune Global 500** company data across multiple years.

[![Fortune Global 500](https://img.shields.io/badge/Data%20Source-Fortune%20Global%20500-orange)](https://fortune.com/ranking/global500/)

## Features

- **Multi-year scraping** – Collect data from any year available on Fortune's website (1995 - 2024)
- **Consistency filtering** – Identify companies that appear across all selected years
- **Rich dataset** – Company, country, industry, year, rank, revenue, profits, assets, employees
- **Export to CSV** – Clean, analysis-ready data format
- **Example analysis** – Sample visualization

## Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Basic Usage
**Run directly:**
```bash
python fortune_scraper.py
```

**Or use as a Python module:**
```python
from fortune_scraper import scrape_fortune_global, filter_consistent_companies

# Scrape data for multiple years
years = [2024, 2023, 2022]
df = scrape_fortune_global(years)

# Filter for companies present in all years
df_filtered = filter_consistent_companies(df)

# Save to CSV
df_filtered.to_csv('fortune500_data.csv', index=False)
```

### Example Analysis

Run the included analysis script to see sample visualization:
```bash
python example_analysis.py
```

## Data Structure

The scraped dataset includes the following fields:

| Field | Description |
|-------|-------------|
| **Company Name** | Official company name |
| **Country** | Company headquarters location |
| **Industry** | Business sector classification |
| **Year** | Ranking year |
| **Rank** | Fortune Global 500 ranking position |
| **Revenue** | Total revenue (USD millions) |
| **Profits** | Net profits (USD millions) |
| **Assets** | Total assets (USD millions) |
| **Employees** | Total employee count |

## Files in This Repository
```
fortune-global-500-scraper/
├── fortune_scraper.py      # Main scraping module
├── fortune500_data.csv     # Pre-scraped dataset (2022-2024)
├── example_analysis.py     # Sample analysis and visualization
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

## Pre-scraped Data

Don't want to scrape? **`fortune500_data.csv`** contains ready-to-use data for 2022–2024, filtered for companies appearing in all three years.
```python
import pandas as pd

# Load pre-scraped data
df = pd.read_csv('fortune500_data.csv')
print(df.head())
```




