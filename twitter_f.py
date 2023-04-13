import snscrape.modules.twitter as sntwitter
import pandas as pd

maxTweets = 2000
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


scrape_by_month('chinesevirus since:2020-01-01 until:2020-01-31', 'Fjan2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-02-01 until:2020-02-29', 'Ffeb2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-03-01 until:2020-03-31', 'Fmar2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-04-01 until:2020-04-30', 'Fapr2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-05-01 until:2020-05-31', 'Fmay2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-06-01 until:2020-06-30', 'Fjun2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-07-01 until:2020-07-31', 'Fjul2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-08-01 until:2020-08-31', 'Faug2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-09-01 until:2020-09-30', 'Fsep2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-10-01 until:2020-10-31', 'Foct2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-11-01 until:2020-11-30', 'Fnov2020-tweets.csv')
scrape_by_month('chinesevirus since:2020-12-01 until:2020-12-31', 'Fdec2020-tweets.csv')

scrape_by_month('chinesevirus since:2021-01-01 until:2021-01-31', 'Fjan2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-02-01 until:2021-02-28', 'Ffeb2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-03-01 until:2021-03-31', 'Fmar2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-04-01 until:2021-04-30', 'Fapr2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-05-01 until:2021-05-31', 'Fmay2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-06-01 until:2021-06-30', 'Fjun2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-07-01 until:2021-07-31', 'Fjul2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-08-01 until:2021-08-31', 'Faug2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-09-01 until:2021-09-30', 'Fsep2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-10-01 until:2021-10-31', 'Foct2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-11-01 until:2021-11-30', 'Fnov2021-tweets.csv')
scrape_by_month('chinesevirus since:2021-12-01 until:2021-12-31', 'Fdec2021-tweets.csv')
