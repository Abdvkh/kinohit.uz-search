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
2. Enter command code(e.g. 's' - to search)
3. Enter type of movie(e.g. serials)
4. How many pages it should go through
5. Details for search(if you pass Комедия all the films containing this word will be returned)

### Example
`python search.py`

```
========== INTERFACE ==========
Welcome to kinohit.uz searching engine!
Use command during the program:
[s]earch - to start searching
[q]uit - to quit the program

Enter the command of the program: s
Enter type of movies. Available now: films, serials, cartoons
>cartoons
How many pages do you want us to through?
>4
Details the film include, add by comma. For example: Комедия, Драма.
>6+, Супер
========== RESULTS START ==========

Name: Супер Пёс и Турбо Кот
Description: Запущенный в космос его владельцем ученым в 1969 году, верный пёс Бадди терпит крушение в наши дни в небольшом городке, ...
Categories: Фэнтези Комедия Мультфильм Семейный
Link: 'https://kinohit.uz/russian-film-kino-tasix-tas-uz-uzbekistan/fentezi/16846-super-pes-i-turbo-kot.html'
Age: 6+
Ratings: IMDb - 7.2 Kinopoisk - 0
Quality: SD


Name: Форма голоса
Description: Молодой человек Сёя Исида внезапно осознаёт, что в школе умудрился превратить жизнь одноклассницы Сёко в ад только потом...
Categories: Аниме Мультфильм
Link: 'https://kinohit.uz/russian-film-kino-tasix-tas-uz-uzbekistan/anime/16803-forma-golosa.html'
Age: 16+
Ratings: IMDb - 8.2 Kinopoisk - 8.0
Quality: SD

Name: Риф. Новые приключения
Description: Это захватывающая и смешная история отважного Алекса — рыбы-попугая, который мечтает стать Супергероем. Он получает свои...
Categories: Мультфильм Приключения
Link: 'https://kinohit.uz/russian-film-kino-tasix-tas-uz-uzbekistan/multfilm/16610-rif-novye-priklyucheniya.html'
Age: 0+
Ratings: IMDb - 4.3 Kinopoisk - 0
Quality: SD
...
```
Let's observe results:
1. "Супер Пёс и Турбо Кот" - coincidence in 'Age'
2. "Форма голоса" - coincidence in 'Age'
3. "Риф. Новые приключения" - coincidence in 'Description'


My telegram for feedback: https://t.me/Abduvakhidov
