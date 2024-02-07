# Coronavirus Hashtag Twitter Analysis

In this project, I scan all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media.

**Project Outcomes:**

1. working with large scale datasets
2. working with multilingual text
3. using the MapReduce divide-and-conquer paradigm to create parallel code to run on a remote server
4. practicing data analysis and visualization techniques

## Background

**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
In this project, I work with a dataset of about 1.1 billion geotagged tweets posted.

**About MapReduce:**

To speed up long computation times, I use the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze these tweets.
All computations from this data analysis project were performed on a remote server with 80 processors, allowing parallelization to improve computation time by up to a factor of 80.

For the mapping step, I begin with the Twitter dataset split into 366 zip files for each day of the year (2020 was a leap year), with each zip file containing 24 text files for each hour of the day. The each line of the text file is one tweet stored in JSON format, containing different attributes about the tweet including the tweet contents, username and profile information, location, date, language, number of retweets, and more. Each of these zip files is processed separately by map.py, which allows for the computations to be performed in parallel. For each zip file, map.py counts the number of uses of certain hand-selected hashtags relevant to the COVID-19 pandemic, tracking both by language and by country. To perform this mapping on each of the zip files, I created a simple shell script run_maps.sh to handle calling map.py on each of the files in the background, and ran it using `$ nohup run_maps.sh &` to ensure the program would not be interrupted. My mapping step was able to finish running overnight.

I created two different reduce programs which I use to create different visualizations of the twitter data. The first (reduce.py) simply sums the counts of each hashtag by language and country to get overall counts for the entire year of 2020. I use this program to create bar charts of which countries/languages tweeted certain hashtags (such as '#coronavirus') the most. The second (alternative_reduce.py) sums together all of the languages using each hashtag for that day, and outputs a list of usage counts for the desired hashtags for each day over the course of the year. I use this ouput to create a line plot tracking various hashtags' popularity over time.

## Results

<table border="0">
 <tr>
     <td></td>
     <td>Top 10 By Country</td>
     <td>Top 10 By Language</td>
 </tr>
 <tr>
    <td>'#coronavirus'</td>
    <td>
        <img width='100%' src=data_visualization/top_10_coronavirus_hashtags_by_country_chart.png />
    </td>
    <td><img width='100%' src=data_visualization/top_10_coronavirus_hashtags_by_lang_chart.png />
</td>
 </tr>
 <tr>
    <td>'#코로나바이러스' ('#coronavirus' in Korean)</td>
    <td><img width='100%' src=data_visualization/top_10_코로나바이러스_hashtags_by_country_chart.png /></td>
    <td><img width='100%' src=data_visualization/top_10_코로나바이러스_hashtags_by_lang_chart.png /></td>
 </tr>
</table>

<center>
    <img width='100%' src=data_visualization/covid_hashtags.png />
</center>

# TODO: Ask Mike if barplots need to be low to high or if high to low is ok

