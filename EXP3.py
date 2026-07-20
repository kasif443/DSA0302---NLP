from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

text = input("Enter a sentence: ")

words = word_tokenize(text)

print("Original Words:", words)
print("Stemmed Words:")

for word in words:
    print(word, "->", ps.stem(word))
