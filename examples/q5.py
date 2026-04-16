sent = input('entaer a sentance: ')
new_sent =' '.join(word.capitalize() for word in sent.split())
print(new_sent)