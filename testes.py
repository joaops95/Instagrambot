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
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import subprocess

# -------------------------------login credentials------------------------------------
insta_username = 'aztrepair'
insta_password = 'Azeitao2018'


# ----------------------------------InstaPy session------------------------------------

def appendCsv(data, csvfile):
    with open(csvfile, 'rt') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        for i in range(len(lines)):
            if(lines[i] == data):
                print('user ja existe na bd')
                readFile.close()
        else:
            with open('Users2.csv', 'a') as userlist:
                userlist.write('\n%s' % data)
            userlist.close()

appendCsv('joaops95', 'Users2.csv')
def readMyFile(filename):
    data = []
    with open(filename, 'rt') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row[0])
    return data


def setrelations(username, relationscsv):
        with urllib.request.urlopen('https://www.instagram.com/joaops95/') as response:
                relation = readMyFile(relationscsv)
                html = response.read()
                soup = BeautifulSoup(html, 'html.parser')
                soup = soup.get_text()
                end_name = soup.find('photos and videos')
                start_desc = soup.find(',"description":')
                end_desc = soup.find(',"mainEntityofPage":')
                soup = (soup[0:end_name] + soup[start_desc+16:end_desc-1])
                print(soup)
                ss = str(soup)
                ss.replace('\', ' ')
                print(ss)
                with open('lixo.txt', 'wt') as lixo:
                    lixo.write(soup)
                    lixo.close
                with open('lixo.txt', 'rt') as lixo:
                    string = lixo.read()
                    lixo.close

                    
                for word in readMyFile(relationscsv):
                    if(soup.find(word) == 11):
                        print(word)
                        print('segue essa merda')
                    else:
                        print('next')

relationwords = ['smart', 'tuned', 'touch', 'engineering']
setrelations('thesmartprojects', 'relations.csv')

'''
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False, multi_logs=True)
# ----------------------------------Supervisor------------------------------------

session.like_by_feed(amount=random.randrange(
        2, 32), randomize=True, unfollow=False, interact=False)

'''