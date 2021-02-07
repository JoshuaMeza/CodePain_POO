# Requirements mapping

## Functional requirements

- **API** capable of:

  - [x] Always is active.
  - [x] Have an accessible database of official offensive words.
  - [x] Have a method to retrieve information from the database.

- **Discord bot** capable of:

  - [x] Always is active.
  - [x] Get Discord messages.
  - [x] Ban automatically.
  - [x] Get information from the API.
  - [x] The bot has space for memory.
  - Manage commands:
    - [x] Send word requests.
    - [x] Provide penalties management.
    - [x] Provide user stories management.
    - [x] Provide API information.
    - [x] Send error or bug messages found by the community.
  - Being customized:
    - [x] Grant usage permissions.
    - [x] _Penalize_ or _No penalize_ mode.
    - [x] Add and delete self-selected offensive words to censor them.
    - [x] Ignore self-selected words.
    - [x] Manage a whitelist.
  - Send default Discord messages for:
    - “In-server” configuration which:
      - Can send user history as:
        - [x] Individual user story.
      - Help command which:
        - [x] Show commands.
        - [x] Can give you the documentation page.
    - [x] Warning messages.
    - [x] Ban messages.
    - [x] Warning alerts for RudeBot Managers.
    - [x] Ban alerts for RudeBot Managers.
  - Can clean user history of:
    - [x] Individual user.
    - [x] All users.

- **Database** capable of:

  - [x] Always is active.
  - [x] Store API information.
  - [x] Store requests.
  - [x] Store custom server settings.

## Non functional requirements

- [x] The maximum amount of warnings until someone can get banned is five.
- [x] The maximum number of requests per user every month is five.
- [x] The request period is one month.
- [x] The review period is three days. Once it is finished, everyone can request again.
- [x] Existing words cannot be suggested.
- [x] The bot can only unban and clean history if a RudeBot Manager asks for it.
- [x] A guild can have up to 15 custom words.
- [x] A guild can have up to 15 ignored words.
- [x] A guild can have up to 10 users in their whitelist.
- [x] A user can send a bug report every 24 hours.

## Advancements summary

In the first deployment, the team worked on preparing all the documentation and investigation needed to start working on the project.

In the second deployment, all the team members got individual tasks to make the developing process faster and more flexible. When ones were working on something, the rest were practicing and learning to be ready. The principal objective at first was creating the API and the part of the database needed for their correct and complete functionality. Then, the team started developing the bot and searching how to make it work for everyone. Also, while creating the bot, some desired functionalities were completely discarded because of using methods which can easily fail, make the program slower, unnecessary ones, and very ambitious for the given amount of time, for example, the Rude Management Page.

In the third deployment, the team got finished the first version of the bot. While creating it some requirements appeared and other ones, for lack of time, were removed for getting a smoother final product.

## Mapping

The API is complete and has every requirement finished.

The bot, when landing on a server, creates their work environment. It can read messages and delete them if they contain an _offensive word_ registered in the Database, and then send to the user a warning message. Is planned to create an algorithm to detect variations for the next deploy. The bot can also execute the command "!help" and simulate (because the add to database module and that section of it hasn't been developed yet) the requests command. And finally, it has been hosted and is always working.

The database is designed for working with the API, but it is still missing the part for server custom settings.

The structure changed for addapting it into a MVC model. All commands now forms part of controller directory. As a bot doesn't has something as a GUI, it is not necessary to include a view directory. The dabase and saver (for memory management) are founded in model directory. Main file guides the initialization and work proccess of the bot.

Most of the requirements can be found spread over the commands files.

[<- Return to index](../README.md)
