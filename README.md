# GoogleAnalytics-Download-Million-of-Rows-of-Data

Google Analytics API allows users to download 10,000 rows of web visit data at a time. But for a large enterprise, there might be millions of rows of data to be download. 
This Python Script goes around Google Analytics API's download limit. It pull 10,000 at a time but compile these 10,000 together into a csv. that contains much more than 10,000 rows. 
The code is originally from www.ryanpraski.com in Python2. I modified it and included a Python3 version of code to run.  
