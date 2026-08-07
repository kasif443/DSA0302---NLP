# Inflectional Morphology - Scenario 5

words = ["create", "creates", "creating"]

def process(word):

    root = "create"

    if word == "create":
        suffix = "-"
        grammar = "Base Form"

    elif word.endswith("s"):
        suffix = "-s"
        grammar = "Third Person Singular"

    elif word.endswith("ing"):
        suffix = "-ing"
        grammar = "Present Participle"

    return [word,suffix,grammar,root,root,root]

print("{:<15}{:<10}{:<30}{:<12}{:<15}{}".format(
    "Original","Suffix","Grammatical Category",
    "Root","Normalized","Final"))

for w in words:
    print("{:<15}{:<10}{:<30}{:<12}{:<15}{}".format(*process(w)))