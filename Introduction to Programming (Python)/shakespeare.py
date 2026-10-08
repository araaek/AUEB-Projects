from urllib.request import urlopen
text=urlopen('https://composingprograms.com/shakespeare.txt').read().decode().split()
print('οι πρώτες 10 λέξεις: ',text[0:10])
print('το πλήθος των and: ',text.count('and'))
print('το πλήθος των mouse: ',text.count('mouse'))
words=set(text)
print('το πλήθος όλων των λέξεων: ',len(words))


