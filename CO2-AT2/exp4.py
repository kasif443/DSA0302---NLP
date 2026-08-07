# Morphological Parsing - Scenario 4

words = ["activate", "activation", "reactivation"]

def parse(word):

    prefix = ""
    suffix = ""
    root = "activate"

    if word == "activate":
        sequence = "Base Verb"
        meaning = "Cause to become active"

    elif word == "activation":
        suffix = "-ion"
        sequence = "activate → activation"
        meaning = "Verb → Noun"

    elif word == "reactivation":
        prefix = "re-"
        suffix = "-ion"
        sequence = "activate → activation → reactivation"
        meaning = "Again + Noun"

    return [word,prefix,root,suffix,sequence,root,meaning]

print("{:<15}{:<10}{:<12}{:<10}{:<35}{:<15}{}".format(
    "Original","Prefix","Root","Suffix",
    "Derivational Sequence","Normalized","Meaning"))

for w in words:
    print("{:<15}{:<10}{:<12}{:<10}{:<35}{:<15}{}".format(*parse(w)))