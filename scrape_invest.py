from splinter import Browser, browser
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup as soup
import pandas as pd 
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Setup Splinter
    executable_path = {"executable_path" : ChromeDriverManager().install()} 
    browser = Browser("chrome", **executable_path, headless=False) 
    # Investing Website URL
    url = "https://www.investing.com" 
    browser.visit(url)

    time.sleep(1)
    # Scrape page into soup
    html = browser.html
    index_soup = soup(html,"html.parser")

    # Get latest price and return for S&P, Gold & U.S. 10Y
    # S&P price and daily return
    index_snp = index_soup.find_all("div", class_="quotesBarContentCellTop")[0].get_text()
    price_snp = index_soup.find_all("div", class_="quotesBarContentCellBottom")[0].get_text()

    # Gold price and daily return
    index_gold = index_soup.find_all("div", class_="quotesBarContentCellTop")[2].get_text()
    price_gold = index_soup.find_all("div", class_="quotesBarContentCellBottom")[2].get_text()

    # U.S. 10Y bond price and daily return
    index_usb = index_soup.find_all("div", class_="quotesBarContentCellTop")[6].get_text()
    price_usb = index_soup.find_all("div", class_="quotesBarContentCellBottom")[6].get_text()

    # Setting URL for Crypto 
    url = "https://www.investing.com/crypto/" 
    browser.visit(url)

    time.sleep(1)

    # Scrape page into soup
    html = browser.html
    crypto_soup = soup(html,"html.parser")

    # Get latest prices for Bitcoin and Ethereum
    # Bitcoin price and daily retun
    index_bit = crypto_soup.find_all("td", class_="left bold elp name cryptoName first js-currency-name")[0].get_text()
    price_bit = crypto_soup.find_all("td", class_="price js-currency-price")[0].get_text()
    

    # Ethereum price and daily return
    index_ete = crypto_soup.find_all("td", class_="left bold elp name cryptoName first js-currency-name")[1].get_text()
    price_ete = crypto_soup.find_all("td", class_="price js-currency-price")[1].get_text()

# Close browser after scrapping
    browser.quit()

    investing_data= {
        "snp" : index_snp,
        "snp_price" : price_snp,
        "gold" : index_gold,
        "gold_price" : price_gold,
        "usb" : index_usb,
        "usb_price" : price_usb,
        "bitcoin" : index_bit,
        "bit_price" : price_bit,
        "ethereum" : index_ete,
        "ete_price" : price_ete,
    }
    print(investing_data)
    # Return results
    return investing_data