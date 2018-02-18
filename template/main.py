# Python 3.6.4 

def add_string_with_plus(iters):

    s = ""

    for i in range(iters):

        s += "xyz"

    assert len(s) == 3*iters



def add_string_with_format(iters):

    fs = "{}"*iters

    s = fs.format(*(["xyz"]*iters))

    assert len(s) == 3*iters



def add_string_with_join(iters):

    l = []

    for i in range(iters):

        l.append("xyz")

    s = "".join(l)

    assert len(s) == 3*iters



def convert_list_to_string(l, iters):

    s = "".join(l)

    assert len(s) == 3*iters
