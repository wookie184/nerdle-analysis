OPERATORS = "+-*/"
DIGITS = "123456789"
LENGTH = 8

def gen(current):
    if current[-1] == "=":
        calc = ''.join(current[:-1])
        if all(op not in calc for op in OPERATORS):
            return
        ans = eval(calc)
        if isinstance(ans, float):
            if not ans.is_integer():
                return
            ans = int(ans)
        final = (*current, *str(ans))
        if ans >= 0 and len(final) == LENGTH:
            yield final
    elif len(current) >= LENGTH - 2:
        if current[-1] in (DIGITS + "0"):
            yield from gen((*current, "="))
    else:
        if current[-1] not in OPERATORS:
            for op in OPERATORS + "0=":
                yield from gen((*current, op))
        for d in DIGITS:
            yield from gen((*current, d))

solns = (sol for d in DIGITS for sol in gen((d,)))
with open("all_answers.txt", "w") as f:
    for res in sorted(solns):
        f.write(''.join(res) + "\n")