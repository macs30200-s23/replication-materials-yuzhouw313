# Analysis of Twitter Sinophobic Sentiment and Real-Life Hate Crimes Against the Chinese and Asian Population

## Introduction
The code and data in this repository is used to answer the research question “Is there any relationship between anti-Chinese public sentiment 
expressed on social media and real-life crimes against the Chinese population during the COVID-19 pandemic?”

Jacobs and van Spanje argue that research into the contextual-level factors driving hate crimes is scant and evidence about their origin from a broad societal perspective remains largely anecdotal (2021, p. 170). In this study, I aim to analyze the relationship, such as correlational, predictionary, and causal, between online anti-Chinese sentiment and real-life anti-Chinese crimes.

Below are four hypotheses: 
H1: Online anti-Chinese hate sentiment will be predictive of anti-Chinese offline hate crime incidents in the United States.
H2: Offline anti-Chinese hate sentiment will be predictive of anti-Chinese online hate crime incidents in the United States.
H3: Online anti-Chinese hate sentiment will be causal of anti-Chinese offline hate crime incidents in the United States.
H4: Offline anti-Chinese hate sentiment will be causal of anti-Chinese online hate crime incidents in the United States.


## Dependencies
The libraries required to replicate this analysis can be found in requirements.txt [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/requirements.txt)

```python
conda create -n <environment-name> --file requirements.txt
```


## Dataset
- Twitter dataset is collected using snsscrape created by Martin Beck [here](https://github.com/MartinKBeck/TwitterScraper/tree/master/snscrape)
- FBI Hate Crime Statistical Dataset is obtained directly from FBI's Crime Data Explorer [here](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/hate-crime).

### Twitter Data
Specifically, all tweets are filtered by the keyword list of Sinophobia sentiment heavy words found by Shen and colleagues (2022, p. 947), their research article can be found [here](https://ojs.aaai.org/index.php/ICWSM/article/view/19348).

I chose the top 5 most frequently occurring words towards combined hateful weight vectors, which are "chink," "chinaman," "chyna," "chinkland," and "gook." They represent the traditional racial slurs againt the Chinese population and China.

The dataset consists of total 303989 tweets collected via Twitter from 2020/1/1 to 2020/12/31. The original data can be found [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/tree/main/twitter%20data) and the code to scrape the data can be found [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/scrape.ipynb)

An example of the Twitter DataFrame looks like this
| Datetime                   | Tweet Id             | Username       | Text                                             | 
| --------                   | --------             | --------       | --------                                         |
| 2020-01-08 23:54:31+00:00  | 1215059236725706757  | ItsEstaFiesta  | Meghan Markle did what y’all though Blac Chyna...| 



### FBI Data
The original FBI Hate Crime Statistical Dataset csv file can be found [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/FBI_hatecrime/hate_crime.csv) which ranges from 1991 to 2021. However, I will preprocess the dataset and convert it into a DataFrame which contains all anti-Asian hate crimes from the year 2020

An example of FBI data looks like this: ![alt text](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/Screenshot%202023-04-16%20at%2020.24.44.png)


## Preliminary Results



## References:
Jacobs, L., & van Spanje, J. (2021). A Time-Series Analysis of Contextual-Level Effects on Hate Crime in The Netherlands. Social Forces, 100(1), 169–193. https://doi.org/10.1093/sf/soaa102

MartinKBeck. (2021). snscrape: A Social Networking Service scraper in Python. GitHub repository. Retrieved Month Day, Year, from https://github.com/MartinKBeck/TwitterScraper/tree/master/snscrape

Shen, X., He, X., Backes, M., Blackburn, J., Zannettou, S., & Zhang, Y. (2022). On Xing Tian and the Perseverance of Anti-China Sentiment Online. Proceedings of the International AAAI Conference on Web and Social Media, 16, 944–955. https://doi.org/10.1609/icwsm.v16i1.19348
