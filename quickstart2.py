""" Quickstart script for InstaPy usage """
# IMPORTS
import os
import time
import csv
from tempfile import gettempdir
import random
import numpy
from selenium.common.exceptions import NoSuchElementException
from instapy import InstaPy
import requests
from instapy.util import get_relationship_counts as grc
from instapy import InstaPy
from instapy.util import smart_run

# ----------------------------------CONSTANTS------------------------------------
likes_per_day = random.randrange(500, 900)
likes_per_hour = random.randrange(40, 80)
follows_per_day = random.randrange(500, 900)
follows_per_hour = random.randrange(40, 80)
unfollows_per_day = random.randrange(500, 900)
unfollows_per_hour = random.randrange(40, 80)
coments_per_day = None
coments_per_hour = None
peak_server_calls_per_day = None
peak_server_calls_per_hour = None
min_time_of_likeorfollow = random.randrange(2, 15)
max_time_of_likeorfollow = random.randrange(30, 60)
# ----------------------------------VARIABLES------------------------------------
random.seed(time.time())
abc = random.randrange(1, 5)
login = False
temp = ['']
def readMyFile(filename):
    data = []
    with open(filename, 'rt') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row[0])
    return data

# -------------------------------login credentials------------------------------------
insta_username = 'smartechpost'
insta_password = 'joaotiago'

# ----------------------------------InstaPy session------------------------------------
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False, multi_logs=True)
# ----------------------------------Supervisor------------------------------------
session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                             peak_likes=(likes_per_hour, likes_per_day),
                             peak_comments=(coments_per_hour, coments_per_day),
                             peak_follows=(follows_per_hour, follows_per_day),
                             peak_unfollows=(unfollows_per_hour,
                                             unfollows_per_day),
                             peak_server_calls=(peak_server_calls_per_hour, peak_server_calls_per_day))
session.set_ignore_if_contains(['sex', 'tasty', 'dick', 'pride', 'gay',
                               'adult', 'adultlife', 'nasty', 'lingerie', 'nails', 'assday'])
#session.set_dont_unfollow_active_users(enabled=True, posts=3)
# Restrictions
my_followers, my_following = grc(session.browser, "joaops95", session.logger)

session.set_relationship_bounds(enabled=True,
                                potency_ratio=None,
                                delimit_by_numbers=True,
                                max_followers=4590,
                                max_following=5555,
                                min_followers=30,
                                min_following=77)
session.set_skip_users(skip_private=True,
                       private_percentage=random.randrange(10, 50),
                       skip_no_profile_pic=True,
                       no_profile_pic_percentage=random.randrange(50, 90),
                       skip_business=True,
                       skip_non_business=False,
                       business_percentage= (20,50),
                       skip_business_categories=[readMyFile('badcategories.csv')],
                       dont_skip_business_categories=[readMyFile('goodcategories.csv')])
session.set_do_comment(False, percentage=10)
session.set_skip_users(skip_private=False)
session.set_simulation(enabled=False)

# ----------------------------------Functions------------------------------------
# Read file function, allows to read any file csv


def doActionBlueprint(filename, actionfn, args):
    #get randomly up to 5 locations
        filedata = readMyFile(filename)
        random.shuffle(filedata)
        filedata = filedata[:random.randrange(1,5)]
        for data_entry in filedata:
            nactions = random.randrange(1,10)
            actionfn([data_entry], **args)
            if (nactions == 0):
                sleeptime = random.randrange(min_time_of_likeorfollow, max_time_of_likeorfollow)
                print('Sleeping for' + str(sleeptime))
                time.sleep(random.randrange(sleeptime))

def likeByLocations():
    doActionBlueprint('Locations2.csv', session.like_by_locations,{'amount':random.randrange(1,10), 'skip_top_posts': True})


    
# Function Like by Tags


