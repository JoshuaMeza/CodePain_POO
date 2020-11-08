# Requirements definition

## System actors

- The User
- The API
- The Discord bot
- The Rude Management page

## User requirements

The user can add the bot to a Discord chat to filter it and prevent the use of the saved *negative words*, and also can add a personal list of banned words. If anyone want, they can ask to the bot for the web page *Rude Management* where they can make requests to add words, delete words and vote the actual requests.   

## System requirements

The API has the property of being modified **only** by the *requests system*, which is connected to the web page and is administrated by the community via requests and votes. The bot is always conected to the API and always give the source of the page if the user want it.

## Functional requirements

- The bot can be added and kicked of any discord chat.
- The bot can be temporally disabled.
- The user can add and delete new personal prohibited words.
- The user can make the bot to ignore words of the *negative words* list.
- The user can change the name of the bot.
- The user can give special permissions to the bot.
- The bot can give the link to the Rude Management page and the documentation.
- The bot can give warnings, and the user decide how much are necessary to ban a user.
- The user can clean the warnings history of another user or all users.
- Anyone can retrieve the *negative words* list of the API.
- The users can make requests to add an delete words in the API.
- The users can vote the actual requests to help them to being implemented or discarded.
- The users can send an email to the developers.

## Non functional requirements

- The maximum number of words added in the API per two weeks is four.
- The maximum number of words deleted in the API per two weeks is one.
- The bot has to check every message in less than a second.
- The default amount of necessary warnings until banning a user is five.

## User stories

- Discord bot
    - As a user, I can add the bot in any Discord chat.
    - As a user, I can kick the bot of any Discord chat.
    - As a user, I can temporally disable the bot in any Discord chat.
    - As a user, I can add personal prohibited words.
    - As a user, I can delete personal prohibited words.
    - As a user, I can make the bot to ignore words of the API.
    - As a user, I can change the name of the bot.
    - As a user, I can give special permissions to the bot.
    - As a user, I can ask to the bot the Rude Management page.
    - As a user, I can ask to the bot the documentation (Github repository).
    - As a user, I can decide how many warnings a user can have after being banned.
    - As a user, I can clean the entire warnings history or a personal one.
- API
    - As a user, I can retrieve all the *negative words* list.
- Rude Management page
    - As a user, I can make a request to add a *negative word*.
    - As a user, I can make a request to delete a *negative word*.
    - As a user, I can vote another request to make it succed or fail.
    - As a user, I can send a mail to the developers.

## Use cases diagram

<img src="https://github.com/JoshuaMeza/CodePain_POO/blob/master/Resources/tempBox.png" alt="Use cases diagram" width="100px" height="100px">

## UML diagram

<img src="https://github.com/JoshuaMeza/CodePain_POO/blob/master/Resources/tempBox.png" alt="UML diagram" width="100px" height="100px">
