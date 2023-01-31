# Tweepy-Tweet-Library
This is a python program that I have created for fun thats main purpose was to help me learn about the real world applications of python programing. Essentially what my program does is it opens up a stream to twitter using the tweepy package, and will gather tweets that contain the hashtags #startup, #entrepreneur, and #smallbusiness. Once three tweets have been gathered in real time the stream will disconect and you will be able to view the tweets through the terminal window. From there, using input prompts, you are able ot view cirtain data that has been collected about each of the tweets(such as the length of the tweet, when it was created, etc.). The program itself is slightly unfinished as I had planned to add a few more categories of data that could be accessed, however the project began feeling very repetetive, and I wanted to move onto something new that I could work on and learn from.

The third file that I have added to the repository named "TweepyAuthorization.py" will not work together with the other two files if you try to run it yourself. This is because in my version of the file I have my own tweepy authorization details that have been generated through my own Twitter Developer Account. If you wish to try and run it yourself to see how it works, replace the four authentifacation details in this file and then try to run it. Make sure that each of the three files are in the same folder to make sure everythung import properly.

Lastly, there are a couple of modules and packages that need to be downloaded. These modules include nltk and tweepy. nltk is used to create the tokenizer that is used to break up the text for analysis. Tweepy is used to access the twitter API and extract the tweets in real time.

If you have any questions about the code or how to get it to work please let me know I would love to help. Also, if any of it can be done better or more efficiantly please let me know. As I said before I have created this project to learn more about the practiacality of coding and if it could be made more practical I would love to improve it.
