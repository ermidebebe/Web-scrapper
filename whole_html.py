from requests_html import HTMLSession
def main():
    session=HTMLSession()
    while True:
        # ask for the user to enter the url
        url = input('URL: ')
        try:
            # download the page
            response = session.get(url)
            # check if it downloaded the page or raise exception
            response.raise_for_status()
            print(response.text)
            return
        except Exception as e:
            # print the error
            print(e)
            # ask the user to quit or enter url again
            prompt = input('Press Q to quit or press another key to enter another url: ')
            if prompt.lower() == 'q':
                return
            # ask the user to enter the webpage again
            print('Please insert the url again')
def render(response):
    try:
        #Reloads the response in Chromium, and replaces HTML content with an updated version, with JavaScript executed.
        response.html.render()
        with open('index.html','w') as file:
            file.write(response.text)
    except Exception as e:
        # print the error
            print(e)

