# Creating a twitter library

# Note: Make sure to enable tweet fields before finding tweet attributes

import tweepy
from TweepyAuthorization import CreateAPI
from TweepyAuthorization import BearerToken
from nltk.tokenize import word_tokenize
import Tokenizer

api = CreateAPI()

#---------#
# Classes #
#---------#
class MyStream(tweepy.StreamingClient):

    def on_connect(self):
        print('Connected')
        self.Lib = {}
        self.selection = 1

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            # This will make additions to the Library as they come in
            print('Adding Tweet')
            self.Lib = self.add_to_lib(tweet, self.Lib)
            if len(self.Lib) == 3:
                self.disconnect()

    # Function returns the dictionary with the added tweet(key=id, value=object containing statistics)
    def add_to_lib(self, tweet, dictionary):
        dictionary[tweet.id] = TweetInformation(tweet, self.selection)
        self.selection += 1
        return dictionary

    # Disconnectes the stream
    def disconnect(self):
        self.running = False
        print('Disconnected')

    # This will be called in the regular program to access the Library once the stream is disconnected
    def export_tweet_data(self):
        return self.Lib

class TweetInformation():

    # set some of the tweet statistics here
    # Completed personal statistics:
    #   -> Text
    #   -> Language
    #   -> ID
    #   -> Date Created (5 hours ahead of est)
    #   -> Avg Letters per word
    #   -> Length of the tweet
    def __init__(self, tweet, selection):
        self.text = self.TweetText(tweet)
        self.lang = tweet.lang
        self.date_and_time = tweet.created_at
        self.letters_per_word = self.avg_letters()[0]
        self.length_of_tweet = self.avg_letters()[1]
        self.selection = selection

    # Returns the tweet text statistic without being truncated
    # If Truncation is a problem fix it here
    def TweetText(self, tweet):
        return tweet.text
    
    # This method will tokanize the tweet to prepare for analysis
    # Will return nothing if used before the text is processed
    def tokenize(self):
        try:
            return Tokenizer.preprocess(self.text)
        except AttributeError:
            return None

    # Calculates the average number of letters per word in a tweet
    # Will not count emoticons, links and hashtags
    def avg_letters(self):
        processedTweet = self.tokenize()
        totalLetters = 0
        for numOfWords, term in enumerate(processedTweet):
            totalLetters += len(term)
            totalWords = numOfWords
        return [totalLetters // (totalWords + 1), totalWords + 1]
            

#-----------#
# Functions #
#-----------#

        
#--------------#
# Main Program #
#--------------#
def main():
    
    stream = MyStream(BearerToken)

    # Sets each of the search terms in the stream
    search_terms = ['#startup', '#entrepreneur', '#smallbusiness']
    for term in search_terms:
        stream.add_rules(tweepy.StreamRule(term))

    # Opens the stream and gathers the tweets
    stream.filter(tweet_fields=['referenced_tweets', 'lang', 'created_at'])

    # Once the stream is disconnected the tweets are saved to "Library"
    Library = stream.export_tweet_data()

    # This is where the data can be accessed
    while True:
        for ID in Library:
            print(str(Library[ID].selection) + ':', ID)
        print()
        print('Please select a tweet to analyze(-1 to quit program):')
        selected = int(input('--> '))
        print()
        if selected == -1:
            break
        for ID in Library:
            if Library[ID].selection == selected:
                selectedID = ID

        print('Please select a attribute to display:')
        print('Text')
        print('Language')
        print('ID')
        print('Date created')
        print('Avg letters per word')
        print('Length of tweet')
        print('Exit')
        print()

        while True:
            attribute = input('--> ')
            if attribute == 'Text':
                print(Library[selectedID].text)
            elif attribute == 'Language':
                print(Library[selectedID].lang)
            elif attribute == 'ID':
                print(selectedID)
            elif attribute == 'Date created':
                print(Library[selectedID].date_and_time)
            elif attribute == 'Avg letters per word':
                print(Library[selectedID].letters_per_word)
            elif attribute == 'Length of tweet':
                print(Library[selectedID].length_of_tweet)
            elif attribute == 'Exit':
                print()
                break
            else:
                print('Entry not valid. Please Try again.')
            print()


if __name__ == '__main__':
    main()











