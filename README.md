The code and data in this repository is used to answer the research question “Is there any relationship between anti-Chinese public sentiment 
expressed on social media and real-life crimes against the Chinese population during the COVID-19 pandemic?”

Below are four hypotheses: 
H1: Online anti-Chinese hate sentiment will be predictive of anti-Chinese offline hate crime incidents in the United States.
H2: Offline anti-Chinese hate sentiment will be predictive of anti-Chinese online hate crime incidents in the United States.
H3: Online anti-Chinese hate sentiment will be causal of anti-Chinese offline hate crime incidents in the United States.
H4: Offline anti-Chinese hate sentiment will be causal of anti-Chinese online hate crime incidents in the United States.


## Dataset
Data are collected using snsscrape created by Martin Beck

Tweets are collected by the keyword list of Sinophobia sentiment heavy words found by Shen et al., their research article can be found [here](https://ojs.aaai.org/index.php/ICWSM/article/view/19348).

I chose the top 5 most frequently occurring words towards combined hateful weight vectors, which are "chink," "chinaman," "chyna," "chinkland," and "gook." They represent the traditional racial slurs againt the Chinese population and China.

Additionally, I also chose the 2 often related to Sinophobiac sentiment triggered by COVID-19 -- "wuhanvirus and chinesevirus." They are newly emerged racial slurs direcly related to the coronavirus pandemic.

MartinKBeck. (2021). snscrape: A Social Networking Service scraper in Python. GitHub repository. Retrieved Month Day, Year, from https://github.com/MartinKBeck/TwitterScraper/tree/master/snscrape


- twitter_a.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_a.py): Web scrape code to obtain the tweets containing keywords of word A in 2020 and 2021

- twitter_b.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_b.py): Web scrape code to obtain the tweets containing keywords of word B in 2020 and 2021

- twitter_c.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_c.py): Web scrape code to obtain the tweets containing keywords of word C in 2020 and 2021

- twitter_d.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_d.py): Web scrape code to obtain the tweets containing keywords of word D in 2020 and 2021

- twitter_e.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_e.py): Web scrape code to obtain the tweets containing keywords of word E in 2020 and 2021

- twitter_f.py [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_f.py): Web scrape code to obtain the tweets containing keywords of word F in 2020 and 2021

