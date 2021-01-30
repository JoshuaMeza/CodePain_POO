"""
Author CodePain Team
Date 14/01/2021
Version 1.0.1
Connector tool
"""
import requests
import json
import mysql.connector
import os
from dotenv import load_dotenv


class Connector:
    def __init__(self):
        """
        This is a constructor
        """
        self.url = 'http://zivotmagazine.net/Pruebas/getAll.php'
        self.words = []
        self.getWordsAPI()

    def getWordsAPI(self):
        """
        This method gets all the words from the api and save them into the list called words
        Args:
            self (object): The object itself
        Returns:
            Nothing
        """
        try:
            response = requests.get(self.url)
            temp = json.loads(response.content)
            for category in temp:
                for word in temp[category]:
                    self.words.append(word)
        except:
            self.words = None

    def returnWordsList(self):
        """
        This method returns the words list
        Args:
            self (object): The object itself
        Returns:
            The words list
        """
        return self.words

    def sendRequest(self, word, languageId):
        """
        This method sends a word request to the database
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "INSERT INTO `{}`.`RequestedWords` (`word`,`languageId`) VALUES ('{}',{});".format(
                os.getenv('DBNAME'), word, languageId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def sendBugReport(self, text, guildId):
        """
        This method sends a bug report to the database
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "INSERT INTO `{}`.`Bugs` (`Comment`,`idGuildBugs`) VALUES ('{}',{});".format(
                os.getenv('DBNAME'), text, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def addCustomWord(self, word, guildId):
        """
        This method adds a new custom word for a guild
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "INSERT INTO `{}`.`CustomWords` (`word`,`guildIdCW`) VALUES ('{}',{});".format(
                os.getenv('DBNAME'), word, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getCustomWords(self):
        """
        This method gets all the custom words
        Args:
        Returns:
        """
        output = []

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "SELECT word,guildIdCW FROM `{}`.`CustomWords`;"

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            output = mycursor.fetchall()

            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getCustomWordsOfGuild(self, guildId):
        """
        This method gets the custom words of a given guild
        Args:
        Returns:
        """
        output = []

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "SELECT word FROM `{}`.`CustomWords` WHERE guildIdCW={};".format(
                guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            output = mycursor.fetchall()

            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def removeCustomWord(self, word, guildId):
        """
        This method removes a custom word of a guild
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "DELETE FROM `{}`.`CustomWords` WHERE word='{}' and guildIdCW={};".format(
                os.getenv('DBNAME'), word, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def recordGuild(self, guildId):
        """
        This method adds new guild to the database
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "INSERT INTO `{}`.`Guilds` (`idGuilds`,`penalizeMode`) VALUES ({},1);".format(
                os.getenv('DBNAME'), guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def searchGuild(self, guildId):
        """
        This verifies if a guild exists in the database
        Args:
        Returns:
        """
        output = []

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "SELECT idGuilds FROM `{}`.`Guilds` WHERE idGuilds={};".format(
                os.getenv('DBNAME'), guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            output = mycursor.fetchone()

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getGuildsInfo(self):
        """
        This returns a list with every guild in database
        Args:
        Returns:
        """
        output = []

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "SELECT * FROM `{}`.`Guilds`;".format(
                os.getenv('DBNAME'))

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            output = mycursor.fecthall()

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def setPenalizeMode(self, guildId, decision):
        """
        This method changes the penilize mode
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "UPDATE `{}`.`Guilds` SET penalizeMode={} WHERE idGuilds={};".format(
                os.getenv('DBNAME'), decision, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def addIgnoredWord(self, word, guildId):
        """
        This method adds a new ignored word of a guild
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "INSERT INTO `{}`.`Ignore` (`word`,`guildIdIg`) VALUES ('{}',{});".format(
                os.getenv('DBNAME'), word, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getIgnoredWords(self):
        """
        This returns a list with every ignored word
        Args:
        Returns:
        """
        output = []

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "SELECT word, guildIdIg FROM `{}`.`Ignore`;".format(
                os.getenv('DBNAME'))

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            output = mycursor.fecthall()

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getIgnoredWordsFromGuild(self, guildId):
        """
        This returns a list with every ignored word
        Args:
        Returns:
        """
        output = []

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "SELECT word FROM `{}`.`Ignore` WHERE guildIdIg={};".format(
                os.getenv('DBNAME'), guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            output = mycursor.fecthall()

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def removeIgnoredWord(self, word, guildId):
        """
        This method removes an ignored word of a guild
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "DELETE FROM `{}`.`Ignore` WHERE word='{}' and guildIdIg={};".format(
                os.getenv('DBNAME'), word, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def addStory(self, userId, guildId):
        """
        This method adds a new story of a guild
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "INSERT INTO `{}`.`Stories` (`userId`,`warnings`,`guildIdSty`) VALUES ({},1,{});".format(
                os.getenv('DBNAME'), userId, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getUserStories(self):
        """
        This returns every story in database
        Args:
        Returns:
        """
        output = []

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "SELECT * FROM `{}`.`Stories`;".format(
                os.getenv('DBNAME'))

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            output = mycursor.fecthall()

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getUserStory(self, userId, guildId):
        """
        This returns the story of a user
        Args:
        Returns:
        """
        output = []

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "SELECT * FROM `{}`.`Stories` WHERE userId={} and guildIdSty={};".format(
                os.getenv('DBNAME'), userId, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            output = mycursor.fecthone()

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def setUserStoryAmount(self, userId, guildId, amount):
        """
        This method sets a new amount of warnings
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "UPDATE `{}`.`Stories` SET warnings={} WHERE userId={} and guildIdSty={};".format(
                os.getenv('DBNAME'), amount, userId, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def addUserToWhitelist(self, userId, guildId):
        """
        This method adds a new user to the whitelist of a guild
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "INSERT INTO `{}`.`Whitelist` (`idUser`,`idGuild`) VALUES ({},{});".format(
                os.getenv('DBNAME'), userId, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def removeUserOfWhitelist(self, userId, guildId):
        """
        This method removes a user from the whitelist of a guild
        Args:
        Returns:
        """
        output = False

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "DELETE FROM `{}`.`Whitelist` WHERE userId={} and guildIdIg={};".format(
                os.getenv('DBNAME'), userId, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output
