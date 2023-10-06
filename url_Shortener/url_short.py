import pyshorteners
# USING PYSHORTENRS library for shortening the urls

url = input('Enter the url: ')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print("The New URL:")
    print(s.tinyurl.short(url))

shortenurl(url)