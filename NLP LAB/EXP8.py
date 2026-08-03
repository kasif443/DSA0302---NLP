import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

text = "The cat sits on the mat."

words = nltk.word_tokenize(text)

tagged_words = nltk.pos_tag(words)

print("Stochastic POS Tagging:")

for word, tag in tagged_words:
    print(word, "->", tag)