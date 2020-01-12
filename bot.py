import requests
from bs4 import BeautifulSoup as bs
import os
# website containing images
url = 'https://www.pexels.com/search/skate'
# download page
page = requests.get(url)
soup = bs(page.text, 'html.parser')
# locate all the elemts with image tags
image_tags = soup.findAll('img')
# create directory for skateboarding images
if not os.path.exists('skaters'):
        os.makedirs('skaters')

    # moving to new directory
os.chdir('skaters')
# image file name variable
x = 0
# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('skate-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
