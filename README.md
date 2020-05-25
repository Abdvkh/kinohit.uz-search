# Searching engine for kinohit.uz
Command line search engine for kinohit.uz

## Setup
To make script start working you should install dependencies given in requirements.txt
This can be done thourh pip:
`pip install -r requirements.txt`

These libraries are:
- requests
- beautifulsoup4

## Usage
1. In command line you run 'search.py'
2. Enter type of movie(e.g. serials)
3. How many pages it should go through
4. Details for search(if you pass Комедия all the films containing this word will be returned)

### Example
>Enter type of movies. Available now: films, serials\
>\>serials\
How many pages do you want us to through?\
>\>2\
Details the film include: Комедия
>
>Name: Соник Х\
Description: Адаптация знаменитой видеоигры компании Sega....\
Categories: Аниме  Мелодрама  Боевик  Комедия  Мультфильм\
Link: 'https://kinohit.uz/serialy-na-russkom-v-tasix/16860-sonik-h.html' \
>Last episode: 26 серия 3 сезон
>
>Name: Великая\
Description: Молодая дочь немецкого князя София Августа Фредерика Ангальт...\
Categories: Исторический  Комедия\
Link: 'https://kinohit.uz/serialy-na-russkom-v-tasix/16851-velikaya.html' \
Last episode: 10 серия 1 сезон
>
>...






My telegram for feedback: t.me/Abduvakhidov
