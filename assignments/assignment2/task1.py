import webbrowser
from random import choice
random_page_generator = ['http://www.google.com',
                              'http://www.twitter.com']
webbrowser.open(choice(random_page_generator))



