import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

# Function to get integer from object

def money_to_float(val):
    """
    Convert a money string like "$21,344" into a float 21344.0.
    Returns None if the input is empty or None.
    """
    if not val:
        return None
    return float(val.replace("$","").replace(",",""))

# Function to get data for one or more years
def scrape_fortune_global(years):
    """
    Scrape Fortune Global 500 for one or more years.
    Fetches the page(s), extracts JSON from <script id="__NEXT_DATA__">,
    and returns a combined DataFrame with company details.
    """
    all_data = []

    for year in years:
        url = f"https://fortune.com/ranking/global500/{year}/"
        resp = requests.get(url)

        soup = BeautifulSoup(resp.content, "html.parser")

        script_tag = soup.select_one("#__NEXT_DATA__")

        page_data = json.loads(script_tag.string)
        page_props = page_data.get("props", {}).get("pageProps", {})
        franchise_search = page_props.get("franchiseSearch", {})
        items = franchise_search.get("items", [])

        for c in items:
            d = c.get("data", {})
            all_data.append({
                "Company": c.get("name"),
                "Country": d.get("Country / Territory"),
                "Industry": d.get("Industry"),
                "Year": year,
                "Rank": c.get("rank"),
                "Revenue": money_to_float(d.get("Revenues ($M)")),
                "Profits": money_to_float(d.get("Profits ($M)")),
                "Assets": money_to_float(d.get("Assets ($M)")),
                "Employees": int(d.get("Employees", "0").replace(",", ""))
            })

    return pd.DataFrame(all_data)

def filter_consistent_companies(df):
    """
    Keep only companies that appear in all years.
    """
    company_year_counts = df.groupby("Company")["Year"].nunique()
    n_years = df["Year"].nunique()
    common_companies = company_year_counts[company_year_counts == n_years].index
    
    return df[df["Company"].isin(common_companies)]

# Example usage
years = [2024, 2023, 2022]
fortune_df = scrape_fortune_global(years)
  
print(f"Total records: {fortune_df.shape}")
print(fortune_df.head())
    
# Filter to companies in all years
fortune_df_all_years = filter_consistent_companies(fortune_df)
print(f"\nConsistent companies: {fortune_df_all_years['Company'].nunique()}")
print(f"Filtered records: {fortune_df_all_years.shape}")


fortune_df_all_years.to_csv('fortune500_data.csv', index=False)


