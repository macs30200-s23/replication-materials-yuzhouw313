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

### Google search Dataset EDA
- [Jupyter Notebook to Analyze Google Search Data](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/twitter_google_analysis.ipynb)
- Aggregate data by daily and weekly level
- Visualize the trends
- Using statsmodels to conduct time series analysis 

### FBI Dataset EDA
[Jupyter Notebook to Analyze FBI Data](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/FBI_hatecrime/crime_analysis.ipynb)
- Filter hate crime incidents of 2020 and desciption bias of anti-Asian
- Aggregate Dataframe by Weekly hate crime incidents instead of individual incident for the sake of statistical significance
- Visualize the trend of anti-Asian hate crime incidents
- Calculate basic statistics such as monthly mean, median, standard deviation, etc.
- Using statsmodels to conduct time series analysis

### [VAR (Vector Autoregression) Model](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/granger_causality.ipynb)
- Estimate the long-run relationship among Tweets, Google searches, and hate crimes
- Regress each variable on its own past values as well as past values of all other variables

### [Granger Gausality Test](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/granger_causality.ipynb)
- Summarize the estimated parameters obtained from the VAR model
- Establish the presence and direction of Granger causality between two variables
- Trend X at time t should provide insights to predict trend Y at time t + 1



## Results
### EDA on Twitter, Google search, and hate crime time series objects

![alt text](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/plots/weekly_tweets.png)

![alt text](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/plots/weekly_google.png)

![alt text](https://github.com/macs30200-s23/replication-materials-yuzhouw313/blob/main/plots/weekly_crime.png)

1. A sharp increase in both the trends of Sinophobic tweets and of anti-Asian hate crimes shortly after the first case of COVID-19 in the US
2. While the trend of Sinophobic Tweets remained high from April to June, anti-Asian hate crimes decreased after March
3. Traditional Sinophobic searches > COVID-19-related searches except from mid-Jan to mid-Feb 
4. COVID-19-related Sinophobic searches decreased after the CDC announced the official name
5. Traditional Sinophobic searches persisted at high levels, COVID-19-related searches and hate crimes decreased in April

### Daily Granger Causality
<img width="1750" height="80" alt="image" src="https://github.com/macs30200-s23/replication-materials-yuzhouw313/assets/112440950/aab826d8-0cb7-4190-9cd0-dd8bd28645ae">

### Weekly Granger Causality
<img width="1750" height="250" alt="image" src="https://github.com/macs30200-s23/replication-materials-yuzhouw313/assets/112440950/3ca54952-ae4b-4315-a930-e087148b9714">

1. No Granger causality between Sinophobic Tweets and Google searches on traditional or COVID-19-related terms on daily or weekly basis
2. Anti-Asian hate crimes Granger causes Sinophobic Tweets 4 weeks later
3. Anti-Asian hate crimes Granger causes Google searches on Sinophobic terms 2 weeks later


## Discussion
### Limitation
1. Keywords only capture traditional Sinophobia on Twitter
2. Keywords may not embody Sinophobic sentiment
3. Alternative meaning of keywords
4. FBI dataset subjects to underreporting issues
5. Anti-Asian hate crimes not ideally representative of anti-Chinese violence

### Social Significance
1. Demonstrate the Granger causality between public sentiment using social media and search engine and real-life violence against the Chinese
2. Challenge the assumption that public sentiment on social media always aligns with search engine trends
3. Contribute to existing literatures of relationships between hate crimes and online sentiment in COVID-19, add new dimensions of Google searches as a measures of public sentiment

### Future Research
- Political rhetoric -> online Sinophobia and anti-Chinese violence?
- Social media and search engine -> broadcasting Sinophobia?
- Normalizing of Sinophobic language -> increasing Sinophobia?
- Social media platform regulations -> addressing racist hate speech?



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
