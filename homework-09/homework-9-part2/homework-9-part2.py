# Generating auto-emails on China-related news from Google News

from bs4 import BeautifulSoup
import requests
import datetime
import re
import pandas as pd

response = requests.get("https://news.google.com/search?q=China&hl=en-US&gl=US&ceid=US%3Aen").content
soup = BeautifulSoup(response, "html.parser")

briefing = []

featured = soup.find(class_='lBwEZb BL5WZb xP6mwf').findAll('div',attrs={'jscontroller':'d0DtYd'})
for feature in featured:
    feature_row = {}
    feature_article = feature.find('article').find(class_='ZulkBc qNiaOd')
    feature_row['title'] = feature_article.span.text
    feature_row['url'] = 'https://news.google.com'+feature_article.a['href'][1:]
    feature_row['first_lines'] = feature_article.find(class_='HO8did Baotjf').text
    feature_row['source'] = feature.find(class_='QmrVtf kybdz').find('div',attrs={'class':'PNwZO zhsNkd'}).text
    feature_rawtime = feature.find('time')['datetime'].split(': ')[1]
    feature_row['time'] = datetime.datetime.fromtimestamp(int(feature_rawtime)).strftime('%Y-%m-%d %H:%M:%S')
    briefing.append(feature_row)

articles = soup.find(class_='lBwEZb BL5WZb xP6mwf').findAll('div',attrs={'jsmodel':'zT6vwb'})
for article in articles:
    article_row = {}
    article_row['title'] = article.find('a',attrs={'class':'ipQwMb Q7tWef'}).span.text
    article_row['url'] = 'https://news.google.com'+article.find('a',attrs={'class':'ipQwMb Q7tWef'})['href'][1:]
    article_row['first_lines'] = article.find('p').text
    article_row['source'] = article.find(class_='KbnJ8').text
    article_rawtime = re.findall(r'[\d]+', article.find('time')['datetime'].split(': ')[1])[0]
    article_row['time'] = datetime.datetime.fromtimestamp(int(article_rawtime)).strftime('%Y-%m-%d %H:%M:%S')
    briefing.append(article_row)
    
df = pd.DataFrame(briefing)
right_now = datetime.datetime.now()
date_string_filename = right_now.strftime("%Y-%b-%d_%-I%p")
df.to_csv('China_news_briefing_{}.csv'.format(date_string_filename), index=False)
date_string_mail = right_now.strftime("%-I %p")

requests.post(
        "https://api.mailgun.net/v3/MY_SANDBOX_DOMAIN/messages",
        auth=("api", "MY_API_KEY"),
        files=[("attachment", open('China_news_briefing_{}.csv'.format(date_string_filename)))],
        data={"from": "Edward Hong <mailgun@MY_SANDBOX_DOMAIN>",
              "to": ["Edward.YSHF@gmail.com"],
              "subject": "{} China News Briefing".format(date_string_mail),
              "text": "See attachment to learn what's new about China.",
              "html": '<html>Inline image here: <img src="cid:test.jpg"></html>'})