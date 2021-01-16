# What is this project
RudeApi is a profanity filtering service currently available for Discord but easily exportable to other platforms.

**@Author** CodePain Team


**@Date** 01/01/2021


**@Version** 1.2.0


# Getting started
**Step 1:**
```
$ pip install
```
**Step 2:**
```
create the .env file with the param keys
TOKEN = you_token_here
```
**Step 3:**
```
$ python3 main.py
```
# UML

<img src="https://raw.githubusercontent.com/JoshuaMeza/CodePain_POO/master/Resources/uml.jpg" alt="uml" width="100%" height="80%">

# Documentation

### main.py
> When the bot gets activated, this function prints a message
```
@client.event
async  def  on_ready():
```

> This function creates a channel and a role for managing the bot.
Args:
guild (object): Server
flag (bool): Used to know if create or not
role (class): Represents a role
temp (class): Discord client
overwrites (tupple): Save permissions
Returns:
Nothing
```
@client.event
async  def  on_guild_join(guild):
```

> This function gets activated when a user send a message
Args:
message (object): Represents the message
search (object): Searcher object
Returns:
Nothing

```
@client.event
async  def  on_message(message):
```


>This function sends a temporal message if a user tries to use an unknown command
Args:
ctx (object): Context
error (object): Error found
Returns:
Nothing
```
@client.event
async  def  on_command_error(ctx, error):
```

### KeepAlive.py
>Creathe the default route of flask
Args:
nothing
Return:
just a string
```
@app.route('/')
def  home():
```
>this just run the server in a specific host and port
Args:
nothing
Return:
nothing  
```
def  run():
  ```
>Start a thread to keep the connection with the sockets
Args:
nothing
Return:
nothing  
```
def  keep_alive():
```

### Searcher.py
>Constructor of the searcher
Args:
connector object 
Return:
nothing
```
def  __init__(self, connector):
```

>Start a thread to keep the connection with the sockets
Args:
the text that send the user
Return:
true or false if contain a profanity
```
def  searchWord(self, text):
```
### Saver.py

>Constructor of the Saver
Args:
nothing
Return:
nothing
```
def  __init__(self):
```

>handles all processes and returns a flag, serves to save information
Args:
userId
Return:
true or false is the process was ok
```
def  addRequest(self, userId):
```
>check if the user exists in the user list
Args:
userId
Return:
0 if isn't in the list or an array of all the request
```
def  verify(self, userId):
```
>add request to user 
Args:
userId
Return:
nothing

```
def  addLog(self, userId):
```
 
>increase the times that an user try a request
Args:
userId
Return:
nothing
```
def  increaseTimes(self, userId):
```

### Connector.py
>default constructor for connector, this just start some variables
Args:
nothing
Return:
nothing
```
def  __init__(self):
```
>get the bad word from the server and apped all to an array.
Args:
nothing
Return:
nothing
```
def  getWords(self):
```
>get the array of bad words
Args:
nothing
Return:
array of words
```
def  returnWords(self):
```

### CommandRequest.py
>constructor of CommandRequest that create the client to run the bot and memory that containt the list of request
Args:
client and memory
Return:
nothing
```
def  __init__(self, client, memory):
```
>When the bot gets activated, this function prints a message
Args:
nothig
Return:
nothing
```
@commands.Cog.listener()
async def on_ready(self):
```
>When a user send a request, verifies if he can still doing it and then send it to the database
Args:
nothing
Return:
nothing
```
@commands.command(aliases=['REQUEST'])
@commands.has_role('Rudebot Manager')
async def request(self, ctx, *, msg=""):
```
>This load the extension
Args:
nothing
Return:
nothing
```
def  setup(client):
```

### CommandHelp.py
> constructor of CommandHelp that initilize the client
Args:
nothing
Return:
nothing
```
def  __init__(self, client):
```
>When the bot gets activated, this function prints a message
Args:
nothing
Return:
nothing
```
@commands.Cog.listener()
async  def  on_ready(self):
```
>This method displays a help message
Args:
ctx (object): Context
embed (object): A Discord message type
arg (str): Argument
Returns:
Nothing
```
@commands.command(name='help', alisases=['HELP', 'info', 'INFO'])
@commands.has_role('Rudebot Manager')
async  def  command_help(self, ctx, *, arg=''):
```
>This load the extension
Args:
nothing
Return:
nothing
```
def  setup(client):
```