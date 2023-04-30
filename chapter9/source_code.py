import urllib.request , urllib.error

file=urllib.request.urlopen("https://www.python.org/")

print(file.read())

#downloading a webpage

try:
    file=urllib.request.urlopen("https://www.python.org/")
    content=file.read()

except urllib.error.HTTPError:
    print('Page not found 404 ')
    exit()

with open('index.html','w') as f:
    f.write(str(content))

