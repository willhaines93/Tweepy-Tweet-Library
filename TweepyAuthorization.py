# This file could be used by itself to test twitter authentication credentials before using it as part of a main code

import tweepy
import logging
import os

logger = logging.getLogger()

# This is only used to create the stream in TwitterLibrary.py without having credentials hardcoded into the file
BearerToken = os.getenv("BearerToken")

def CreateAPI():

    # Access Credentials
    # Gets the environment variables for twitter authentication credentials
    AccessToken = os.getenv("AccessToken")
    AccessSecret = os.getenv("AccessSecret")
    ConsumerKey = os.getenv("ConsumerKey")
    ConsumerSecret = os.getenv("ConsumerSecret")

    # Creating the authorization and accessing the api
    auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
    auth.set_access_token(AccessToken, AccessSecret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Ensuring credentials are valid
    # If Credentials ore not valid then an error will be raised
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")

    # Returns api as the tweepy object
    return api

