# Advanced Algorithms

This repository contains implementations of various advanced algorithms covered in the "Advanced Algorithms" lecture by Professor Albers at the Technical University of Munich (TUM). The algorithms are implemented in Python and include both the algorithm implementations and corresponding unit tests.

## Table of Contents

- Algorithms
- Tests
- Installation
- Usage
- Visualization
- License

## Algorithms

The following algorithms are implemented in this repository:

### Divide and Conquer Algorithms

- **Maximum Subarray Sum**  
- **Fast Fourier Transform (FFT)**  

### Dynamic Programming

- **Maximum Money Path**  
- **Weight Sum Possible**  

### Randomized Algorithms

- **Quicksort**  
- **Naive Primality Test**  
- **Simple Probably Prime Test**  
- **Randomized Primality Test**  
- **Fast Exponentiation**  
- **Miller-Rabin Primality Test**

### Data Structures

- **Fibonacci Heap**  
- **Treap**

### Cryptography

- **RSA Encryption and Decryption**

### String Algorithms

- **Suffix Trees**

## Tests

Unit tests are provided for each algorithm to ensure correctness. The tests are located in the "tests" directory and are implemented using the "unittest" framework.

## Installation

To run the algorithms and tests, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

You can run the unit tests to verify the implementations by typing:

```bash
python -m unittest discover -s tests
```

You can also run individual test files, for example:

```bash
python test_treap.py
```

## Visualization

Some algorithms and data structures in this repository use Graphviz to visualize their operations and output step-by-step images. These images are saved in the "output" directory. To use this feature, you need to have Graphviz installed on your machine. You can download and install Graphviz by visiting:

[Graphviz Download Page](https://graphviz.org/download/)

For example, the Treap data structure captures snapshots of its state after each insertion and deletion operation, which can be helpful for understanding how the data structure evolves over time.

## License

This project is licensed under the MIT License. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, provided that you include the original copyright and permission notice in all copies or substantial portions of the Software.

For more details, see the LICENSE file.