from random import randint

def generate_vector(length: int) -> list:
    return [randint(1,10) for _ in range(int(length))]

def split(a, n):
    k, m = divmod(len(a), n)
    return [a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]