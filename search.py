try:
    import requests
    from bs4 import BeautifulSoup as BS
except ModuleNotFoundError:
    print('Firstly you have to download dependencies by "pip install -r requirements.txt"')

site = 'https://kinohit.uz/'

hr = "="*10 + "{}" + "="*10

urls = {
    'films': site + 'russian-film-kino-tasix-tas-uz-uzbekistan/',
    'serials': site + 'serialy-na-russkom-v-tasix/',
    'cartoons': site + 'russian-film-kino-tasix-tas-uz-uzbekistan/multfilm/'
}

def get_stripped_text(component):
    return component.get_text().strip()

def get_scraped(url, session):
    page = session.get(url)
    return BS(page.content, 'html.parser')

def content_includes(content, details):
    keywrds = details.split(',')
    coincidences = []
    if details is not None:
        for word in keywrds:
            coincidences.append(word in content)

    counts = coincidences.count(True)
    if counts >= 1:
        return True
    return False

def get_films(scraped_page, details, description_length=120):
    films = scraped_page.find_all('a', class_='popover-dismissible-serial')
    for data in films:
        link = data['href'].strip()
        content = data['data-content']
        if content_includes(content, details):
            result = BS(content, 'html.parser')

            name = result.h3.get_text().strip()
            descr = get_stripped_text(result.p)[:description_length]
            categories = [get_stripped_text(categ) \
                          for categ in result.select('div.box_info_cat_movie')]
            age = get_stripped_text(result.find('div',
                                                class_='box_info_age'))
            ratings = [get_stripped_text(rating)\
                        for rating in result.find_all('div',
                                                        class_='text-rate')]
            extra = 'Quality' if type != 'serials' else 'Last episode'
            quality_or_episode = get_stripped_text(
                data.parent.parent.select('div.kachestvo_short_story')[0]
            )

            msg = f"\nName: {name}"\
                + f"\nDescription: {descr}..."\
                + f"\nCategories: {', '.join(categories)}"\
                + f"\nLink: '{link}'"\
                + f"\nAge: {age}"\
                + f"\nRatings: IMDb - {ratings[0]} Kinopoisk - {ratings[1] if len(ratings)==2 else '0'}"\
                + f"\n{extra}: {quality_or_episode}\n"

            print(msg)

def get_russian(type):
    url = urls[type]

    pages_count = int(input('How many pages do you want us to through?\n>'))
    details = input('Details the film include, add extras by comma. For example: 6+, Комедия.\n>')

    s = requests.Session()
    print(hr.format(' RESULTS START '))

    first_page_scraped = get_scraped(url, s)
    get_films(first_page_scraped, details)

    if pages_count >= 2:
        for i in range(2, int(pages_count)+1):
            page_scraped = get_scraped(url + f'page/{str(i)}/', s)
            get_films(page_scraped, details)
    print(hr.format(' RESULTS END '))

if __name__ == '__main__':
    msg = hr.format(' INTERFACE ') + '\nWelcome to kinohit.uz searching engine!\
\nUse command during the program:\
\n[s]earch - to start searching\
\n[q]uit - to quit the program'
    command = input(f'{msg}\n\nEnter the command of the program: ')
    while not (command.lower() in ['q', 'quit', 'exit', '^C']):
        search_types = ', '.join(list(urls.keys()))
        if command.lower() in ['s', 'search', 'start']:
            type = input(f"Enter type of movies. Available now: {search_types}\n>")
            get_russian(type)

        command = input(f'{msg}\n\nEnter the command of the program: ')
