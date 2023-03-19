# # # from urllib import request
# # # # url = "http://www.bbc.co.uk/news/election-us-2016-35791008"
# # # url = "https://i.ytimg.com/vi/6ktFUwPGWag/maxresdefault.jpg?sqp=-oaymwEmCIAFEOAD8quKqQMa8AEB-AH-BIAC4AOKAgwIABABGF4gXiheMA8=&rs=AOn4CLBAD4uaOXDcC1J_8tvGbZqRbPhBEw"
# # # html = request.urlopen(url).read().decode('utf8')
# # # html[:60]

# # # from bs4 import BeautifulSoup
# # # soup = BeautifulSoup(html, 'html.parser')
# # # title = soup.find('title')

# # # print(title) # Prints the tag
# # # print(title.string) # Prints the tag string content

# # import requests, bs4
# # url = 'http://www.transfermarkt.co.uk/wettbewerbe/europa'
# # url = "https://i.ytimg.com/vi/6ktFUwPGWag/maxresdefault.jpg?sqp=-oaymwEmCIAFEOAD8quKqQMa8AEB-AH-BIAC4AOKAgwIABABGF4gXiheMA8=&rs=AOn4CLBAD4uaOXDcC1J_8tvGbZqRbPhBEw"
# # headers = {"User-Agent":"Mozilla/5.0"}
# # response = requests.get(url, headers=headers)
# # soup = bs4.BeautifulSoup(response.text, 'lxml')
# # print(soup)
# # # print(title)

# import requests, bs4

# url = "https://i.ytimg.com/vi/6ktFUwPGWag"
# # url = 'https://stackoverflow.com/questions/26812470/how-to-get-page-title-in-requests'
# # url = 'https://www.w3schools.com/html/html_basic.asp'
# headers = {"User-Agent":"Mozilla/5.0", 'Content-Type': 'image/jpeg'}
# response = requests.get(url, headers=headers)
# filename  = response.headers.get("Content-Disposition").split("filename=")[1].strip('"')
# print("Filename:", filename)
# # html = bs4.BeautifulSoup(response.text)
# # print(html.title)

# # with open("response.txt", "w") as file1:
# #     file1.write(response.text)
# #     # file1.writelines(L)

def has_highres_thumbnail(thumbnail_url):
    response = requests.head(thumbnail_url)
    return response.status_code == 200

import os
import requests

url = "https://i.ytimg.com/vi/E2ndTCorYsI/maxresdefault.jpg"

print(has_highres_thumbnail(url))
