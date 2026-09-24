# E-Commerce Web Scraping & Data Cleaning Pipeline

**Goal:** To automate the extraction of competitor pricing data and clean it for immediate business analysis.

Businesses lose countless hours manually copying and pasting competitor prices into Excel. This project demonstrates an automated Python pipeline that extracts live web data, strips away messy formatting, and outputs a clean, analysis-ready dataset. 

## The Automation Process
1. **Data Extraction:** Utilized `BeautifulSoup` and `requests` to parse HTML and systematically extract product names, raw prices, and inventory status.
2. **Data Transformation:** Leveraged `pandas` to remove non-numeric characters (currency symbols) and convert string data into functional floats.
3. **Data Structuring:** Applied business logic to filter out out-of-stock items and exported the final structured dataset to a `.csv` file, ready for import into Excel or Tableau.

## Technologies Used
* **Python** 
* **Web Scraping:** BeautifulSoup4, Requests
* **Data Cleaning:** Pandas
