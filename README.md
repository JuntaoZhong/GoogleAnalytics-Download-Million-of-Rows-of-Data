# GoogleAnalytics-Download-Million-of-Rows-of-Data

Google Analytics API allows users to download 10,000 rows of web visit data at a time. But for a large enterprise, there might be millions of rows of data to be download. 
This Python Script goes around Google Analytics API's download limit. It pull 10,000 at a time but compile these 10,000 together into a csv. that contains much more than 10,000 rows. 
The code is originally from www.ryanpraski.com in Python2. I modified it and included a Python3 version of code to run.  

This repository contains two pieces of codes: first, a python API code by Ryan Praski. Often, if there are 200,000+ rows, script will return an error. So, I recommend selecting the right month range so that there is less than 200,000 rows of data in one csv. file. 

Also, if you are only interested in a list of (hundreds of, or thousands of) websites. I wrote the second part of the codes, which selects only websites in that list. And then, it compiles the click statistic from the csv. files for each month into a big csv. Each column in the big csv. is named as the monthly file names
