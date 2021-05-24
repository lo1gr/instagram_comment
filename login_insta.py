# This code was extracted from another project: https://github.com/arc298/instagram-scraper
import warnings
import threading
import concurrent.futures
import requests
import tqdm
import json

import hashlib
import logger

import logging.config
import sys
import argparse

default_random_ua = "Mozilla/5.0 (iPhone; U; ru; CPU iPhone OS 4_2_1 like Mac OS X; ru) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5"
BASE_URL = 'https://www.instagram.com/'
LOGIN_URL = BASE_URL + 'accounts/login/ajax/'
STORIES_UA = 'Instagram 123.0.0.21.114 (iPhone; CPU iPhone OS 11_4 like Mac OS X; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/605.1.15'


def get_logger(level=logging.DEBUG, dest='', verbose=0):
    """Returns a logger."""
    logger = logging.getLogger(__name__)

    dest +=  '/' if (dest !=  '') and dest[-1] != '/' else ''
    fh = logging.FileHandler(dest + 'instagram-log.log', 'w')
    fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    fh.setLevel(level)
    logger.addHandler(fh)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    sh_lvls = [logging.ERROR, logging.WARNING, logging.INFO]
    sh.setLevel(sh_lvls[verbose])
    logger.addHandler(sh)

    logger.setLevel(level)

    return logger


logger = get_logger(level=logging.DEBUG, dest='', verbose=True)



def authenticate_with_login(login_user, login_pass, random_ua = default_random_ua, verbose = True):
        """Logs in to instagram."""

        session = requests.Session()
        session.headers.update({'Referer': BASE_URL, 'user-agent': STORIES_UA})
        req = session.get(BASE_URL)

        session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})

        login_data = {'username': login_user, 'password': login_pass}
        login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
        session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        cookies = login.cookies
        login_text = json.loads(login.text)

        if login_text.get('authenticated') and login.status_code == 200:
            authenticated = True
            logged_in = True
            session.headers.update({'user-agent': random_ua})
            rhx_gis = ""
            if verbose:
                logger.info('Login success for ' + login_user)
        else:
            logger.error('Login failed for ' + login_user)

            return None
        
        return session, cookies

rhx_gis = ""
def get_ig_gis(rhx_gis, params):
    data = rhx_gis + ":" + params
    if sys.version_info.major >= 3:
        return hashlib.md5(data.encode('utf-8')).hexdigest()
    else:
        return hashlib.md5(data).hexdigest()


