import snscrape.modules.twitter as sntwitter
import pandas as pd

maxTweets = 1000
attr_col = ['Datetime', 'Tweet Id', 'Text', 'Username']

def scrape_by_month(target, output):
    ''' 
    Function to web scrape all one month of tweets containing word B
    Input:
        target(str): The command to webscrape including keyword and date bound
        output(str): The output csv file name
    '''

    lst = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(target).get_items()):
        if i > maxTweets:
            break
        lst.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

    df = pd.DataFrame(lst, columns=attr_col)
    df.to_csv(output, sep=',', index=False)


scrape_by_month('chinaman since:2020-01-01 until:2020-01-31', 'Bjan2020-tweets.csv')
scrape_by_month('chinaman since:2020-02-01 until:2020-02-29', 'Bfeb2020-tweets.csv')
scrape_by_month('chinaman since:2020-03-01 until:2020-03-31', 'Bmar2020-tweets.csv')
scrape_by_month('chinaman since:2020-04-01 until:2020-04-30', 'Bapr2020-tweets.csv')
scrape_by_month('chinaman since:2020-05-01 until:2020-05-31', 'Bmay2020-tweets.csv')
scrape_by_month('chinaman since:2020-06-01 until:2020-06-30', 'Bjun2020-tweets.csv')
scrape_by_month('chinaman since:2020-07-01 until:2020-07-31', 'Bjul2020-tweets.csv')
scrape_by_month('chinaman since:2020-08-01 until:2020-08-31', 'Baug2020-tweets.csv')
scrape_by_month('chinaman since:2020-09-01 until:2020-09-30', 'Bsep2020-tweets.csv')
scrape_by_month('chinaman since:2020-10-01 until:2020-10-31', 'Boct2020-tweets.csv')
scrape_by_month('chinaman since:2020-11-01 until:2020-11-30', 'Bnov2020-tweets.csv')
scrape_by_month('chinaman since:2020-12-01 until:2020-12-31', 'Bdec2020-tweets.csv')

scrape_by_month('chinaman since:2021-01-01 until:2021-01-31', 'Bjan2021-tweets.csv')
scrape_by_month('chinaman since:2021-02-01 until:2021-02-28', 'Bfeb2021-tweets.csv')
scrape_by_month('chinaman since:2021-03-01 until:2021-03-31', 'Bmar2021-tweets.csv')
scrape_by_month('chinaman since:2021-04-01 until:2021-04-30', 'Bapr2021-tweets.csv')
scrape_by_month('chinaman since:2021-05-01 until:2021-05-31', 'Bmay2021-tweets.csv')
scrape_by_month('chinaman since:2021-06-01 until:2021-06-30', 'Bjun2021-tweets.csv')
scrape_by_month('chinaman since:2021-07-01 until:2021-07-31', 'Bjul2021-tweets.csv')
scrape_by_month('chinaman since:2021-08-01 until:2021-08-31', 'Baug2021-tweets.csv')
scrape_by_month('chinaman since:2021-09-01 until:2021-09-30', 'Bsep2021-tweets.csv')
scrape_by_month('chinaman since:2021-10-01 until:2021-10-31', 'Boct2021-tweets.csv')
scrape_by_month('chinaman since:2021-11-01 until:2021-11-30', 'Bnov2021-tweets.csv')
scrape_by_month('chinaman since:2021-12-01 until:2021-12-31', 'Bdec2021-tweets.csv')