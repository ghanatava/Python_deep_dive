import urllib.request

url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2FHD%2520wallpaper%2F&psig=AOvVaw37RO83B4cpjHtQIs0jpQ4t&ust=1682946015842000&source=images&cd=vfe&ved=0CA4QjRxqFwoTCJDiqc7U0f4CFQAAAAAdAAAAABAD"

download=urllib.request.urlretrieve(url,"wallpaper.jpg")
