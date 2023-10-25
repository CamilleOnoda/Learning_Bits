from urllib import request

#1/Simple web browser
fhand = request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
print()


#2/Work with it like a file. Here word count
fhand = request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
print()

#3/Reading web pages
fhand = request.urlopen('http://www.dr-chuck.com/page1.html')
for line in fhand:
    print(line.decode().strip())
