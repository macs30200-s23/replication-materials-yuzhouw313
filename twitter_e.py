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


scrape_by_month('wuhanvirus since:2020-01-01 until:2020-01-31', 'Ejan2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-02-01 until:2020-02-29', 'Efeb2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-03-01 until:2020-03-31', 'Emar2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-04-01 until:2020-04-30', 'Eapr2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-05-01 until:2020-05-31', 'Emay2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-06-01 until:2020-06-30', 'Ejun2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-07-01 until:2020-07-31', 'Ejul2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-08-01 until:2020-08-31', 'Eaug2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-09-01 until:2020-09-30', 'Esep2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-10-01 until:2020-10-31', 'Eoct2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-11-01 until:2020-11-30', 'Enov2020-tweets.csv')
scrape_by_month('wuhanvirus since:2020-12-01 until:2020-12-31', 'Edec2020-tweets.csv')

scrape_by_month('wuhanvirus since:2021-01-01 until:2021-01-31', 'Ejan2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-02-01 until:2021-02-28', 'Efeb2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-03-01 until:2021-03-31', 'Emar2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-04-01 until:2021-04-30', 'Eapr2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-05-01 until:2021-05-31', 'Emay2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-06-01 until:2021-06-30', 'Ejun2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-07-01 until:2021-07-31', 'Ejul2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-08-01 until:2021-08-31', 'Eaug2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-09-01 until:2021-09-30', 'Esep2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-10-01 until:2021-10-31', 'Eoct2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-11-01 until:2021-11-30', 'Enov2021-tweets.csv')
scrape_by_month('wuhanvirus since:2021-12-01 until:2021-12-31', 'Edec2021-tweets.csv')