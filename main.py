import tweepy
import yaml
import pickle
import os.path
import time

def saveUsers(users, filename):
    pickle.dump(users, open(filename, "wb" ) )

def crawler(api, seed):
    found = set(list())
    searched = set(list())
    for s in seed:
	print s
        #users = api.followers(s)
        user_ids = api.friends_ids(s)
        for user_id in user_ids:
            print user_id
            u = api.get_user(user_id)
            print u.screen_name
            found.add(u.screen_name)
            time.sleep(10)
            saveUsers(found, "found.p")
        searched.add(s)
        saveUsers(searched, "searched.p")

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

seed = set(['realDonaldTrump', 'BarackObama', 'TheDailyShow', 'iamjohnoliver', '20thcenturyfox', 'CNN', 'TIME', 'FoxNews'])

if(os.path.exists("people.p")):
    people = pickle.load( open( "found.p", "rb" ) )
    crawler(api, people)
else:
    crawler(api, seed)

#places = api.trends_available()
#for place in places:
#    trends = api.trends_place(place['woeid'])
#    print(trends)