def likeByTags():
    myusers = readMyFile('Tags2.csv')
    sizemyusers = len(myusers)
    i = 0
    for i in range(random.randrange(1,5)):
        temp[0] = myusers[random.randrange(0, sizemyusers)]
        print(temp[0])
        a = 0
        while(a <= random.randrange(1, 10)):
            tm = random.randrange(1, 4)
            session.like_by_tags(temp, amount=tm, interact=False)
            if(tm == 1):
                a += 1
                print("1 Like")
            elif(tm == 2):
                a += 2
                print("2 Likes")
            elif(tm == 3):
                a += 3
            else:
                a += 0
                print("sleeping a bit")
                time.sleep(random.randrange(
                    min_time_of_likeorfollow, max_time_of_likeorfollow))

# unfollow function


def unfollow():
        # session.unfollow_users(amount=random.randrange(20,50), onlyNotFollowMe=True, sleep_delay=60)
        # session.unfollow_users(amount=random.randrange(20,50), onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=600, unfollow_after=48*60*60)
    session.unfollow_users(amount=random.randrange(
        20, 50), onlyInstapyFollowed=True, onlyInstapyMethod='FIFO', sleep_delay=60)
    session.unfollow_users(amount=random.randrange(
        20, 50), onlyInstapyFollowed=False, onlyInstapyMethod='LIFO', sleep_delay=60)
# Function to follow that users follow


def followByUserFollow():
    myusers = readMyFile('Users2.csv')
    sizemyusers = len(myusers)
    i = 0
    for i in range(random.randrange(1,5)):
        temp[0] = myusers[random.randrange(0, sizemyusers)]
        print(temp[0])
        a = 0
        while(a <= random.randrange(1, 10)):
            tm = random.randrange(1, 4)
            session.follow_user_following(
                temp, amount=tm, randomize=True, sleep_delay=60)
            if(tm == 1):
                a += 1
                print("1 follow")
            elif(tm == 2):
                a += 2
                print("2 follow")
            elif(tm == 3):
                a += 3
            else:
                a += 0
                print("sleeping a bit")
                time.sleep(random.randrange(
                    min_time_of_likeorfollow, max_time_of_likeorfollow))

# Function to steal the followers of the users


def followByUserFollowers():
    myusers = readMyFile('Users2.csv')
    sizemyusers = len(myusers)
    i = 0
    for i in range(random.randrange(1,5)):
        temp[0] = myusers[random.randrange(0, sizemyusers)]
        print(temp[0])
        a = 0
        while(a <= random.randrange(1, 10)):
            tm = random.randrange(1, 4)
            session.follow_user_followers(
                temp, amount=tm, randomize=True, sleep_delay=60)
            if(tm == 1):
                a += 1
                print("1 follow")
            elif(tm == 2):
                a += 2
                print("2 follow")
            elif(tm == 3):
                a += 3
            else:
                a += 0
                print("sleeping a bit")
                time.sleep(random.randrange(
                    min_time_of_likeorfollow, max_time_of_likeorfollow))

# Function to like in the timeline
def followByUserLikers():
    myusers = readMyFile('Users2.csv')
    sizemyusers = len(myusers)
    i = 0
    for i in range(random.randrange(1,5)):
        temp[0] = myusers[random.randrange(0, sizemyusers)]
        print(temp[0])
        a = 0
        while(a <= random.randrange(1, 10)):
            tm = random.randrange(1, 4)
            session.follow_likers (temp, photos_grab_amount = random.randrange(1, 5), follow_likers_per_photo = tm, randomize=True, sleep_delay=600, interact=True)
            if(tm == 1):
                a += 1
                print("1 follow")
            elif(tm == 2):
                a += 2
                print("2 follow")
            elif(tm == 3):
                a += 3
            else:
                a += 0
                print("sleeping a bit")
                time.sleep(random.randrange(
                    min_time_of_likeorfollow, max_time_of_likeorfollow))

def likeByTimeline():
    session.like_by_feed(amount=random.randrange(
        2, 32), randomize=True, unfollow=False, interact=False)



def followComenters():
    myusers = readMyFile('Users2.csv')
    sizemyusers = len(myusers)
    i = 0
    for i in range(random.randrange(1,5)):
        temp[0] = myusers[random.randrange(0, sizemyusers)]
        print(temp[0])
        a = 0
        while(a <= 5):
            tm = random.randrange(1, 4)
            session.follow_commenters(temp, amount=tm, daysold=random.randrange(1, 200), max_pic=random.randrange(1, 60), sleep_delay=600, interact=False)
            if(tm == 1):
                a += 1
                print("1 follow")
            elif(tm == 2):
                a += 2
                print("2 follow")
            elif(random.randrange(1, 4) == 3):
                a += 3
            else:
                a += 0
                print("sleeping a bit")
                time.sleep(random.randrange(
                    min_time_of_likeorfollow, max_time_of_likeorfollow))

