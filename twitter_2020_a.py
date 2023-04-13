import snscrape.modules.twitter as sntwitter
import pandas as pd

# Query by text search
maxTweets = 1000
attr_col = ['Datetime', 'Tweet Id', 'Text', 'Username']



def scrape_by_month(target, output):
    lst = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(target).get_items()):
        if i>maxTweets:
            break
        lst.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

    df = pd.DataFrame(lst, columns=attr_col)
    df.to_csv(output, sep=',', index=False)

    return


scrape_by_month('chink since:2020-01-01 until:2020-01-31', 'jan2020-tweets.csv')
scrape_by_month('chink since:2020-02-01 until:2020-02-29', 'feb2020-tweets.csv')
scrape_by_month('chink since:2020-03-01 until:2020-03-31', 'mar2020-tweets.csv')
scrape_by_month('chink since:2020-04-01 until:2020-04-30', 'apr2020-tweets.csv')
scrape_by_month('chink since:2020-05-01 until:2020-05-31', 'may2020-tweets.csv')
scrape_by_month('chink since:2020-06-01 until:2020-06-30', 'jun2020-tweets.csv')
scrape_by_month('chink since:2020-07-01 until:2020-07-31', 'jul2020-tweets.csv')
scrape_by_month('chink since:2020-08-01 until:2020-08-31', 'aug2020-tweets.csv')
scrape_by_month('chink since:2020-09-01 until:2020-09-30', 'sep2020-tweets.csv')
scrape_by_month('chink since:2020-10-01 until:2020-10-31', 'oct2020-tweets.csv')
scrape_by_month('chink since:2020-11-01 until:2020-11-30', 'nov2020-tweets.csv')
scrape_by_month('chink since:2020-12-01 until:2020-12-31', 'dec2020-tweets.csv')

