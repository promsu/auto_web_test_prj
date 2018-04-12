#! /usr/bin/python3
#! -*- coding:utf-8 -*-


import xml.dom.minidom as mndom


doc = mndom.Document()
root = doc.createElement('Collections')
root.setAttribute('shelf', 'New Arrivals')
doc.appendChild(root)
movielists = [{'name': 'biubiubiu', 'type': 'War, Thriller', 'format': 'DVD', 'year': 1989, 'rating': 'PG', 'stars': 10, 'description': 'Talk about a US-Japan war'},
              {'name': 'papapa', 'type': 'science', 'format': '蓝光', 'year': 2018, 'rating': 'R', 'stars': 20, 'description': 'A schientific fiction'},
              {'name': '前任3:再见前任', 'type': 'comdy', 'format': 'MP3', 'year': 2006, 'rating': 'SM', 'stars': 12, 'description': 'Viewable boredom'}]
for item1 in movielists:
    movie = doc.createElement(item1['name'])
    types = doc.createElement('type')
    types.appendChild(doc.createTextNode(item1['type']))
    formats = doc.createElement('format')
    formats.appendChild(doc.createTextNode(item1['format']))
    year = doc.createElement('year')
    year.appendChild(doc.createTextNode(str(item1['year'])))
    rating = doc.createElement('rating')
    rating.appendChild(doc.createTextNode(item1['rating']))
    star = doc.createElement('stars')
    star.appendChild(doc.createTextNode(str(item1['stars'])))
    dscrpt = doc.createElement('description')
    dscrpt.appendChild(doc.createTextNode(item1['description']))
    movie.appendChild(types)
    movie.appendChild(formats)
    movie.appendChild(year)
    movie.appendChild(rating)
    movie.appendChild(star)
    movie.appendChild(dscrpt)
    root.appendChild(movie)
f = open('C:/Users/AYYK/Desktop/mv.xml', 'w', encoding='utf-8')
doc.writexml(f, indent='\t', addindent='\t', newl='\n', encoding='utf-8')
f.close()
