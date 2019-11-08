from bs4 import BeautifulSoup
import requests
import csv

# =============================================================================
# make sure to 
# * pip install bs4 *
# before you proceeeeeeeed
# =============================================================================


# =============================================================================
# This is literally the 'Hello World' for webscraping, atleast for me
# huge shoutout to Corey Schafer for making me understand this
# you should definitely watch this for better understanding 'https://www.youtube.com/watch?v=ng2o98k983k'
# =============================================================================


source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source,'lxml')

# =============================================================================
# this csv file will be created and saved in the cwd (current working directory)
# =============================================================================

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary','Video Link'])

for article in soup.find_all('article'):
    # print(article.prettify())

    headline = article.h2.a.text
    print('Headline: ',headline)

    summary = article.find('div', class_='entry-content').p.text
    print('\nSummary: ',summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        # print(vid_src)

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        # print(vid_id)

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    print("\nYoutube Link: ",yt_link)
    print('\n ................. \n')

    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()


# =============================================================================
# Also check out webscrapping_weather.py, which is somewhat similar
# =============================================================================
