# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/SaitamaRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 7232694  # integer value, dont use ""
    API_HASH = "959d9ed64a5fb41ba3418248ff1fd835"
    TOKEN = "5016945112:AAE0JoU0Z94GpaGPzSuglqrPpvdIzHbWpAM"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1538405771  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "ribochan"
    SUPPORT_CHAT = "OnePunchSupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001764710818
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001799411291
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:z61TTTIuoNNgqdldZ8Ge@containers-us-west-26.railway.app:6587/railway"  # needed for any database modules # its "URI" and not "URL" as heroku and similar ones only accept it as such
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "LK53RBG7R1WU80RY"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "FILUWCH5L9F4"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ALLOW_CHATS="Onepunchrobot"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
