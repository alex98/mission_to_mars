

from bs4 import BeautifulSoup 
from splinter import Browser
from selenium import webdriver 
import pandas as pd
from IPython import get_ipython





get_ipython().system('C:\\Users\\alexc\\Documents\\USCLOS201811DATA3\\12_web_scraping_and_document_databases\\homework\\chromedriver_win32')





#
executable_path = {'executable_path': 'C:/Users/alexc/Anaconda3/envs/pythondata/chromedriver'}




browser = Browser('chrome', **executable_path)


mars_news_url = 'https://mars.nasa.gov/news/'


browser.visit(mars_news_url)
raw_html_news = browser.html


soup_news = BeautifulSoup(raw_html_news, 'lxml')


browser.quit()




listTextLabelElem = news_soup.find('div', class_='content_title')
print(listTextLabelElem)




news_title = listTextLabelElem.find('a').get_text()
print(news_title)





title = soup_news.find('div', class_='content_title').get_text()
news = soup_news.find('div', class_='article_teaser_body').get_text()

print(title)
print(news)





browser = Browser("chrome", **executable_path, headless=False)


jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)
raw_html_image = browser.html
soup_image = BeautifulSoup(raw_html_image, 'lxml')
browser.quit()


featured_image = soup_image.find('a', class_='fancybox')
featured_image_url = "https://www.jpl.nasa.gov/" + featured_image["data-fancybox-href"]

print(featured_image_url)






browser = Browser("chrome", **executable_path, headless=False)


weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)
raw_html_twitter = browser.html
soup_twitter = BeautifulSoup(raw_html_twitter, 'lxml')
browser.quit()


weather = soup_twitter.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()

weather






mars_facts_df = pd.read_html('https://space-facts.com/mars/')
mars_facts = str(mars_facts_df[0].to_html(index=False, header=False, border="0"))

mars_facts






browser = Browser("chrome", **executable_path, headless=False)


hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemisphere_url)
raw_html_hemispheres = browser.html
soup_hemispheres = BeautifulSoup(raw_html_hemispheres, 'lxml')

hemispheres = soup_hemispheres.findAll('div', class_='description')
browser.quit()

hemispheres





hemisphere_links = []
for sphere in hemispheres:
    hemisphere_links.append('https://astrogeology.usgs.gov' + sphere.find('a')["href"])

hemisphere_links






import re
hemisphere_image_urls = []

for link in hemisphere_links:
    browser = Browser("chrome", **executable_path, headless=False)
    browser.visit(link)
    html_h = browser.html
    soup_h = BeautifulSoup(html_h, 'lxml')
    temp_h = soup_h.find("div", class_="content") 
    #print(temp_h)
    hemisphere_image_urls.append({
            "title" : temp_h.find('h2').get_text(),
            "img_url" : temp_h.find('a', href=re.compile('^http://astropedia.astrogeology.usgs.gov/download/Mars/Viking'))["href"]
        })
    browser.quit()

hemisphere_image_urls





