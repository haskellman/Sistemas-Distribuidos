<br />
<p align="center">
  <h3 align="center">Laboratorio 1</h3>

  <p align="center">
    Israel dos Santos Candeias
  </p>
</p>

## Sobre

Experimentar o paralelismo por meio de processos e threads na ordenação de um
vetor de grandes dimensões. Comparar o tempo de execução da tarefa de ordenação
de vetores com diferentes quantidades de processos ou threads.

### Feito com

* [Python 3](https://www.python.org/about/)

### Hardware

O programa foi testado em uma máquina com as seguintes especificações:

* Processador Ryzen 7 de 8 núcleos e 16 threads
* Memória de 16 GB à 3200 MHz

Os resultados mostrados aqui podem variar de acordo com as especificações de hardware

## Executando

O script de ordenação pode ser executado seguindo estes passos.

## Uso

Rodando o programa:
  ```sh
  python main.py
  ```
ou então:
  ```sh
  python3 main.py
  ```
OBS:
Passar os valores de k e n por linha de comando como especificado

## Módulos

O pacote `src` contém os módulos auxiliares desenvolvidos, são eles:

1. [sort.py] módulo contendo as funçoes de ordenação por paralelismo por processos;

2. [utils.py] módulo contendo funções auxiliares para gerar uma lista aleatória, dividir o vetor etc;

<!-- ## Resultados

Foram utilizados os valores de 1, 2, 4, 8 e 16 processos durante os testes e foi realizado 5 testes para cada, a lista que foi ordenada possui 10.000.000 elementos que são números de 0 a 9 gerados aleatoriamente.

<center>

  | Num Processos | Média Tempo Exec. |
  |:-------------:|:-----------------:|
  |       1       |     1.56152 s     |
  |       2       |     4.46606 s     |
  |       4       |     6.37051 s     |
  |       8       |     7.84878 s     |
  |       16      |     9.27737 s     |

</center>

Como podemos ver na tabela, o tempo médio cresce a medida que vamos adicionando mais processos isso se deve ao fato de que o python possui um mutex Python Global Interpreter (GIL) que faz com que não permita que mais de uma thread seja executada simultaneamente fazendo com que gere um gargalo no programa com o aumento de processos gerando overheads

-->

## Grupo

  Israel dos Santos Candeias- 2016101252 
