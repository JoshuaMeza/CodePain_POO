# How to access to the API?

If you want to know how the API works, you can check its documented code in the [Code/API](../Code/API) section

## If you want to recover all languages

You will need to consume the following link : http://zivotmagazine.net/NO-BORRAR/getAll.php

## If you want to recover the insults in Spanish

You will need to consume the following link : http://zivotmagazine.net/NO-BORRAR/getSpanish.php

## If you want to recover the insults in English

You will need to consume the following link : http://zivotmagazine.net/NO-BORRAR/getEnglish.php

## If you want to recover the insults in Mayan

You will need to consume the following link : http://zivotmagazine.net/NO-BORRAR/getMayan.php

## Python to get all words in all languages

You need to retrieve the content of the link with the help of the requests library, then with the help of the json library and its .loads () method, it will load the content of the link into a variable transforming it from json to a Python Object, which will represent an array where each word represents an index, if you want to give it a better visual format you can do it with the help of the json.dumps () method that receives as a parameter the array and the indentation to be applied.

YOU CAN CHOOSE A LANGUAGE IN THE ARRAY BY SPECIFYING THIS ONE

```python
import requests
import json
if __name__ == '__main__':
    url = 'http://zivotmagazine.net/NO-BORRAR/getAll.php'
    response= requests.get(url)
    words = json.loads(response.content)
    print(words['English'])
    print(json.dumps(words, indent=2))
```

YOU CAN CHOOSE A LANGUAGE IN THE ARRAY BY SPECIFYING BEFORE THE INDEX AND IN ADDITION THE INDEX OF THAT WORD FOR THIS LANGUAGE

```python
import requests
import json
if __name__ == '__main__':
    url = 'http://zivotmagazine.net/NO-BORRAR/getAll.php'
    response= requests.get(url)
    words = json.loads(response.content)
    print(words['English'][3])
    print(json.dumps(words, indent=2))
```

## Python to get all words in a language (change the url)

You need to retrieve the content of the link with the help of the requests library, then with the help of the json library and its .loads () method, it will load the content of the link into a variable transforming it from json to a Python Object, which will represent an array where each word represents an index, if you want to give it a better visual format you can do it with the help of the json.dumps () method that receives as a parameter the array and the indentation to be applied

```python
import requests
import json

if __name__ == '__main__':
    url = 'http://zivotmagazine.net/NO-BORRAR/getSpanish.php'
    response= requests.get(url)
    words = json.loads(response.content)
    print(words)
    print(json.dumps(words, indent=2))

```

## Python to get a specific word (change the url)

Using the above code, you just need to specify the index of the word within the array

```python
import requests
import json

if __name__ == '__main__':
    url = 'http://zivotmagazine.net/NO-BORRAR/getSpanish.php'
    response= requests.get(url)
    words = json.loads(response.content)
    print(words[3])

```

[<- Return to index](../README.md)
