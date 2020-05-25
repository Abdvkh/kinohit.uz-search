try:
    import requests
    from bs4 import BeautifulSoup as BS
except ModuleNotFoundError:
    print('Firstly you have to download dependencies by "pip install -r requirements.txt"')

urls = {
    'films': 'https://kinohit.uz/russian-film-kino-tasix-tas-uz-uzbekistan/',
    'serials': 'https://kinohit.uz/serialy-na-russkom-v-tasix/'
}

def get_stripped_text(component):
    return component.get_text().strip()

def get_scraped(url, session):
    page = session.get(url)
    return BS(page.content, 'html.parser')

def get_films(scraped_page, details, description_length=120):
    films = scraped_page.find_all('a', class_='popover-dismissible-serial')

    for data in films:
        link = data['href']
        content = data['data-content']
        if details in content:
            result = BS(content, 'html.parser')
            msg = f"Name: {result.h3.get_text().strip()}"\
                + f"\nDescription: {get_stripped_text(result.p)[:description_length]}..."\
                + f"\nCategories: {', '.join([get_stripped_text(categ) for categ in result.select('div.box_info_cat_movie')])}"\
                + f"\nLink: '{link.strip()}'"\
                + f"\n{'Quality' if type == 'films' else 'Last episode'}: {get_stripped_text(data.parent.parent.select('div.kachestvo_short_story')[0])}\n\n"

            print(msg)

def get_russian(type):
    url = urls[type]
    pages_count = int(input('How many pages do you want us to through?\n>'))
    details = input('Details the film include: ')
    s = requests.Session()

    first_page_scraped = get_scraped(url, s)
    get_films(first_page_scraped, details)

    if pages_count >= 2:
        for i in range(2, int(pages_count)+1):
            page_scraped = get_scraped(url + f'page/{str(i)}/', s)
            get_films(page_scraped, details)

if __name__ == '__main__':
    type = input(f"Enter type of movies. Available now: {', '.join(list(urls.keys()))}\n>")
    get_russian(type)
