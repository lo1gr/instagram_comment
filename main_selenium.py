from giveaway_util import GiveawayActions
from user_password import user_password

user = list(user_password)[3]
pw = user_password[user]

GiveawayActions(data = "CPTezvzhd8x", user=user,password=pw).launch()
