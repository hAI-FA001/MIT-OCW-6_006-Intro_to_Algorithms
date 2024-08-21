# Lec 1 - Algorithms and Computation

## Goals:

- Solving computational problems
- Proving correctness of algorithms
- Efficiency
- Communicating these solutions or ideas to others

## Problem:

- a binary relation b/w inputs and outputs
  - a bipartite graph
- for each input, we specify which outputs are correct
- Defined using a predicate to check if given output is correct
  - as opposed to specifying outputs for all possible inputs, which could take forever

## Algorithm:

- should not be bound to a specific input size or a specific case
  - we want it to work for arbitrarily sized inputs and in the general case
- algo is `f: I -> O`
  - function that takes Input and maps it to a single Output
  - and the output must be correct based on our problem

### Example: Birthday Problem

"Find a pair of people with the same birthday"
<br> Algorithm:

<pre>
- Maintain record
- Interview students in some order
  - Check if birthday is in record
    - If so, return the pair
  - Add new student to record
- Return None
</pre>

## Inductive Proof

- To prove algorithm's correctness, we took courses like Discrete Maths to learn stuff like induction
- Made up of:
  - Inductive Hypothesis: What I need to maintain
  - Base Case: Initial value for the variable set up in the hypothesis (variable K)
  - Inductive Step

For birthday problem:

<pre>
Inductive Hypothesis (I.H.):
    If first K students contain a match, algo returns the match before interviewing student K+1
Base Case:
    K = 0
    No student, no match so I.H. holds true
Inductive Step
    Assume I.H. is true for K = K`
    Two Cases:
        - if we already had a match, then algo returned it, by I.H.
        - else if (k`+1) contains match, then algo checks (k`+1)th student against all other students
</pre>

## Efficiency

- Measure number of operations rather than time
  - cuz time is dependent on hardware, we want to abstract that away
- Performance depends on size of the input "n"
  - size can be different than "n":
    - if input is a n-by-n matrix, then input size is n^2
    - if it's a graph, then input size is |V| + |E|
- Big-O Notation:
  - O(.) -> upper bound
  - Ω(.) -> lower bound
  - Θ(.) -> both, bounds the performance from above and below ("tight bound")

### Examples:

- `Θ(1):` Constant time
- `Θ(lg(n)):` Logarithmic time
- `Θ(n):` Linear time
- `Θ(nlg(n)):` Log-linear time
- `Θ(n^2):` Quadratic time
- `Θ(n^c):` Polynomial time
  - as long as "c" is some constant
- `2^Θ(n):` Exponential time
  - this is some constant to the function of "n"

## Model of Computation

### RAM (Random Access Machine) Model

- Assumption: we can randomly access places in memory in Θ(1)
- CPU acts on words
  - if word size is w, then it can address 2^w locations
    - for 32b, it's 4GB
      - if we had HDD with more than 4GB storage, then need to partition it into 4GB partitions
    - for 64b, it's about 10 exabytes
- CPU
  - can hold a small amount of info and operate on it
  - has instructions to load and put info back in memory
  - operations that take Θ(1):
    - arithmetic operations
    - logical operations
    - bitwise operations
    - reading/writing to and from memory
  - takes Θ(1) time to operate on Θ(1) amount of memory
    - would take Θ(n) to operate on linear amount of memory

# Data Structures

- Store non-constant amount of info
- Make operations on that info faster

# How to solve an Algorithms Problem

## Reduce to a problem you already know (DS or Algo)

- Search Problem (Data Structures)
  - Static Array (Lec 1)
  - Linked List (Lec 2)
  - Dynamic Array (Lec 2)
  - Sorted Array (Lec 3)
  - Direct-Access Array (Lec 4)
  - Hash Table (Lec 4)
  - Balanced Binary Tree (Lec 6-7)
  - Binary Heap (Lec 8)
- Sort Algos

  - Insertion Sort (Lec 3)
  - Selection Sort (Lec 3)
  - Merge Sort (Lec 3)
  - Counting Sort (Lec 5)
  - Radix Sort (Lec 5)
  - AVL Sort (Lec 7)
  - Heap Sort (Lec 8)

- Shortest Path Algos
  - Breadth First Search (Lec 9)
  - DAG Relaxation (Lec 11)
    - Depth First Search (Lec 10)
    - Topological Sort (Lec 10)
  - Bellman-Ford (Lec 12)
  - Dijkstra (Lec 13)
  - Johnson (Lec 14)
  - Floyd-Warshall (Lec 18)

## Design your own Algo

- Brute Force
- Decrease and Conquer
- Divide and Conquer
- Dynamic Programming (Lec 15-19)
- Greedy/Incremental
