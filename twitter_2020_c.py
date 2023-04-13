import snscrape.modules.twitter as sntwitter
import pandas as pd

maxTweets = 1000
attr_col = ['Datetime', 'Tweet Id', 'Text', 'Username']

def scrape_by_month(target, output):
    ''' 
    Function to web scrape all one month of tweets containing word C
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


scrape_by_month('chyna since:2020-01-01 until:2020-01-31', 'Cjan2020-tweets.csv')
scrape_by_month('chyna since:2020-02-01 until:2020-02-29', 'Cfeb2020-tweets.csv')
scrape_by_month('chyna since:2020-03-01 until:2020-03-31', 'Cmar2020-tweets.csv')
scrape_by_month('chyna since:2020-04-01 until:2020-04-30', 'Capr2020-tweets.csv')
scrape_by_month('chyna since:2020-05-01 until:2020-05-31', 'Cmay2020-tweets.csv')
scrape_by_month('chyna since:2020-06-01 until:2020-06-30', 'Cjun2020-tweets.csv')
scrape_by_month('chyna since:2020-07-01 until:2020-07-31', 'Cjul2020-tweets.csv')
scrape_by_month('chyna since:2020-08-01 until:2020-08-31', 'Caug2020-tweets.csv')
scrape_by_month('chyna since:2020-09-01 until:2020-09-30', 'Csep2020-tweets.csv')
scrape_by_month('chyna since:2020-10-01 until:2020-10-31', 'Coct2020-tweets.csv')
scrape_by_month('chyna since:2020-11-01 until:2020-11-30', 'Cnov2020-tweets.csv')
scrape_by_month('chyna since:2020-12-01 until:2020-12-31', 'Cdec2020-tweets.csv')