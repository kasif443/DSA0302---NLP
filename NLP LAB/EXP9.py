import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')
nltk.download('punkt_tab')

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'NN$'),
    (r'.*s$', 'NNS'),
    (r'^[0-9]+$', 'CD'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

text = "The boys are playing games"

words = word_tokenize(text)

tagged_words = tagger.tag(words)

print("Rule-Based POS Tags:")

for word, tag in tagged_words:
    print(word, "->", tag)