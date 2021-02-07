"""
Author CodePain Team
Date 14/01/2021
Version 1.0.3
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
        self.url = 'http://www.zivotmagazine.net/NO-BORRAR/getAll.php'

    def getWordsAPI(self):
        """
        This method gets all the words from the api
        Args:
            self (object): The object itself
            words (list): The list of banned words
            url (str): API url
            response (bin): Information from the api
            temp (list): Response as json
            category (list): Lists inside the json
            word (str): Banned words
        Returns:
            The list of words
        """
        words = []

        try:
            response = requests.get(self.url)
            temp = json.loads(response.content)
            for category in temp:
                for word in temp[category]:
                    words.append(word)
        except:
            words = None

        return words

    def returnUrl(self):
        """
        This method returns the API url
        Args:
            self (object): The object itself
            url (str): API url
        """
        return self.url

    def sendRequest(self, word, languageId):
        """
        This method sends a word request to the database
        Args:
            self (object): The object itself
            word (str): Requested word
            languageId (int): Langage ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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
            self (object): The object itself
            text (str): Text of the report
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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
            self (object): The object itself
            word (str): A word to penalize
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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
            self (object): The object itself
            output (list): Result
            temp (list): Database information
            line (list): Database information
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            The list of custom words and their guild id
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

            sql = "SELECT word,guildIdCW FROM `{}`.`CustomWords`;".format(
                os.getenv('DBNAME'))

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            temp = mycursor.fetchall()

            if temp is not None:
                for line in temp:
                    output.append('{},{}'.format(line[1], line[0]))

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getCustomWordsOfGuild(self, guildId):
        """
        This method gets the custom words of a given guild
        Args:
            self (object): The object itself
            guildId (str): Guild's id
            output (list): Result
            temp (list): Database information
            line (list): Database information
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            The list of custom words of a guild
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

            sql = "SELECT word FROM `{}`.`CustomWords` WHERE guildIdCW={};".format(os.getenv('DBNAME'),
                                                                                   guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            temp = mycursor.fetchall()

            if temp is not None:
                for line in temp:
                    output.append('{}'.format(line[0]))

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def removeCustomWord(self, word, guildId):
        """
        This method removes a custom word of a guild
        Args:
            self (object): The object itself
            word (str): Custom word
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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

            sql = "DELETE FROM `{}`.`CustomWords` WHERE word='{}' and guildIdCW={} LIMIT 1;".format(
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
            self (object): The object itself
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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
            self (object): The object itself
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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

            sql = "SELECT idGuilds FROM `{}`.`Guilds` WHERE idGuilds={};".format(
                os.getenv('DBNAME'), guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            temp = mycursor.fetchone()

            if temp is not None:
                output = True

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getGuildsInfo(self):
        """
        This returns a list with every guild in database
        Args:
            self (object): The object itself
            output (list): Result
            temp (list): Database information
            line (list): Database information
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            A list with every guild and their settings
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

            temp = mycursor.fetchall()

            if temp is not None:
                for line in temp:
                    output.append(str(line)[1:][:-1])

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def setPenalizeMode(self, guildId, decision):
        """
        This method changes the penilize mode
        Args:
            self (object): The object itself
            decision (int): 1 for True and 0 for False
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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
            self (object): The object itself
            word (str): A word to ignore
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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
            self (object): The object itself
            output (list): Result
            temp (list): Database information
            line (list): Database information
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            The list of all ignored words and their guild id
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

            sql = "SELECT word,guildIdIg FROM `{}`.`Ignore`;".format(
                os.getenv('DBNAME'))

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            temp = mycursor.fetchall()

            if temp is not None:
                for line in temp:
                    output.append('{},{}'.format(line[1], line[0]))

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getIgnoredWordsFromGuild(self, guildId):
        """
        This returns a list with every ignored word
        Args:
            self (object): The object itself
            output (list): Result
            guildId (str): Guild's id
            temp (list): Database information
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            The list of ignored words of a guild
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

            temp = mycursor.fetchall()

            if temp is not None:
                for line in temp:
                    output.append('{}'.format(line[0]))

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def removeIgnoredWord(self, word, guildId):
        """
        This method removes an ignored word of a guild
        Args:
            self (object): The object itself
            word (str): Ignored word
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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

            sql = "DELETE FROM `{}`.`Ignore` WHERE word='{}' and guildIdIg={} LIMIT 1;".format(
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
        This method adds a new user story
        Args:
            self (object): The object itself
            userId (str): User's id
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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

    def getUserStories(self, guildId):
        """
        This method returns every story in database
        Args:
            self (object): The object itself
            output (list): Result
            guildId (str): Guild ID
            temp (list): Database information
            line (list): Database information
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            This list with the complete history
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

            sql = "SELECT * FROM `{}`.`Stories` WHERE guildIdSty={};".format(
                os.getenv('DBNAME'), guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            temp = mycursor.fetchall()

            if temp is not None:
                for line in temp:
                    output.append(str(line)[1:][:-1])

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getUserStory(self, userId, guildId):
        """
        This method returns the story of a user
        Args:
            self (object): The object itself
            userId (str): User's id
            guildId (str): Guild ID
            output (str): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            A string with the story of a user
        """
        output = None

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )

            sql = "SELECT warnings FROM `{}`.`Stories` WHERE userId={} and guildIdSty={};".format(
                os.getenv('DBNAME'), userId, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            temp = mycursor.fetchone()

            if temp is not None:
                output = str(temp[0])

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def setUserStoryAmount(self, userId, guildId, amount):
        """
        This method sets a new amount of warnings
        Args:
            self (object): The object itself
            userId (str): User's id
            amount (int): Amount of warnings
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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

    def resetGlobalStory(self, guildId):
        """
        This method resets the stories of every member of a guild
        Args:
            self (object): The object itself
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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

            sql = "UPDATE `{}`.`Stories` SET warnings=0 WHERE guildIdSty={};".format(
                os.getenv('DBNAME'), guildId)

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
            self (object): The object itself
            userId (str): User's id
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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

    def getWhiteList(self):
        """
        This method returns the whitelist
        Args:
            self (object): The object itself
            output (list): Result
            temp (list): Database information
            line (list): Database information
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            A list with the entire whitelist
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

            sql = "SELECT idUser,idGuild FROM `{}`.`Whitelist`;".format(
                os.getenv('DBNAME'))

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            temp = mycursor.fetchall()

            if temp is not None:
                for line in temp:
                    output.append('{},{}'.format(line[1], line[0]))

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def getWhiteListFromGuild(self, guildId):
        """
        This method returns the whitelist
        Args:
            self (object): The object itself
            output (list): Result
            userId (str): User's id
            temp (list): Database information
            line (list): Database information
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            The list of the whitelist of a guild
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

            sql = "SELECT idUser FROM `{}`.`Whitelist` WHERE idGuild={};".format(
                os.getenv('DBNAME'), guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            temp = mycursor.fetchall()

            if temp is not None:
                for line in temp:
                    output.append(line[0])

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def removeUserOfWhitelist(self, userId, guildId):
        """
        This method removes a user from the whitelist of a guild
        Args:
            self (object): The object itself
            userId (str): User's id
            guildId (str): Guild ID
            output (bool): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            True if success, False if not
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

            sql = "DELETE FROM `{}`.`Whitelist` WHERE idUser={} and idGuild={} LIMIT 1;".format(
                os.getenv('DBNAME'), userId, guildId)

            mycursor = mydb.cursor()
            mycursor.execute(sql)

            mydb.commit()
            mydb.close()
            output = True
        except Exception as e:
            print('Error: {}'.format(e))

        return output

    def countAmounts(self, guildId, selection):
        """
        This returns the amount of selected elements a guild has
        Args:
            self (object): The object itself
            selection (str): Which table you want to count
            guildId (str): Guild ID
            output (int): Result
            mydb (object): MySQL connection
            sql (str): A sql scrypt
            mycursor (object): Instantiates objects that can execute operations
        Returns:
            The amount of selected elements a guild has, if the guild does not has items,
            this method will return -1
        """
        output = -1

        try:
            load_dotenv()
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('DBUSER'),
                password=os.getenv('PASSW'),
                database=os.getenv('DBNAME')
            )
            flag = False
            sql = ""

            if (selection == 'Ignore'):
                sql = "SELECT COUNT(*) FROM `{}`.`{}` WHERE guildIdIg={};".format(
                    os.getenv('DBNAME'), selection, guildId)
                flag = True
            elif (selection == 'CustomWords'):
                sql = "SELECT COUNT(*) FROM `{}`.`{}` WHERE guildIdCW={};".format(
                    os.getenv('DBNAME'), selection, guildId)
                flag = True
            elif (selection == 'Whitelist'):
                sql = "SELECT COUNT(*) FROM `{}`.`{}` WHERE idGuild={};".format(
                    os.getenv('DBNAME'), selection, guildId)
                flag = True

            if (flag):
                mycursor = mydb.cursor()
                mycursor.execute(sql)

                temp = mycursor.fetchone()

                output = int(temp[0])

            mydb.close()
        except Exception as e:
            print('Error: {}'.format(e))

        return output
