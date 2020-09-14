'''
Python Intsargram crawler module sample code
pip install instapy==0.1.1
'''

from instapy import InstaPy
from instapy import smart_run

insta_username = ''
insta_passwrd = ''

session = InstaPy(username=insta_username,
                  password=insta_passwrd,
                  headless_browser=False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4500,
                                    min_following=10)
    session.set_dont_include(['test1','test2','test3'])
    session.set_dont_like(['pizza','#store'])

    session.like_by_tags(['#hacker'],amount=10)