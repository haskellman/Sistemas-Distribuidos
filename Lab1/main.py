import time
from src.sort import mergesort
from src.utils import generate_vector

if __name__ == '__main__':
    k_input = int(input('Digite o número de vezes que os dados devem ser divididos no mergesort (k): '))
    n_input = int(input('Digite o tamanho do vetor de entrada a ser ordenado (n): '))
    vector : list = generate_vector(n_input)
    start : float = time.time()
    mergesort(vector, k=k_input)
    end : float = time.time()
    print(f"Tempo total: {end - start}")
