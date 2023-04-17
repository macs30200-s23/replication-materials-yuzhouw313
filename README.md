The code and data in this repository is used to answer the research question “Is there any relationship between anti-Chinese public sentiment 
expressed on social media and real-life crimes against the Chinese population during the COVID-19 pandemic?”

Research into the contextual-level factors driving hate crimes is scant and evidence about their origin from a broad societal perspective remains largely anecdotal

Below are four hypotheses: 
H1: Online anti-Chinese hate sentiment will be predictive of anti-Chinese offline hate crime incidents in the United States.
H2: Offline anti-Chinese hate sentiment will be predictive of anti-Chinese online hate crime incidents in the United States.
H3: Online anti-Chinese hate sentiment will be causal of anti-Chinese offline hate crime incidents in the United States.
H4: Offline anti-Chinese hate sentiment will be causal of anti-Chinese online hate crime incidents in the United States.


## Dataset
Twitter data are collected using snsscrape created by Martin Beck.

Specifically, all tweets are collected by the keyword list of Sinophobia sentiment heavy words found by Shen et al., their research article can be found [here](https://ojs.aaai.org/index.php/ICWSM/article/view/19348).

I chose the top 4 most frequently occurring words towards combined hateful weight vectors, which are "chink," "chinaman," "chyna," "chinkland." They represent the traditional racial slurs againt the Chinese population and China.

Additionally, I also chose the 2 often related to Sinophobiac sentiment triggered by COVID-19 -- "wuhanvirus and chinesevirus." They are newly emerged racial slurs direcly related to the coronavirus pandemic.

MartinKBeck. (2021). snscrape: A Social Networking Service scraper in Python. GitHub repository. Retrieved Month Day, Year, from https://github.com/MartinKBeck/TwitterScraper/tree/master/snscrape


## Files and Folders
- Tweets containing word A from 1/1/2020 to 12/31/2021
    - twitter_a.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_a.py): Web scrape code to obtain the tweets
    - tweet-part-A [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/tree/main/tweet-part-A): Data folder of all A related tweets

- Tweets containing word B from 1/1/2020 to 12/31/2021
    - twitter_a.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_a.py): Web scrape code to obtain the tweets
    - tweet-part-B [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/tree/main/tweet-part-B): Data folder of all B related tweets

- Tweets containing word C from 1/1/2020 to 12/31/2021
    - twitter_c.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_c.py): Web scrape code to obtain the tweets
    - tweet-part-C [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/tree/main/tweet-part-C): Data folder of all C related tweets

- Tweets containing word D from 1/1/2020 to 12/31/2021
    - twitter_d.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_d.py): Web scrape code to obtain the tweets
    - tweet-part-D [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/tree/main/tweet-part-D): Data folder of all D related tweets

- Tweets containing word E from 1/1/2020 to 12/31/2021
    - twitter_e.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_e.py): Web scrape code to obtain the tweets
    - tweet-part-E [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/tree/main/tweet-part-E): Data folder of all E related tweets

- Tweets containing word F from 1/1/2020 to 12/31/2021
    - twitter_f.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_f.py): Web scrape code to obtain the tweets
    - tweet-part-F [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/tree/main/tweet-part-F): Data folder of all F related tweets


References:
Jacobs, L., & van Spanje, J. (2021). A Time-Series Analysis of Contextual-Level Effects on Hate Crime in The Netherlands. Social Forces, 100(1), 169–193. https://doi.org/10.1093/sf/soaa102