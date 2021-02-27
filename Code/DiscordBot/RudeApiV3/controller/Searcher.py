"""
Author CodePain Team
Date 14/01/2021
Version 1.0.3
Searcher tool
"""


class Searcher:
    def __init__(self, memory, formatter):
        """
        This is a constructor
        """
        self.words = memory.getWordsList()
        self.custom = memory.getCustomDict()
        self.ignore = memory.getIgnoredDict()
        self.whitelist = memory.getWhiteList()
        self.formatter = formatter
        self.variants = {
            'A': ('4', '@'),
            'B': ('8'),
            'C': ('[', '{', 'K', 'Q'),
            'D': (),
            'E': ('3'),
            'F': ('7'),
            'G': ('6', '9'),
            'H': (),
            'I': ('1', '|', 'L', '!', '¡'),
            'J': (),
            'K': ('C', 'Q'),
            'L': ('1', '|', 'I', '!', '¡'),
            'M': (),
            'N': (),
            'O': ('0', '*', '°', '@'),
            'P': (),
            'Q': ('K'),
            'R': (),
            'S': ('5'),
            'T': ('7', '+'),
            'U': ('V'),
            'V': ('U'),
            'W': (),
            'X': (),
            'Y': (),
            'Z': ('7')
        }

    def searchWord(self, text, guildId):
        """
        This method verifies if a word in the text is already in the list
        Args:
            self (object): The object itself
            text (str): A text
            splittedText (list): Words from the text separated by spaces
            words (list): Banned words
            flag (bool): Verifies if the word was found
            word (str): Word in text
            newWord (str): Word in upper case
            swering (str): Word in banned words list
        Returns:
            True if that word exist in the list, False if not
        """
        splittedText = text.split(' ')
        flag = False

        for word in splittedText:
            newWord = word.upper()
            if self.words is not None:
                for swering in self.words:
                    if self.searchIgnore(newWord, guildId):
                        continue
                    elif self.searchAlgorithm(newWord, swering) or self.searchCustom(newWord, guildId):
                        flag = True
                        break
                if flag:
                    break

        return flag

    def searchCustom(self, word, guildId):
        """
        This method searches for custom words
        Args:
            self (object): The object itself
            word (str): Word to verify
            guildId (int): Guild ID
            flag (bool): Success flag
            custom (dict): Custom words dictionary
            item (str): Word in the custom list
        Returns:
            True if that word exist in the list, False if not
        """
        flag = False

        for item in self.custom[str(guildId)]:
            if word == item or self.searchAlgorithm(word, item):
                flag = True
                break

        return flag

    def searchIgnore(self, word, guildId):
        """
        This method searches for ignored words
        Args:
            self (object): The object itself
            word (str): Word to verify
            guildId (int): Guild ID
            flag (bool): Success flag
            ignore (dict): Ignore words dictionary
            item (str): Word in the ignored list
        Returns:
            True if that word exist in the list, False if not
        """
        flag = False

        for item in self.ignore[str(guildId)]:
            if word == item or self.searchAlgorithm(word, item):
                flag = True
                break

        return flag

    def verifyUser(self,  userId, guildId):
        """
        This method verifies if a user is on the whitelist
        Args:
            self (object): The object itself
            userId: (int): User ID
            user (str): User ID in whitelist
            whitelist (dict): Whitelist dictionary
        Returns:
            True if they is on it, False if not
        """
        flag = False

        for user in self.whitelist[str(guildId)]:
            if str(userId) == user:
                flag = True
                break

        return flag

    def searchAlgorithm(self, wordOne, wordTwo):
        """
        This method does the search
        Args:
            self (object): The object itself
            wordOne (str): Word one
            wordTwo (str): Word two
            result (bool): The result
            stack (list): A stack for removing repeated words
            check (list): The word to examine
            length (int): The length of the word
            sameChars (int): The amount of equal chars
            lengthFlag (bool): Flag for preventing out of index exception
            i (int): Iterator
            previousLetter (str): Previous letter
            letter (str): Actual letter
            key (str): Dictionary key value
            j (int): Iterator
            percentage (float): Equality percentage
        Returns:
            True if equal or similar, False if not
        """
        result = False
        wordTwo = self.formatter.formatWord(wordTwo)
        stack = []
        check = self.cut(self.formatter.formatWord(wordOne))
        length = len(check)
        sameChars = 0
        lengthFlag = True
        i = 0

        # Analize
        if length > 0:
            previousLetter = None
            for letter in wordTwo:
                if lengthFlag:
                    # Contractions
                    if previousLetter is not None:
                        if previousLetter == 'C' and letter == 'K' and (check[i] != letter and not any(var == check[i] for var in self.variants[letter])):
                            previousLetter = None
                            stack = ['K']
                            sameChars += 1
                            continue

                    # Start or end with symbols
                    if i == 0:
                        if letter != 'I' and letter != 'L' and (check[i] == '¡' or check == '¿'):
                            i += 1
                            length -= 1

                            if i >= length:
                                lengthFlag = False
                    elif i == length - 1:
                        if letter != 'I' and letter != 'L' and (check[i] == '!' or check == '?'):
                            i += 1
                            length -= 1
                            lengthFlag = False

                    # Repeated words
                    if len(stack) != 0 and lengthFlag:
                        if letter != stack[0] and letter != check[i]:
                            while lengthFlag and (check[i] == stack[0] or any(var == check[i] for var in self.variants[stack[0]])):
                                i += 1
                                sameChars += 1

                                if i >= length:
                                    lengthFlag = False

                    # Stack saving
                    if len(stack) > 0:
                        stack.pop(0)

                    if lengthFlag:
                        for key in self.variants:
                            if check[i] == key or any(var == check[i] for var in self.variants[key]):
                                # What do I expect to find? (groups with things in common)
                                if key == 'I' or key == 'L':
                                    if letter == 'I' or letter == 'L':
                                        stack.append(letter)
                                        check[i] = letter
                                elif key == 'U' or key == 'V':
                                    if letter == 'U' or letter == 'V':
                                        stack.append(letter)
                                        check[i] = letter
                                elif key == 'C' or key == 'K' or key == 'Q':
                                    if letter == 'C' or letter == 'K' or letter == 'Q':
                                        stack.append(letter)
                                        check[i] = letter
                                # Not a special case
                                else:
                                    stack.append(key)
                                    check[i] = key
                                break

                    # Compare
                    if lengthFlag and letter == check[i]:
                        sameChars += 1

                    # Exit
                    i += 1
                    if i >= length:
                        lengthFlag = False
                    previousLetter = letter

            # Clean again with updated stack and special cases
            if len(stack) != 0 and lengthFlag:
                while lengthFlag and (check[i] == stack[0] or any(var == letter for var in self.variants[stack[0]])):
                    i += 1
                    sameChars += 1

                    if i >= length:
                        lengthFlag = False

            if lengthFlag:
                j = length - 1

                while j >= i:
                    if check[j] == '!' or check[j] == '?':
                        length -= 1
                        j -= 1
                    else:
                        break

                if check[i] == 'S':
                    sameChars += 1

            # Equality percentage
            if len(wordTwo) > length:
                percentage = float(sameChars)/len(wordTwo)
                if len(wordTwo) < 5 and percentage >= 0.75:
                    result = True
                elif percentage >= 0.8:
                    result = True
            else:
                percentage = float(sameChars)/length
                if length < 5 and percentage >= 0.75:
                    result = True
                elif percentage >= 0.8:
                    result = True

        return result

    def cut(self, word):
        """
        Transforms a string into a list of characters
        Args:
            self (object): The object itself
            word (str): A string
            char (str): Every char in the string
        Returns:
            A list of chars
        """
        return [char for char in word]
