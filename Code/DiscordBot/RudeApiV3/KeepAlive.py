"""
Code from freeCodeCamp:
https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
01/01/20201
Version 1.0.0
Used to maintain alive the bot
"""
from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    """
    This function returns a message when you enter to the main route
    Args:
        Nothing
    Returns:
        Nothing
    """
    return "Hello. I am alive!"


def run():
    """
    This function initializes a server
    Args:
        Nothing
    Returns:
        Nothing
    """
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    """
    This function starts the server
    Args:
        Nothing
    Returns:
        Nothing
    """
    t = Thread(target=run)
    t.start()
    