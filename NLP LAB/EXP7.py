import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

text = "Natural Language Processing is an interesting field."

words = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(words)

print("Part-of-Speech Tags:")
for word, tag in pos_tags:
    print(word, "->", tag)