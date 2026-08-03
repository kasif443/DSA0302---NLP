from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running", "jumps", "easily", "flying", "studies", "playing", "cats"]

print("Original Word -> Stemmed Word")

for word in words:
    print(word, "->", ps.stem(word))