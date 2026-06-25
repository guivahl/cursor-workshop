# Checklist:

# [] Como o atual algoritmo funciona?
# [] Como melhorar a legibilidade do código?
# [] Qual é a complexidade temporal do algoritmo atual?
# [] Existe uma maneira de otimizar a solução (tempo ou espaço)?

def v(x, y):
    if len(x) != len(y):
        return False
    q = []
    for c in y:
        q.append(c)
    for p in x:
        r = -1
        for k in range(0, len(q)):
            if q[k] == p:
                r = k
                break
        if r == -1:
            return False
        q[r] = "!"
    return True


if __name__ == "__main__":
    print(v("anagram", "nagaram"))  # True
    print(v("rat", "car"))        # False

    # Testes adicionais:
    # print(v("listen", "silent"))  # True
    # print(v("triangle", "integral"))  # True
    # print(v("apple", "papel"))    # True
    # print(v("apple", "appeal"))   # False
