import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_ecommerce_data():
    """Scrapes raw product data from the target website."""
    url = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = []
    # Find all product containers on the page
    for item in soup.find_all('article', class_='product_pod'):
        title = item.h3.a['title']
        raw_price = item.find('p', class_='price_color').text
        availability = item.find('p', class_='instock availability').text.strip()
        
        products.append({
            'Product_Name': title,
            'Raw_Price': raw_price,
            'Status': availability
        })
        
    return pd.DataFrame(products)

def clean_data(df):
    """Cleans and formats the raw data for business use."""
    # Remove the currency symbol (£) and convert to float for calculations
    df['Clean_Price_USD'] = df['Raw_Price'].str.replace('£', '').astype(float)
    
    # Drop the old messy column
    df = df.drop(columns=['Raw_Price'])
    
    # Filter out anything that isn't in stock (simulating a business rule)
    df = df[df['Status'] == 'In stock']
    
    return df

if __name__ == "__main__":
    print("Initializing extraction pipeline...")
    raw_data = scrape_ecommerce_data()
    
    print("Cleaning and formatting data...")
    clean_dataframe = clean_data(raw_data)
    
    # Export the pristine data to a CSV file
    clean_dataframe.to_csv('clean_product_data.csv', index=False)
    print("Pipeline complete. Clean data exported to 'clean_product_data.csv'.")
