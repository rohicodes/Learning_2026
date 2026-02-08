word = "aAbBcCdDeEfFgG"
sentence = """LEssgo 
lessgoe go go lessgo"""
##for multi line strings you just use tripple quotes """like this """
print(sentence)
print(word.upper())
print(word.capitalize())
print(word.casefold())
print(word.lower())
print(word.count("o"))
print(word[4])
print(sentence[7])
print(word[0:-4:2])
print(word[1:-4:2])
print(word[0:-4])
print(word[-4])
print(sentence.title())
print(word.title())
print(sentence.find("bb"))
print(word.find("x"))
new_sentence= sentence.replace("ss","s")
print(new_sentence.replace("o","oo"))
