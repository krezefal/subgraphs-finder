# Finding the probability of connected graph existence

Finding the probability of the existence of a connected graph in 2 ways: 
- **Modeling**. In this case, according to the adjacency matrix, where the 
paths existence probabilities are indicated, subgraphs are repeatedly
constructed (specified with tests number) and then, summing up the number of 
connected graphs and dividing it on the number of tests, the probability is 
calculated.
- **Brute forcing**. Then all vertices in the graph whose probability is 
greater than 0 are considered as possible ones and all subgraphs are iterated 
with the calculation of probability for connected ones. Summing up all the 
probabilities, the final one is calculated.

## Usage

The program is a CLI app written in Python 3.9.6, which alternately performs 
the two operations described above.

```
Usage: finder.py -s SIZE -n NUMBER [-m] [-v] [-t] [-h]

Options:
  -s SIZE, --size SIZE  Adjacency matrix size - number of vertices.
  -n NUMBER, --number NUMBER
                        Number of tests for simulation process.
  -m, --manual          If argument is provided, you will be asked to enter the adjacency matrix.
  -v, --verbose         If argument is provided, more detailed output will be shown.
  -t, --timer           If argument is provided, the time will be measured for each operation.
  -h, --help            Show this help message and exit.
```