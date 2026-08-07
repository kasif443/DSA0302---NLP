# Morphological Processing - Scenario 1

words = ["analyzing", "analysis", "analytical"]

def analyze(word):
    root = "analyze"
    affixes = []

    if word.endswith("ing"):
        affixes.append("-ing")
        mtype = "Inflectional (Present Participle)"
    elif word.endswith("sis"):
        affixes.append("-sis")
        mtype = "Derivational (Noun Formation)"
    elif word.endswith("ical"):
        affixes.append("-ical")
        mtype = "Derivational (Adjective Formation)"
    else:
        mtype = "Base"

    normalized = root

    return {
        "Original": word,
        "Root": root,
        "Affix": ", ".join(affixes),
        "Transformation": mtype,
        "Normalized": normalized
    }

print("{:<15}{:<12}{:<12}{:<35}{}".format(
    "Original","Root","Affix","Transformation","Normalized"))

for w in words:
    r = analyze(w)
    print("{:<15}{:<12}{:<12}{:<35}{}".format(
        r["Original"],
        r["Root"],
        r["Affix"],
        r["Transformation"],
        r["Normalized"]))