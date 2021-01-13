# Short code
import tweepy
api_key = ''
api_secret_key = ''
access_token = ''
secret_access_token = ''

auth = tweepy.OAuthHandler(api_key, api_secret_key)       
auth.set_access_token(access_token, secret_access_token)
api = tweepy.API(auth)
print('Everything is fine')

import time 
while True: 
  user = api.get_user('')
  follower = user.followers_count 
  api.update_profile(name = f'AMEER {follower} followers')
  print(f'AMEER {follower} followers')
  time.sleep(60)          
