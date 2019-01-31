import tweepy
import random
import time 

# Generated from the Twitter API

consumer_key = "ENTER KEY HERE"

consumer_secret = "ENTER SECRET HERE"

access_token = "ENTER TOKEN HERE"

access_token_secret = "ENTER ACCESS TOKEN SECRET HERE"

#Tweepy authentication middleware

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


languages = ["Python","C++","JavaScript","Java","Swift","C#"] #Feel free to mix and match your messages!

mainMessage = f"Hey you should learn {random.choice(languages)}! Try by learning how to say Hello World! It's pretty cool!" #The f-string is used in conjuction with random.choice to grab a random value from the array

seen = {} # Keep a memo of users you have already messaged, so you don't bombard them with tweets


while True:
    searching = api.search("\"hello world\"") #search all public tweets for the phrase "hello world"#
    recipient = searching[0].user.screen_name #store the first tweet's screen_ name
    if recipient not in seen: #if the username has not already been tweeted to, tweet them
        api.update_status(f"@{recipient} {mainMessage}",searching[0].id) #api.update_status is taking two parameters in this case, the tweet itself, and who the tweet is in reply to, so the id of the user
        print(f"sent hello world to {recipient}")
        seen[recipient] = 1 #store the usernamme in the memo
    time.sleep(30) #try the loop again in 30 seconds
