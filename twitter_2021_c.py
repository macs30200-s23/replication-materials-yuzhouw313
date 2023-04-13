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


scrape_by_month('chyna since:2021-01-01 until:2021-01-31', 'Cjan2021-tweets.csv')
scrape_by_month('chyna since:2021-02-01 until:2021-02-28', 'Cfeb2021-tweets.csv')
scrape_by_month('chyna since:2021-03-01 until:2021-03-31', 'Cmar2021-tweets.csv')
scrape_by_month('chyna since:2021-04-01 until:2021-04-30', 'Capr2021-tweets.csv')
scrape_by_month('chyna since:2021-05-01 until:2021-05-31', 'Cmay2021-tweets.csv')
scrape_by_month('chyna since:2021-06-01 until:2021-06-30', 'Cjun2021-tweets.csv')
scrape_by_month('chyna since:2021-07-01 until:2021-07-31', 'Cjul2021-tweets.csv')
scrape_by_month('chyna since:2021-08-01 until:2021-08-31', 'Caug2021-tweets.csv')
scrape_by_month('chyna since:2021-09-01 until:2021-09-30', 'Csep2021-tweets.csv')
scrape_by_month('chyna since:2021-10-01 until:2021-10-31', 'Coct2021-tweets.csv')
scrape_by_month('chyna since:2021-11-01 until:2021-11-30', 'Cnov2021-tweets.csv')
scrape_by_month('chyna since:2021-12-01 until:2021-12-31', 'Cdec2021-tweets.csv')