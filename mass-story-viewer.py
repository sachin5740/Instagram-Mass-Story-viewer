import instabot
bot = instabot.Bot()
bot.login(username='input("enter Your UserName: ")', password=input('enter Your password : '))
# bot.l
# using_location=bot.get_geotag_users(LOCATION)
using_hashtag=bot.get_hashtag_users('sarcasm')
# using_user_id=bot.get_user_followers(USER_ID)
print(len(using_hashtag))

# for id in bot.get_hashtag_users("memes"):
#     bot.watch_users_reels(id)
#     print("#")
# bot.logout()