text = "The cat is running"

words = text.split()

tags = []

for word in words:
    if word.lower() in ["the", "a", "an"]:
        tag = "DT"
    elif word.lower() in ["is", "am", "are", "was", "were"]:
        tag = "VB"
    elif word.endswith("ing"):
        tag = "VBG"
    else:
        tag = "NN"
    tags.append((word, tag))

print("Transformation-Based POS Tagging:")

for word, tag in tags:
    print(word, "->", tag)