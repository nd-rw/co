import csv
import urllib.request


def moviesiwanttowatch_csv():
    url = "http://www.imdb.com/list/ls025824959/export?ref_=ttls_exp"
    response = urllib.request.urlopen(url)
    cr = csv.reader(response)

    for row in cr:
        print(row)


moviesiwanttowatch_csv()