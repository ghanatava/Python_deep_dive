import urllib.parse

url='http://www.dreamtechpress.com:80/engineering/computer-science.html'

tpl=urllib.parse.urlparse(url)

print(tpl)

print('Scheme = ',tpl.scheme)
print('Net location= ',tpl.netloc)
print('Path = ',tpl.path)
print('Parameters = ',tpl.params)
print('Port = ',tpl.port)
print('Total url=',tpl.geturl())