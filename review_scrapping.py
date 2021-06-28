import requests
import bs4
from selenium import webdriver

def main():
    while True:
        # ask for the user to enter the url
        url = input('URL: ')
        try:
            # download the page
            driver = webdriver.Chrome()
            driver.implicitly_wait(30)
            driver.get(url)
            driver.implicitly_wait(10)
            response = driver.page_source
            get_review(response)
            break
        except Exception as e:
            # print the error
            print(e)
            # ask the user to quit or enter url again
            prompt = input('Press Q to quit or press another key to enter another url: ')
            if prompt.lower() == 'q':
                return
            # ask the user to enter the webpage again
            print('Please insert the url again')


def get_review(response):
    review_soup = bs4.BeautifulSoup(response,features="lxml")
    while True:
        # Ask the user to insert user's nick and date
        print('please insert nick and date like nick date time e.g København 03/11/2020 17:18')
        nick_date = input('nick date time:')
        # get nick date and time.
        separate = nick_date.split(' ')
        if len(separate) == 3:
            nick, date, time = separate
            # get nick class elements
            element_nick = review_soup.select('.nick')
            # get the nick names
            nick_names = [x.getText().strip() for x in element_nick]
            # get review date class elements
            element_date = review_soup.select('.review__date')
            # get the review dates
            review_date = [x.getText().strip() for x in element_date]
            # change 12/23/45 to 12.34.45
            date = date.split('/')
            date = '.'.join(date)
            if nick in nick_names and date + '\xa0' + time in review_date:
                element = element_nick[nick_names.index(nick)]
                # get the parent of the element
                parent = element.parent.parent
                # get unique code of the review
                code = parent['id'][16:]
                # get the review paragraph
                review_element = review_soup.select('.review-content-' + code)
                # print the result
                print(review_element[0].getText()[0:30])
                # review helpful
                helpful = review_soup.select('.js-add-vote')
                i = 0
                print('Review Helpful')
                for link in helpful:
                    if link['data-post-id'] == code:
                        # get and print the votes
                        vote = link.select('span')
                        # if it is the first element print it is helpful
                        if i == 0:
                            print("Helpful :)", vote[0].getText())
                            # if it is second element print not helpful
                            i += 1
                        else:
                            print("Not helpful :(", vote[0].getText())
                return
            else:
                print('Nick or date is not found')
                prompt = input('Press Q to quit or press another key to enter another nick date: ')
                if prompt.lower() == 'q':
                    return
                # ask the user to enter the webpage again
                print('Please insert the nick and date again')
        else:
            print('Nick and date format is not correct')
            prompt = input('Press Q to quit or press another key to enter another nick date: ')
            if prompt.lower() == 'q':
                return
            # ask the user to enter the webpage again
            print('Please insert the nick and date again')


if __name__ == '__main__':
    main()