def followSmartHashes():
    myusers = readMyFile('smarthash.csv')
    sizemyusers = len(myusers)
    i = 0
    for i in range(random.randrange(1,5)):
        temp[0] = myusers[random.randrange(0, sizemyusers)]
        print(temp[0])
        a = 0
        while(a <= 5):
            tm = random.randrange(1, 4)
            session.follow_commenters(temp, amount=tm, daysold=random.randrange(1, 200), max_pic=random.randrange(1, 60), sleep_delay=600, interact=False)
            if(tm == 1):
                a += 1
                print("1 follow")
            elif(tm == 2):
                a += 2
                print("2 follow")
            elif(random.randrange(1, 4) == 3):
                a += 3
            else:
                a += 0
                print("sleeping a bit")
                time.sleep(random.randrange(
                    min_time_of_likeorfollow, max_time_of_likeorfollow))


# ---------------------------------- Run Script-------	-----------------------------
try:
    print(login)
    while(True):
        print("Comecou")
        if(int(time.strftime("%H")) >= random.randrange(1,2) and int(time.strftime("%H")) < random.randrange(23,25)):
            if(not login):
                print("Comecou")
                session.login()
                login = True
                print(login)
                print(my_following)
                # settings

            if(my_following >= random.randrange(1000, 1200)):
                ctt = random.randrange(1, 3)

                while(my_following >= random.randrange(800, 1000)):
                    session.set_dont_unfollow_active_users(enabled=True, posts=5)				
                    ct = 0
                    if ctt == 1:
                        ct += 1
                        print('Tens muitos seguidores 1')
                        print('Unffolowing')
                        time.sleep(random.randrange(2, 5))							
                        if(ct >= random.randrange(1, 4)):
                            session.unfollow_users(amount=60, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=90*60*60, sleep_delay=501)
                    if ctt == 2:
                        ct += 1
                        print('Tens muitos seguidores 2')
                        print('Unffolowing')
                        time.sleep(random.randrange(2, 5))							
                        if(ct >= random.randrange(1, 4)):
                            session.unfollow_users(amount=random.randrange(10, 20), nonFollowers=True, style="RANDOM", unfollow_after=42*60*60,sleep_delay=random.randrange(100, 250))																				
            likeByLocations()
            abc = random.randrange(1, 5)
            if abc == 1:
                print("Welcome to func n 1")
                print("do job")
                followByUserFollowers()
                ct = random.randrange(1, 4)
                if(ct == 1):
                    print("wildcard1")
                    followComenters()
                if(ct == 2):
                    print("wildcard2")
                    likeByTimeline()
                time.sleep(1)
                print(abc)
            elif abc == 2:
                print("Welcome to func n 2")
                print("do job")
                likeByTags()
                ct = random.randrange(1, 4)
                if(ct == 1):
                    print("wildcard2.1")
                    session.set_simulation(enabled=True, percentage=random.randrange(30,90))
                    followComenters()
                if(ct == 2):
                    print("wildcard2.2")
                    time.sleep(random.randrange(500, 2000))
                time.sleep(1)
                print(abc)
            elif abc == 3:
                print("Welcome to func n 3")
                print("do job")
                followByUserLikers()
                ct = random.randrange(1, 4)
                if(ct == 1):
                    print("wildcard3.1")
                    likeByTags()
                if(ct == 2):
                    print("wildcard3.2")
                    likeByTimeline()
                time.sleep(1)
                print(abc)
            elif abc == 4:
                print("Welcome to func n 4")
                print("do job")
                likeByTimeline()
                time.sleep(1)
                print(abc)
            else:
                continue

        else:
            if(login):
                login = False
                print(login)
                session.end()
                exit()
            print("sleeping")
            print(time.strftime("%H"))
            time.sleep(1)
except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    session.end()
