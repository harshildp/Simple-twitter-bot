import tweepy,  time # access to Twitter API and time 

# Keep the quotes and fill in the fields below with the appropriate tokens and keys
CONSUMER_KEY = 'some key'
CONSUMER_SECRET = 'some secret'
ACCESS_TOKEN = 'some token'
ACCESS_SECRET = 'some other secret'

# Authenticates and allows access for the bot to use the provided account
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth

# Feeds the file from which tweets are to be posted 
filename = open('content.txt')
f = filename.readlines()
filename.close()

# Logic for creating the post
for line in f:
    try:
        api.update_status(line)
        print('Tweeting! :)') # success
    except tweepy.TweepError as err:
        print(err) # failure
    time.sleep(90) # every minute and half
    
print('All tweets completed! Goodnight Zzzz')

