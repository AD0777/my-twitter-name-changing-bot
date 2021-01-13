# Short code
import tweepy
api_key = 'IKB2Ce7CSVPTBC62ElYPfgGQV'
api_secret_key = 'CFDmCz2CVvxyXSUYqFodmvgx52EIYhCT8GhffXDQTEtsuyO2X4'
access_token = '1303659259079487488-iGOgIdTFJ7fPlM0hyfo8Ej5BpR32m3'
secret_access_token = 'IE8ab5VFIanZzhYrSleWORrxGrKfHALSbtrMmFif9TeyC'

auth = tweepy.OAuthHandler(api_key, api_secret_key)       #for authentication 
auth.set_access_token(access_token, secret_access_token)

api = tweepy.API(auth)

import time 
while True: 
  user = api.get_user('AD_bxd')
  follower = user.followers_count 
  api.update_profile(name = f'ARYAMAN {follower} followers')
  print(f'ARYAMAN {follower} followers')
  time.sleep(60)                      #but this wont work if the program is not running all the time 
         
