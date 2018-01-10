# KAPA

**K**it's  
**A**rtificial immune system  
**P**ython  
**A**lgorithm

KAPA is an implementation of the clonal selection algorithm CLONALG described in [*Learning and Optimization Using the Clonal Selection Principle (2001)*](http://www.dca.fee.unicamp.br/~vonzuben/research/lnunes_dout/artigos/ieee_tec01.pdf).

KAPA is unrelated to the company, academy, fabric or radio station with similar names.

## Requirements
- Python 2.7
- Matplotlib

## Installation

1. Install Python 2.7
2. Install Matplotlib using `pip install matplotlib`

## Usage

KAPA comes with `h1_evaluation.py` and `h2_evaluation.py`. They run KAPA with different parameters and save the results to a CSV file for analysis. H1 and H2 refers to the two hypothesis tested by my replication of the aforementioned paper:

H1:
> Given a set of antigens KAPA will produce antibodies capable of identifying the antigens. This can be analysed be running KAPA on the original set of eight digits. This was done by recreating the 10x12 binary characters in the original paper. The characters were converted to antigens by representing them using the Hamming shape-space, where each character is a bitstring of length 120. Black and white pixels were converted to True/False values respectively.

H2:
> The number of generations taken for convergence remains constant as antigen numbers increase, given Ag <= Ab. This can be measured using a linear model with the number of antigens as the independent variable and the number of generations taken for convergence as the dependant variable. KAPA was run 30 times each on an increasing number of randomly generated antigens Ag = 1..10.

KAPA is written as a library, so you could instead `import kapa` and then run `kapa.kapa()`, specifying the antibodies, antigens and your preferred parameters for the algorithm.

## License
[MIT License](https://opensource.org/licenses/MIT)
