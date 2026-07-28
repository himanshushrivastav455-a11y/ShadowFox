import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime
import logging

logging.basicConfig(filename="scraper.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

BASE_URL="https://books.toscrape.com/catalogue/page-{}.html"
HEADERS={"User-Agent":"Mozilla/5.0"}

def scrape(pages=3):
    books=[]
    for page in range(1,pages+1):
        url=BASE_URL.format(page)
        print(f"Scraping Page {page}...")
        try:
            r=requests.get(url,headers=HEADERS,timeout=10)
            r.raise_for_status()
            soup=BeautifulSoup(r.text,"lxml")
            for b in soup.select("article.product_pod"):
                books.append({
                    "Title":b.h3.a["title"],
                    "Price":b.select_one(".price_color").text,
                    "Availability":b.select_one(".instock.availability").get_text(strip=True),
                    "Rating":b.p["class"][1],
                    "ScrapedAt":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
        except Exception as e:
            logging.error(f"{url}: {e}")
    return pd.DataFrame(books)

def save(df):
    df.to_csv("data/books.csv",index=False)
    df.to_json("data/books.json",orient="records",indent=4)
    conn=sqlite3.connect("data/books.db")
    df.to_sql("books",conn,if_exists="replace",index=False)
    conn.close()

if __name__=="__main__":
    try:
        pages=int(input("Enter number of pages to scrape (1-50): "))
    except:
        pages=3
    df=scrape(pages)
    save(df)
    print(df.head())
    print(f"\nTotal Books Scraped: {len(df)}")
    print("Saved to CSV, JSON and SQLite.")
