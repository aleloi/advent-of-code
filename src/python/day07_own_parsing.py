# If I recall my automata course correctly, this is an LR parser with one look ahead:
def parse_line(line):
    """<line> ::= <color> contain <contents>"""
    tokens = line.replace(",", " COMMA").replace(".", " PERIOD").split()
    tokens = list(reversed(tokens))  # it's a stack
    def eat(*expected):
        assert tokens.pop() in expected
    def parse_color():
        """<color> ::= <word> <word> (bag|bags)"""
        res = "{} {}".format(tokens.pop(), tokens.pop())
        eat("bag", "bags")
        return res

    def parse_contents():
        """<contents> ::= contain (no other bags|<bag-amount-list>) PERIOD"""
        assert tokens.pop() == "contain"
        if tokens[-1] == "no":
            eat("no")
            eat("other")
            eat("bags")
            res = [(0, None)]
        else:
            res = parse_bag_amount_list()
        eat("PERIOD")
        return res

    def parse_bag_amount_list():
        """<bag-amount-list> ::= <integer> <color> (COMMA <integer> <color>)*"""
        res = []
        am = int(tokens.pop())
        col = parse_color()
        res.append((am, col))
        while tokens[-1] == "COMMA":
            eat("COMMA")
            am = int(tokens.pop())
            col = parse_color()
            res.append((am, col))
        return res

    col = parse_color()
    contents = parse_contents()
    assert not tokens
    return (col, contents)
            
for line in desc:
    print(parse_line(line))
    """dull gray bags contain 4 muted cyan bags, 3 light maroon bags."""
    line = line.rstrip(".")
    what, rest = line.split(" contain ")
    what = strip_bag(what)
    rest = rest[:-1].split(", ")
    rest_am = []
    for r in rest:
        """4 muted cyan bags"""
        r = strip_bag(r)
        #print(r)
        if r == "no other":
            am, col = 0, None
        else:
            am, col = int(r[0]), r[2:]
        rest_am.append((am, col))
    assert what not in graph
    graph[what] = rest_am
