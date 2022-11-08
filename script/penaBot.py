'''
2022 © MaoHuPi
penanaBot/script/penaBot.py
'''

import os, sys
import json
import http.cookiejar as cookiejar
import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

path = '.' if os.path.isfile('./'+os.path.basename(__file__)) else os.path.dirname(os.path.abspath(__file__))

def requestsWebsite(mode = 'GET', url = '', cookie = {}, args = {}, allow_redirects = True):
    r = getattr(requests, mode.lower())(url, cookies = cookie, data = args, allow_redirects = allow_redirects)
    r.status = r.status_code
    r.data = r.text
    if r.status != 200:
        print('{mode} {url}: {status}'.format(mode = mode, url= url, status = r.status))
    # print(r.cookies)
    return(r)

def login(account, password):
    cookie = cookiejar.CookieJar()
    formData = {
        'email': account, 
        'password': password, 
        'rmbme': 1, 
        'redirurl': '/home'
    }
    home = requestsWebsite('GET', url + '/story/114674/storyName/issue/1', cookie = cookie)
    home = requestsWebsite('POST', url + '/login.php', cookie = cookie, args = formData, allow_redirects = False)
    cookie = home.cookies
    return(cookie)

def like(cookie, story_id, chapter):
    page = requestsWebsite('GET', url + '/story/{story_id}/storyName/issue/{chapter}'.format(story_id = story_id, chapter = chapter), cookie = cookie)
    page_html = BeautifulSoup(page.content, 'html.parser')
    chapter_id = page_html.find('div', {'class': 'datadiv', 'story-id': story_id, 'chapter': chapter}).attrs['chapter-id']
    action_token = page_html.find('meta', {'name': 'csrf-token'}).attrs['content']
    formData = {
        'story_id': story_id, 
        'chapter_id': chapter_id, 
        'chapter': chapter, 
        'action': 'likechapter', 
        'return_json': 1, 
        'action_token': action_token
    }
    print(formData)
    json = requestsWebsite('POST', url + '/process.php', cookie = cookie, args = formData).content
    file = open(path + '/request.html', 'w+', encoding = 'utf-8')
    file.write(str(json))
    file.close()