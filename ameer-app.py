# Short code
import tweepy
api_key = 'K7RfVNIo7Ffyat0mSO42YsMwg'
api_secret_key = 'j8ytz5cfSovEkTw7SB4o3tESCIN6iBaBaWyJv3gsN9euY63h10'
access_token = '1303659259079487488-dNQNwCSCRcQNJgtMNHsMHGJzzx9qjN'
secret_access_token = 'ghGL6VDeoHtuxT36bE6Z8Wwzrw5LSX8D6KNBMOEGdfT7k'

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

  

