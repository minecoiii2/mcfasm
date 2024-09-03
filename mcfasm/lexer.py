from lexer_kws import score

keywords = {
    "score": score
}

def read_line(line: str):
    tokens = []

    for kw, v in keywords.items():
        if line.startswith("#"): continue

        if line.startswith(kw + " "):
            line = line.removeprefix(kw + " ")

            init = v.feed(line)

            break