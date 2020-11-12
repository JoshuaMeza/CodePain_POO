# Requirements mapping

## Functional requirements

- **API** capable to:
    - [ ] Have an accessible database of oficial offensive words.
    - [ ] Have a method to search, add and delete words.
    - [ ] Record the actual top ten addition words and the amount of follow ups.
    - [ ] Record all requests made by users (cleaned after a month) and the amount of follow ups.
- **Discord bot** capable to:
    - [ ] Get Discord messages in real time.
    - [ ] Ban automatically.
    - [ ] Get all information of our database or API.
    - [ ] Send error or bug messages found by the community.
    - [ ] The bot has a space for memory.
    - Being customized:
        - [ ] Change of permissions.
        - [ ] *Active* or *Disabled* mode.
        - [ ] *Delete message* or *Censor message* mode.
        - [ ] *Penalize* or *No penalize* mode. 
        - [ ] Change the maximum amount of *Warnings*.
        - [ ] Add and delete self-selected offensive words to censor them.
        - [ ] Ignore self-selected words.
    - Send default Discord messages for:
        - [ ] Joining server.
        - “In-server” configuration which:
            - Can send user history as:
                - [ ] Individual user story.
                - [ ] List of all warned/banned people.
            -   Help command which:
                - [ ] Print commands
                - [ ] Can give you the documentation page.
                - [ ] Can give you the management page.
            - Follow management command:
                - [ ] Send the actual top ten and the amount of follow ups.
        - [ ] Warning messages.
        - [ ] Ban messages.
        - [ ] Weekly resume for admins.
        - [ ] Warning alerts for admins.
        - [ ] Ban alerts for admins.
    - Can clean user history of:
        - [ ] Individual user.
        - [ ] All users.
    - Can unban people by:
        - [ ] Individual user.
        - [ ] All banned users (just that ones that got banned by the bot).
- **Website** capable to:
    - [ ] Consume API & get saved information from a user.
    - [ ] Make modifications to the bot from the page.
    - [ ] Show the same information as: discord bot in-server configuration.
    - [ ] Have a submission box to suggest *offensive words*.
    - [ ]  Have a graphic that shows top 10 additions suggested of *offensive words*.
    - [ ] Log in / Register users (at least with discord).
    - [ ] Have a bot joining method.
    - [ ] Give the opportunity to the community to keep in touch with the developers (email address).
    - [ ] Show the last added words.
    - [ ] Shows all the words that are actually in the API.

## Non functional requirements

- [ ] The maximum amount of warnings until someone can get banned is default to five.
- [ ] The maximum number of requests per user every month is eight (suggestion points).
- [ ] The requests can not be the same words.
- [ ] The first time the user repeats a word, they will get a message and he will not lose any suggestion points, then, if he does the same thing, he will start losing their suggestion points.
- [ ] The request period is one month.
- [ ] The review period is three days, during this time anyone can suggest. Once is finished everyone refreshes their suggestion points.
- [ ] The top three is the only group of words that could be added.
- [ ] At the start of every request period, the past unselected top ten words will remain in the graphic with the twenty percent of the past votes.
- [ ] Anyone can follow up or suggest any word at the start of every period. Even if he selected the same word the past season.
- [ ] If an existent word is suggested, the page gives a warning to the user without any penalization.
- [ ] The bot can only unban and clean history if an administrator asks it.
- [ ] The database of the web page has to encrypt the data inside (for accounts). 

## Advancements summary

In the first deploy phase the team worked on preparing all the documentation needed to start working in the project.

## Mapping

There's any requirement done yet.


[<- Return to index](https://github.com/JoshuaMeza/CodePain_POO)
