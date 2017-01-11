
from instabot import InstaBot
from check_status import check_status
from feed_scanner import feed_scanner
from unfollow_protocol import unfollow_protocol
from follow_protocol import follow_protocol
import time


bot = InstaBot(login="username", password="passaqui",
               like_per_day=100,
               comments_per_day=0,
               tag_list=['picoftheday', 'tech', 'security', 'marketing', 'marketingdigital', 'design', 'designer', 'redesociais', 'marketingsocial', 'assistenciatecnica', 'recuperacaodedados', 'datarecovery', 'website', 'responsivedesign', 'responsive', 'pantone'],
               tag_blacklist=['rain', 'thunderstorm'],
               user_blacklist={},
               max_like_for_one_tag=250,
               follow_per_day=150,
               follow_time=1*60,
               unfollow_per_day=150,
               unfollow_break_min=90,
               unfollow_break_max=120,
               log_mod=0,
               proxy='',
               
               unwanted_username_list=['second','stuff','art','project','love','life','food','blog','free','keren','photo','graphy','indo',
                                       'travel','art','shop','store','sex','toko','jual','online','murah','jam','kaos','case','baju','fashion',
                                        'corp','tas','butik','grosir','karpet','sosis','salon','skin','care','cloth','tech','rental',
                                        'kamera','beauty','express','kredit','collection','impor','preloved','follow','follower','gain',
                                        '.id','_id','bags'])
while True:


    ################################
    ###  api manhosa first try   ###
    ################################

    mode = 0

    if mode == 0 :
        bot.new_auto_mod()

    elif mode == 1 :
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10*60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) <50 :
                feed_scanner(bot)
                time.sleep(5*60)
                follow_protocol(bot)
                time.sleep(10*60)
                check_status(bot)

    elif mode == 2 :
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3 :
        unfollow_protocol(bot)
        time.sleep(10*60)

    elif mode == 4 :
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10*60)

    elif mode == 5 :
        bot.bot_mode=2
        unfollow_protocol(bot)

    else :
        print ("Wrong mode!")
