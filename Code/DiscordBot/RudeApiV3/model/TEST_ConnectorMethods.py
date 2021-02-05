"""
Author Joshua Meza
02/02/2021
Temporary file for testing the Connector and helping the team with the commands.
"""
from Connector import *

def main():
    con = Connector()
    temp = []

    # Method calling:
    """
    print(con.sendRequest('test',1))
    print(con.sendBugReport('The request system does not send anything >:(','794783492197187587'))
    print(con.addCustomWord('Psyco','794783492197187587'))
    temp = con.getCustomWords()
    temp = con.getCustomWordsOfGuild('794783492197187587')
    print(con.removeCustomWord('Psyco','794783492197187587'))
    print(con.recordGuild('123'))
    print(con.searchGuild('123'))
    temp = con.getGuildsInfo()
    print(con.setPenalizeMode('794783492197187587',1))
    print(con.addIgnoredWord('Crazy','794783492197187587'))
    temp = con.getIgnoredWords()
    temp = con.getIgnoredWordsFromGuild('794783492197187587')
    print(con.removeIgnoredWord('Psyco','794783492197187587'))
    print(con.addStory('123','794783492197187587'))
    temp = con.getUserStories()
    temp = con.getUserStory('123','794783492197187587')
    print(con.setUserStoryAmount('123','794783492197187587',5))
    print(con.addUserToWhitelist('123','794783492197187587'))
    temp = con.getWhiteList()
    temp = con.getWhiteListFromGuild('794783492197187587')
    print(con.removeUserOfWhitelist('123','794783492197187587'))
    print(con.countAmounts('794783492197187587','Ignore'))
    print(con.countAmounts('794783492197187587','CustomWords'))
    print(con.countAmounts('794783492197187587','Whitelist'))
    print(con.countAmounts('794783492197187587','test'))
    """

    for x in temp:
        print(x)
    

if __name__ == '__main__':
    main()