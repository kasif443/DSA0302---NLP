from collections import defaultdict
import random

text = "machine learning is fun machine learning is powerful"

words = text.split()

bigrams = defaultdict(list)

for i in range(len(words) - 1):
    bigrams[words[i]].append(words[i + 1])

current_word = random.choice(words)
generated_text = [current_word]

for i in range(9):
    if current_word in bigrams:
        current_word = random.choice(bigrams[current_word])
        generated_text.append(current_word)
    else:
        break

print("Generated Text:")
print(" ".join(generated_text))