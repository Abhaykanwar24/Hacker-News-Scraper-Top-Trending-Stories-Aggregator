
# Hacker News Scraper: Top Trending Stories Aggregator  

## 📌 Overview  
This project is a **web scraper for Hacker News**, built using Python with **BeautifulSoup** and **requests**. It fetches top articles from Hacker News, filters stories with **99+ votes**, and sorts them in descending order of votes. Users can specify how many pages to scrape (up to 20).  

## 🚀 Features  
- Scrapes multiple pages from [Hacker News](https://news.ycombinator.com/)  
- Extracts **title, link, and votes** for each story  
- Filters **only high-ranking stories (99+ votes)**  
- Sorts stories **by popularity** (highest votes first)  
- Provides user input to specify the number of pages to scrape  

## 🛠️ Technologies Used  
- Python  
- Requests  
- BeautifulSoup  
- PrettyPrint (pprint)  

## 📌 How to Run  
1. Install dependencies:  
   ```sh
   pip install requests beautifulsoup4
