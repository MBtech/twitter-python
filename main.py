import tweepy
import yaml

file = open("credentials.yaml", 'r')
cred = yaml.load(file)
auth = tweepy.OAuthHandler(cred['consumer_key'], cred['consumer_secret'])
auth.set_access_token(cred['access_token'], cred['access_token_secret'])
api = tweepy.API(auth)
#api.update_status(status="Sorry for the mean, awful and hurtful accurate things I said #Sarcast")
user = api.get_user('realDonaldTrump')
print("Name:",user.name)
print("Location:",user.location)
print("Following:",user.friends_count)
print("Followers:",user.followers_count)
places = api.trends_available()
#for place in places:
#    trends = api.trends_place(place['woeid'])
#    print(trends)
