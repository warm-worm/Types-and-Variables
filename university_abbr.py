###
# A program that prints a university abbreviation
# ''.join means there is no separator  
university = "Krakow University of Economics"
exclude_words = {"of", "and", "the", "in", "at", "for"}
abbreviation = ''.join(word[0].upper() for word in university.split() if word.lower() not in exclude_words)
print(f'The university abbreviation is: {abbreviation}')