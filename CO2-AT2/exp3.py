# Morphology Normalization - Scenario 3

words = ["govern", "government", "governance"]

def normalize(word):

    root = "govern"

    if word == "govern":
        affix = "-"
        level = "Level 0 (Base)"

    elif word.endswith("ment"):
        affix = "-ment"
        level = "Level 1 (Noun Derivation)"

    elif word.endswith("ance"):
        affix = "-ance"
        level = "Level 1 (Abstract Noun)"

    return [word,root,affix,level,root,root]

print("{:<15}{:<12}{:<12}{:<28}{:<15}{}".format(
    "Original","Root","Affix",
    "Derivational Hierarchy",
    "Normalized","Final"))

for w in words:
    print("{:<15}{:<12}{:<12}{:<28}{:<15}{}".format(*normalize(w)))