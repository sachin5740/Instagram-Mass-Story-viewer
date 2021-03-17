import instabot
import time
from os import system, name 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

HASHTAGSs = ['love', 'romantic', "model", "shopping", "dress" , "memes"]
HASHTAGS = ['indianmemes', 'memes', 'desimemes', 'funnymemes', 'dankmemes', 'memesdaily', 'meme', 'bakchodi', 'chutiyapa', 'hindimemes', 'india', 'funny', 'sarcasm', 'bollywoodmemes', 'indianjokes', 'sarcasticmemes', 'bakchod', 'indianmemesdaily', 'follow', 'chutiyapanti', 'trolls', 'rvcjinsta', 'jokes', 'dailymemes', 'adultmemes', 'indianmeme', 'indian', 'carryminati', 'bollywood', 'bhfyp', 'desijokes', 'instagram', 'comedy', 'sarcastic', 'memer', 'like', 'love', 'bakchodiyaan', 'indianmemestore', 'bcbilli', 'fun', 'sakhtlaunda', 'lol', 'hindijokes', 'memestagram', 'bbkivines', 'tiktok', 'chutiya', 'trending', 'likeforlikes', 'lockdown', 'funnyvideos', 'adultjokes', 'desimeme', 'desi', 'desifun', 'dekhbhai', 'adultgram', 'bhfyp', 'backbenchers', 'likes', 'like', 'follow', 'likeforlikes', 'love', 'instagood', 'instagram', 'followforfollowback', 'followme', 'photooftheday', 'bhfyp', 'instalike', 'photography', 'instadaily', 'me', 'picoftheday', 'beautiful', 'myself', 'likeforfollow', 'fashion', 'smile', 'followers', 'likeforlike', 'followback', 'followforfollow', 'comment', 'likesforlikes', 'bhfyp', 'happy', 'style', 'life', 'photo', 'nature', 'cute', 'insta', 'model', 'music', 'travel', 'likesforlike', 'girl', 'selfie', 'viral', 'loveyourself', 'following', 'memes', 'beauty', 'liker', 'lfl', 'yourself', 'lifestyle', 'likeback', 'sad', 'thoughts', 'writer', 'photographer', 'k', 'photoshoot', 'india','love', 'romantic', "model", "shopping", "dress" , "memes"]

SLEEP_TIME_BETWEEN_MAIN_LOOP = 5 * 60
SLEEP_TIME_BETWEEN_HASHTAG_LOOP = 60
USERNAME = 'baby_girl_giya'
PASSWORD = 'Sachin@123'

bot = instabot.Bot()

bot.login(username=input('enter Your Username : '), password=input('enter Your password : '))
# bot.login(username=USERNAME, password=PASSWORD)

# MAIN LOOP
while True:
    try:
        for hashtag in HASHTAGS :
            clear()
            # GET USERS FROM HASHTAG
            users = bot.get_hashtag_users(hashtag)
            for id in users:
                # WATCH USER STORIES
                if bot.watch_users_reels(id):
                    bot.logger.info(f'Instagram user: {id}, Total stories viewed: {bot.total["stories_viewed"]}')
            bot.logger.info(f'Sleeping for {SLEEP_TIME_BETWEEN_HASHTAG_LOOP} seconds...')           
            time.sleep(SLEEP_TIME_BETWEEN_HASHTAG_LOOP)
        bot.logger.info(f'Sleeping for {SLEEP_TIME_BETWEEN_MAIN_LOOP} seconds...')           
        time.sleep(SLEEP_TIME_BETWEEN_MAIN_LOOP)

    except Exception as e:
        bot.logger.info(e)
        time.sleep(SLEEP_TIME_BETWEEN_MAIN_LOOP)