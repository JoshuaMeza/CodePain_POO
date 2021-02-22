"""
Author CodePain Team
Date 21/02/2021
Version 1.0.0
Formatter tool
"""


class Formatter:
    def __init__(self):
        """
        This is a constructor
        """
        self.ignore = ('.', '_', '~', '\'', '`', '¨', '´',
                       '"', ',', '^', '-', '<', '>', '¬', '=', ':', ';')

    def formatWord(self, word):
        """
        This function gives a format to the word
        Args:
            self (object): The object itself
            word (str): A string
            verifiedWord (str): The formatted word
            ignore (tuple): Group of ignored characters in the formatting
            letter (str): A letter of the word
        Returns:
            A formatted word
        """
        verifiedWord = ''

        for letter in word:
            if letter == 'Ñ':
                verifiedWord += 'NI'
            elif letter == 'Á' or letter == 'Ä':
                verifiedWord += 'A'
            elif letter == 'É' or letter == 'Ë':
                verifiedWord += 'E'
            elif letter == 'Í' or letter == 'Ï':
                verifiedWord += 'I'
            elif letter == 'Ó' or letter == 'Ö':
                verifiedWord += 'O'
            elif letter == 'Ú' or letter == 'Ü':
                verifiedWord += 'U'
            elif any(char == letter for char in self.ignore):
                continue
            else:
                verifiedWord += letter

        return verifiedWord
