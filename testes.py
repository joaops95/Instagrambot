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

import logging
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
)
# -------------------------------login credentials------------------------------------
insta_username = 'joaops95'
insta_password = 'jpjcs3595'

# ----------------------------------InstaPy session------------------------------------
getattr(logging, loglevel.upper())
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False, multi_logs=True)
# ----------------------------------Supervisor------------------------------------

session.like_by_feed(amount=random.randrange(
        2, 32), randomize=True, unfollow=False, interact=False)

