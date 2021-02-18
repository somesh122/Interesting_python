x = input('Enter the phrase: ')
phrase = x.replace('of','').split()
y=''
for w in phrase:
    y = y + w[0].upper()

print('Acronym of'+' '+x+' '+'is'+' '+y)
