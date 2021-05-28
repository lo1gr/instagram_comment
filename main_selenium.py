from giveaway_util import GiveawayActions
from user_password import user_password, tag_friends
import itertools

from time import time

user = list(user_password)[3]
pw = user_password[user]

list_iter = [0,1]

cur_time = time()

for element in itertools.cycle(list_iter):
    user = list(user_password)[element]
    pw = user_password[user]
    friends_el = tag_friends[element]
    GiveawayActions(data = "CPTezvzhd8x", user=user,password=pw, tag_friends=friends_el).launch()
    if time() - cur_time > 7000:
        break

print("Done successfully")
