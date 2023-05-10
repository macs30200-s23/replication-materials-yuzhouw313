# Analysis of Twitter Sinophobic Sentiment and Real-Life Hate Crimes Against the Chinese and Asian Population

## Introduction
<b>Research Project:</b>
- From Tweets and Google searches to hate crimes: 
Analyzing the relationship between online Sinophobia and offline anti-Chinese violence during COVID-19

The code and data in this repository is used to answer the research question “How is Sinophobic sentiment expressed online during the COVID-19 pandemic related to incidents of real-life violence against the Chinese population?”

Jacobs and van Spanje argue that research into the contextual-level factors driving hate crimes is scant and evidence about their origin from a broad societal perspective remains largely anecdotal (2021, p. 170). In this study, I aim to analyze the relationship, such as correlational, predictionary, and causal, between online anti-Chinese sentiment and real-life anti-Chinese crimes.


## Dependencies
The libraries required to replicate this analysis can be found in requirements.txt [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/requirements.txt)

The code is written in Python 3.9.12 and all of its dependencies can be installed by running in the terminal:


```python
conda install -r requirements.txt
```


## Dataset
- Twitter dataset is collected using snsscrape created by Martin Beck [here](https://github.com/MartinKBeck/TwitterScraper/tree/master/snscrape)
- FBI Hate Crime Statistical Dataset is obtained directly from FBI's Crime Data Explorer [here](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/hate-crime).

### Twitter Data
- Proxy to capture the frequency and normalization of the use of Sinophobic words
- Tweets are filtered by Sinophobic keywords found and used by [Shen and colleagues (2022, p. 947)](https://ojs.aaai.org/index.php/ICWSM/article/view/19348)
- I chose the top 5 most frequently occurring words towards combined hateful weight vectors, which are "chink," "chinaman," "chyna," "chinkland," and "gook." They represent the traditional racial slurs againt the Chinese population and China.
- The dataset consists of total <i>303989</i> tweets collected via Twitter from 2020/1/1 to 2020/12/31. The original data can be found [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/tree/main/twitter%20data) and the code to scrape the data can be found [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/scrape.ipynb)

An example of the Twitter DataFrame looks like this
| Datetime                   | Tweet Id             | Username       | Text                                                     | 
| --------                   | --------             | --------       | --------                                                 |
| 2020-03-13 23:49:38+00:00	 | 1238613218425073664  | Phallossus     | Slap the shit out of anyone tries to give me Chinaman flu| 


### Google Search Data
- Proxy to capture people’s general interest and concern over Sinophobic words and topics
- Old search terms: chink, chinaman, chinkland, gook
- New search terms: China virus, Chinese virus, Wuhan virus, Kung flu
- [Google search dataset](https://github.com/macs30200-s23/replication-materials-yuzhouw313/tree/main/Google%20data) is collected from [Google Trends website](https://trends.google.com/home)

An example of the Google search DataFrame looks like this
| Day            | chink + chinaman + chinkland + gook: (United States)|
| --------       | -------                                             |
| 2020-01-01		 | 59                                                  |


### FBI Data
- The original FBI Hate Crime Statistical Dataset csv file can be found [here](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/FBI_hatecrime/hate_crime.csv) which ranges from 1991 to 2021
- I preprocessed the dataset and converted it into a DataFrame which contains all anti-Asian hate crimes from the year 2020, which has a size of <i>356</i> anti-Asian hate crime incidents
- First, the law enforcement officer recording an incident decides whether it might constitute a hate crime. Second, potential hate crime cases are evaluated by officers with special training in hate crime matters. The FBI (2015) states (p. 35): “For an incident to be reported as a hate crime, sufficient objective facts must be present to lead a reasonable and prudent person to conclude that the offenders actions were motivated, in whole or in part, by bias.”

An example of preprocessed FBI data looks like this:
| incident_date  | count|
| --------       | -----|
| 2020-01-05		 | 2    |


## Methods
### Twitter Dataset EDA
[Jupyter Notebook to Analyze Twitter Data](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_google_analysis.ipynb)
- Use nltk package to (1) lowercase all tweets, (2) remove irrelavent components such as URLs, (3) remove stop words, (4) lemmatize, and (5) stem all tweets
- Use SentimentIntensityAnalyzer to compute negative, positive, neutral, and compound sentiment scores for each preprocessed tweet
- Conduct some basic statistics analysis to get mean, median, std, min, and quartiles
- Conduct time series analysis using both day and month as unit of analysis, calculating rolling means and trend analysis for both short-term and long-term patterns
- Visualization

### Google search Dataset
- [Jupyter Notebook to Analyze Google Search Data](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_google_analysis.ipynb)
- Aggregate data by daily and weekly level
- Visualize the trends
- Using statsmodels to conduct time series analysis 

### FBI Dataset
[Jupyter Notebook to Analyze FBI Data](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/FBI_hatecrime/crime_analysis.ipynb)
- Filter hate crime incidents of 2020 and desciption bias of anti-Asian
- Aggregate Dataframe by Weekly hate crime incidents instead of individual incident for the sake of statistical significance
- Visualize the trend of anti-Asian hate crime incidents
- Calculate basic statistics such as monthly mean, median, standard deviation, etc.
- Using statsmodels to conduct time series analysis


## Results
### EDA on Twitter, Google search, and hate crime time series objects


![alt text](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/pictures_README/sentiment_compound.png)
  
- <b><i>Monthly Rolling Means Analysis -- Short-Term</i></b>

  - This rolling mean shows the average sentiment score over a period of time, with each data point representing the average score for the previous 3 months.
  - For this particular rolling mean, we can see that the sentiment score started off high in February 2020, but then sharply decreased in March and April before stabilizing around a slightly negative sentiment score for the rest of the year.
  - One interesting point to note is the sudden spike in sentiment score in September and October, which suggests a temporary shift in sentiment towards a more positive outlook, before returning to a slightly negative sentiment score in the final months of the year.

![alt text](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/pictures_README/rolling_monthly.png)

- <b><i>Daily Rolling Means Analysis -- Short-Term</i></b>
  - Notice here, however, if we don't aggregate tweets into monthly but instead analyze them in a daily basis, we see again the constant and seemingly patternless plot as shown below

![alt text](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/pictures_README/rolling_daily.png)


### FBI Hate Crime Dataset
1. Anti-Asian Hate Crime in 2020 Visualization

![alt text](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/pictures_README/monthly_crime.png)
![alt text](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/pictures_README/bimonthly_crime.png)


Rolling Mean:
|                |   hate_crimes |
|:---------------|--------------:|
| 2020-01-01     |           nan |
| 2020-02-01     |           nan |
| 2020-03-01     |        29     |
| 2020-04-01     |        39.67  |
| 2020-05-01     |        49.67  |
| 2020-06-01     |        44.33  |
| 2020-07-01     |        36.33  |
| 2020-08-01     |        28     |
| 2020-09-01     |        24.67  |
| 2020-10-01     |        24.67  |
| 2020-11-01     |        24     |
| 2020-12-01     |        20.67  |

Trend Analysis:
Date       | Value
---        | ---
2020-01-01 | 36.246475
2020-02-01 | 35.155348
2020-03-01 | 34.052817
2020-04-01 | 32.914256
2020-05-01 | 31.728130
2020-06-01 | 30.493585
2020-07-01 | 29.217434
2020-08-01 | 27.911808
2020-09-01 | 26.586828
2020-10-01 | 25.247043
2020-11-01 | 23.898512
2020-12-01 | 22.547764

After preprocessing and aggregating our FBI Hate Crime Dataset, we conducted time series analysis and found that
- based on the rolling means, we see that the average number of hate crimes per month increased from March to May (29 to 49.67), indicating a potential spike in hate crimes during that period. However, the rolling mean decreased from May to June (49.67 to 44.33), suggesting that the number of hate crimes may have decreased in June. The rolling mean then decreased further from June to July (44.33 to 36.33) and continued to decrease gradually until December (20.67), indicating a general downward trend in the number of hate crimes.
- based on trend analysis, we see that the number of hate crimes per month decreased from January (36.25) to December (22.55), suggesting a general downward trend in the number of hate crimes throughout the year. The negative trend value (-1.69) indicates that the time series data is decreasing over time.

![alt text](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/pictures_README/crime_rolling.png)


### Notice that, when comparing the monthly rolling means for Twitter anti-Chinese dataset and FBI anti-Asian hate crime dataset, we see a delaying trend in the former. That is, the increase and spike of the FBI anti-Asian Hate Crimes precede those of the Twitter data. Although without further statistical analysis and causality test we cannot conclude any correlation or causality between the two variables, we can have a sense of the order or prediction power of these two variables.


## How to Cite
```python
cff-version: 1.15.0
message: "If you use this software, please cite it as below."
authors:
  - family-names: Wang
    given-names: Yuzhou
    orcid: https://orcid.org/0009-0005-1443-0532
title: "The relationship between online Sinophobic sentiment and anti-Chinese hate crimes"
version: 1.0.0
date-released: 2023-04-16
url: "https://github.com/macs30200-s23/replication-materials-yuzhouw313"
```

APA Format
```python
Wang, Y. (2023). The relationship between online Sinophobic sentiment and anti-Chinese hate crimes (Version 1.0.0) [Computer software]. https://github.com/macs30200-s23/replication-materials-yuzhouw313
```

BibTeX Format
```python
@software{Wang_The_relationship_between_2023,
author = {Wang, Yuzhou},
month = {4},
title = {{The relationship between online Sinophobic sentiment and anti-Chinese hate crimes}},
url = {https://github.com/macs30200-s23/replication-materials-yuzhouw313},
version = {1.0.0},
year = {2023}
}
```


## References:
Jacobs, L., & van Spanje, J. (2021). A Time-Series Analysis of Contextual-Level Effects on Hate Crime in The Netherlands. Social Forces, 100(1), 169–193. https://doi.org/10.1093/sf/soaa102

MartinKBeck. (2021). snscrape: A Social Networking Service scraper in Python. GitHub repository. Retrieved Month Day, Year, from https://github.com/MartinKBeck/TwitterScraper/tree/master/snscrape

Shen, X., He, X., Backes, M., Blackburn, J., Zannettou, S., & Zhang, Y. (2022). On Xing Tian and the Perseverance of Anti-China Sentiment Online. Proceedings of the International AAAI Conference on Web and Social Media, 16, 944–955. https://doi.org/10.1609/icwsm.v16i1.19348
