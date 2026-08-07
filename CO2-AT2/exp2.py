# Morphological Parser - Scenario 2

words = ["disagree", "agreement", "agreeable"]

def parse(word):

    prefix = ""
    suffix = ""
    root = "agree"
    if word.startswith("dis"):
        prefix = "dis-"
        category = "Derivational (Negative Prefix)"
        meaning = "Opposite of agree"

    elif word.endswith("ment"):
        suffix = "-ment"
        category = "Derivational (Noun Formation)"
        meaning = "State or act of agreeing"

    elif word.endswith("able"):
        suffix = "-able"
        category = "Derivational (Adjective Formation)"
        meaning = "Capable of agreeing"

    else:
        category = "Base"
        meaning = "Agreement"

    return [word,prefix,root,suffix,category,meaning,root]

print("{:<15}{:<10}{:<10}{:<10}{:<30}{:<35}{}".format(
    "Original","Prefix","Root","Suffix",
    "Category","Semantic Interpretation","Normalized"))

for w in words:
    print("{:<15}{:<10}{:<10}{:<10}{:<30}{:<35}{}".format(*parse(w)))