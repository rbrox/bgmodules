import requests
from bs4 import BeautifulSoup


def url_constructor(book, chapter, verse):
    return f'https://vedabase.io/en/library/{book}/{chapter}/{verse}'

class_names = [
    "r r-title r-verse",
    "wrapper-devanagari",
    "r r-devanagari",
    "wrapper-verse-text",
    "wrapper-synonyms",
    "wrapper-translation",
    "wrapper-puport"
]

def web_scrape_divs(url, div_classes=None, div_id=None):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            div_texts = []
            
            # If div_classes is provided and it's a list, loop through each class
            if div_classes:
                for div_class in div_classes:
                    divs = soup.find_all('div', class_=div_class)  # Find divs by each class
                    # Extract and add the text from these divs to the div_texts list
                    div_texts.extend([div.get_text(separator=' ', strip=True) for div in divs])
            
            # If div_id is provided, scrape based on id
            elif div_id:
                divs = soup.find_all('div', id=div_id)  # Find div by id
                div_texts.extend([div.get_text(separator=' ', strip=True) for div in divs])
            
            # If neither div_class nor div_id is provided, scrape all divs
            else:
                divs = soup.find_all('div')  # Find all divs if no class or id is given
                div_texts.extend([div.get_text(separator=' ', strip=True) for div in divs])
            
            # Join all the div texts into a single string
            return ' '.join(div_texts)
        else:
            return f"Error: Unable to fetch the page, status code {response.status_code}"
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    
    url = url_constructor('bg', 1, 1)
    
    # You can now pass a list of classes
    print(web_scrape_divs(url, div_classes=class_names))
