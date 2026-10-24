import urllib.request
url="https://www.python.org"
response=urllib.request.urlopen(url)
html_data=response.read().decode('utf-8')
print(html_data)
