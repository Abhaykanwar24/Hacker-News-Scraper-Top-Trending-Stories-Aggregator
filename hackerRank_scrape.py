import requests
from bs4 import BeautifulSoup
import pprint

def fetch_pages(limit):
    base_url = 'https://news.ycombinator.com/news'
    current_url = base_url
    all_links = []
    all_subtext = []
    page_count = 0

    while current_url and page_count < limit:
        res = requests.get(current_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Extract links and subtext from the current page
        links = soup.select('.titleline > a')
        subtext = soup.select('.subtext')
        all_links.extend(links)
        all_subtext.extend(subtext)
        
        # Find the "More" link to proceed to the next page
        more_link = soup.select_one('.morelink')
        if more_link:
            current_url = f"https://news.ycombinator.com/{more_link.get('href')}"
            page_count += 1
        else:
            current_url = None  # No more pages to scrape

    return all_links, all_subtext

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:  # Only include stories with more than 99 votes
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

# Ask the user how many pages to scrape
try:
    user_page_limit = int(input("Enter the number of pages to scrape (max 20): ").strip())
    if user_page_limit > 20:
        print("Limiting to 20 pages.")
        user_page_limit = 20
    elif user_page_limit < 1:
        print("Minimum page limit is 1. Setting to 1 page.")
        user_page_limit = 1
except ValueError:
    print("Invalid input. Defaulting to 1 page.")
    user_page_limit = 1

# Fetch the specified number of pages
all_links, all_subtext = fetch_pages(user_page_limit)

# Process the collected data
hn_stories = create_custom_hn(all_links, all_subtext)

# Display the stories
if hn_stories:
    pprint.pprint(hn_stories)
else:
    print("No stories found.")
