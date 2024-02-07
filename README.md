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

For the mapping step, I begin with the Twitter dataset split into 366 zip files for each day of the year (2020 was a leap year), with each zip file containing 24 text files for each hour of the day. The each line of the text file is one tweet stored in JSON format, containing different attributes about the tweet including the tweet contents, username and profile information, location, date, language, number of retweets, and more. Each of these zip files is processed separately by map.py, which allows for the computations to be performed in parallel. For each zip file, map.py counts the number of uses of certain hand-selected hashtags relevant to the COVID-19 pandemic, tracking both by language and by country. To perform this mapping on each of the zip files, I created a simple shell script run_maps.sh to handle calling map.py on each of the files in the background, and ran it with the nohup command to ensure the program would not be interrupted. My mapping step was able to finish running overnight.

I created two different reduce programs which I use to create different visualizations of the twitter data. The first (reduce.py) simply sums the counts of each hashtag by language and country to get overall counts for the entire year of 2020. I use this program to create bar charts of which countries/languages tweeted certain hashtags (such as '#coronavirus') the most. The second (alternative_reduce.py) sums together all of the languages using each hashtag for that day, and outputs a list of usage counts for the desired hashtags for each day over the course of the year. I use this ouput to create a line plot tracking various hashtags' popularity over time.

## Results

<center>
<img width='100%' src=data_visualization/top_10_coronavirus_hashtags_by_country_chart.png />
</center>

<center>
<img width='100%' src=data_visualization/top_10_coronavirus_hashtags_by_lang_chart.png />
</center>

<center>
<img width='100%' src=data_visualization/top_10_코로나바이러스_hashtags_by_country_chart.png />
</center>

<center>
<img width='100%' src=data_visualization/top_10_코로나바이러스_hashtags_by_lang_chart.png />
</center>


**Task 1: Run the mapper**



**Task 2: Reduce**

> **HINT:**
> You should manually inspect the output of your mapper code to ensure that it is reasonable and that you did not run into any error messages.
> If you have errors above that you don't deal with,
> then everything else below will be incorrect.

After your modified `map.py` has run on all the files,
you should have a large number of files in your `outputs` folder.
Use the `reduce.py` file to combine all of the `.lang` files into a single file,
and all of the `.country` files into a different file.

**Task 3: Visualize**

Recall that you can visualize your output files with the command
```
$ ./src/visualize.py --input_path=PATH --key=HASHTAG
```
Currently, this prints the top keys to stdout.

Modify the `visualize.py` file so that it generates a bar graph of the results and stores the bar graph as a png file.
The horizontal axis of the graph should be the keys of the input file,
and the vertical axis of the graph should be the values of the input file.
The final results should be sorted from low to high, and you only need to include the top 10 keys.

> **HINT:**
> We are not covering how to create images from python code in this class.
> I recommend you use the matplotlib library,
> and you can find some samples to base your code off of [in the documentation here](https://matplotlib.org/3.1.1/tutorials/introductory/sample_plots.html).

Then, run the `visualize.py` file with the `--input_path` equal to both the country and lang files created in the reduce phase, and the `--key` set to `#coronavirus` and `#코로나바이러스`.
This should generate four plots in total.

**Task 4: Alternative Reduce**

Create a new file `alternative_reduce.py`.
This file should take as input on the command line a list of hashtags,
and output a line plot where:
1. There is one line per input hashtag.
1. The x-axis is the day of the year.
1. The y-axis is the number of tweets that use that hashtag during the year.

Your `alternative_reduce.py` file have to follow a similar structure to a combined version of the `reduce.py` and `visualize.py` files.
First, you will scan through all of the data in the `outputs` folder created by the mapping step.
In this scan, you will construct a dataset that contains the information that you need to plot.
Then, after you have extracted this information,
you should call the appropriate matplotlib functions to plot the data.

> **HINT:**
> The specifications for this program and plot are intentionally underspecified
> (similar to how many real-world problems are underspecified).
> Feel free to ask clarifying questions.

**Task 5: Uploading**

Commit all of your code and images output files to your github repo and push the results to github.
You must:
1. Delete the current contents of the `README.md` file
1. Insert into the `README.md` file a brief explanation of your project, including the 4 generated png files.
    This explanation should be suitable for a future employer to look at while they are interviewing you to get a rough idea of what you accomplished.
    (And you should tell them about this in your interviews!)

## Submission

Upload a link to you github repository on sakai.
I will look at your code and visualization to determine your grade.

**Grading:**

The assignment is worth 32 points:

1. 8 points for getting the map/reduce to work
1. 8 points for your repo/readme file
1. 8 points for Task 3 plots
1. 8 points for Task 4 plots

The most common ways to miss points are:
1. having incorrect data plotted (because the map program didn't finish running on all of the inputs)
1. having illegible plots that are not "reasonably" formatted

Notice that we are not using CI to grade this assignment.
There's two reasons:

1. You can get slightly different numbers depending on some of the design choices you make in your code.
    For example, should the term `corona` count tweets that contain `coronavirus` as well as tweets that contain just `corona`?
    These are relatively insignificant decisions.
    I'm more concerned with your ability to write a shell script and use `nohup`, `&`, and other process control tools effectively.

1. The dataset is too large to upload to github actions.
    In general, writing test cases for large data analysis tasks is tricky and rarely done.
    Writing correct code without test cases is hard,
    and so many (most?) analysis of large datasets contain lots of bugs.
