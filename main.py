def tan_b(seq):
    """
    Recursive function to find the b value of a path
    """
    if len(seq) == 1:
        return 0
    if seq[-1] == 0:
        return tan_b(seq[:-1])
    if seq[-1] == 1:
        return tan_b(seq[:-1]) + 2

def tan_c(seq):
    """
    Recursive function to find the c value of a path
    """
    if len(seq) == 1:
        return 1
    if seq[-1] == 0:
        return tan_c(seq[:-1]) + 1
    if seq[-1] == 1:
        return tan_c(seq[:-1]) - 1

def tan_a(seq):
    """
    Recursive function to find the a value of a path
    """
    if len(seq) == 1:
        return 1
    if seq[-1] == 0:
        return tan_a(seq[:-1]) * tan_b(seq[:-1])
    if seq[-1] == 1:
        return tan_a(seq[:-1]) * tan_c(seq[:-1])

def get_seqs_n(n):
    """
    Produces every ith path for each leaf of an n-depth binary tree, in order from left-right
    """
    seqs = [[0]]
    for i in range(n):
        seqs1 = []
        for seq in seqs:
            seqs1.append(seq + [0])
            seqs1.append(seq + [1])
        seqs = seqs1
    return seqs

def tan_combine_like_terms(terms):
    """
    This method will take a set of 3-tuples, (a,b,c), where like terms are matching b,c
    It will then combine like terms by summing up all the coefficients a
    """
    output = {}
    for term in terms:
        a = term[0]
        b = term[1]
        c = term[2]
        if b in output:
            if c in output[b]:
                output[b][c] += a
            else:
                output[b][c] = a
        else:
            output[b] = {}
            output[b][c] = a
    output1 = []
    for b in output:
        for c in output[b]:
            output1.append([output[b][c],b,c])
    return output1

def print_tan_derivative_no_like_terms(n):
    """
    Main method that will compute the nth derivative of tan,
    but DOES NOT combine like terms.
    """
    output = ""
    seqs = get_seqs_n(n)
    for seq in seqs:
        a = tan_a(seq)
        if a != 0:
            if a != 1:
                output += f"{a}"
            b = tan_b(seq)
            if b != 0:
                if b != 1:
                    output += f"sec{b}"
                else:
                    output += "sec"
            c = tan_c(seq)
            if c != 0:
                if c != 1:
                    output += f"tan{c}"
                else:
                    output += "tan"
            output += " + "
    output = output.strip()
    if output.endswith("+"):
        output = output[:-1]
    print(output)

def print_tan_derivative(n):
    """
    Main method that will compute the nth derivative of tan
    """
    output = ""
    seqs = get_seqs_n(n)
    seqs1 = []
    for seq in seqs:
        a = tan_a(seq)
        b = tan_b(seq)
        c = tan_c(seq)
        seqs1.append([a,b,c])
    seqs = tan_combine_like_terms(seqs1)
    for seq in seqs:
        a = seq[0]
        b = seq[1]
        c = seq[2]
        if a != 0:
            if a != 1:
                output += f"{a}"            
            if b != 0:
                if b != 1:
                    output += f"sec{b}"
                else:
                    output += "sec"
            if c != 0:
                if c != 1:
                    output += f"tan{c}"
                else:
                    output += "tan"
            output += " + "
    output = output.strip()
    if output.endswith("+"):
        output = output[:-1]
    return f"tan^({n}) = "+output

""" 
Run code that will produce the first 15 derivatives of tan
WARNING: the code does not work well over i=15, becoming very slow very quickly,
due to recursion. Possible fix: Utilise memory to reduce recursion work.
"""
for i in range(16):
    print(print_tan_derivative(i))


