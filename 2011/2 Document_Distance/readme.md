# Lec 2 - Models of Computation

Unlike computer code, an algorithm always has some input and generates an output <br>

Algorithm is a mathematical analog of a computer program

- To reason about computer programs, convert them to algorithms first
- To solve a problem, devise an algorithm and convert it to computer code
- Analog of programming language in algo world is pseudo-code
- Analog of computer in algo world is Models of Computation
  - What operations a computer can do
  - What is their cost

## Models of Computation

### Random Access Machine (RAM Model)

- Random Access Memory (RAM) modeled by a big array
- In Θ(1) i.e. constant time:
  - load Θ(1) words (defined below)
  - do Θ(1) computations
  - store Θ(1) words
  - have Θ(1) registers
- is like Assembly programming
- word is "w" bits for us, not 64 or 32
  - in Peak Finding, our input was a matrix of numbers
    - didn't think about ints or floats
    - those are our "words"
  - should be <= lg(size of memory)
    - (lg = log w/ base 2)
    - cuz a word should be able to specify an index into the RAM array

### Pointer Machine (PM Model)

- Corresponds to OOP
- In RAM Model, there's no dynamic memory allocation unlike in PM where we have dynamically allocated objects
- Object has Θ(1) fields
- "field" is:
  - either our word (e.g. storing an int)
  - or a pointer (points to an object)
  - or null/none
- List is a data structure in a PM Model
- PM Model can be implemented in RAM Model, so PM Model is a weaker model

### Python Model

- arrays are called lists
  - "list" isn't actually a Linked List in Python
  - `L[i] = L[i] + 5` takes Θ(1) in Python rather than Θ(n)
- Object with Θ(1) attributes
  - if object has reasonable number of attributes, it fits in PM Model
    - not a million attributes, can't have "n" attributes
  - therefore, we can think manipulating that object as Θ(1)
  - accessing a field of an object of Θ(1) size takes Θ(1)
- above are our core concepts, everything else can be thought in terms of them
  - `l.append(x)`
    - obvious way: allocated new array, copy elements -> Θ(n)
    - but Python does "table doubling" (Lec 9)
    - it's Θ(1)
  - `l1 + l2`
    - is like:
    ```python
    l = []
    for x in l1:
        l.append(x)  # Θ(1)
    for x in l2:
        l.append(x)  # Θ(1)
    ```
    - takes O(|l1| + |l2| + 1)
      - "+ 1" cuz it still takes Θ(1) time to build an initial list even if both are empty
  - `x in l` is O(n)
  - `len(l)` is Θ(1) cuz Python stores a counter first
  - `L.sort()` is O(|L|lg(|L|) x time-to-compare-two-words)
    - time to compare is Θ(1) cuz usually we're just sorting words
    - uses comparison-based sort (Lec 3)
  - `D[key] = val` is O(1) cuz hash table (Lec 8 to 10)
    - assuming `key` is a single word
    - is O(1) with _high probability_ (uses randomized algo)
  - long (as in long int, data type) (Lec 11)
    - x + y takes O(|x| + |y|)
    - x \* y takes O( (|x| + |y|)^lg(3) )
      - lg(3) is about 1.6
      - straightforward algo (the one we used in grade school) would be O( (|x| + |y|)^2 ), so the one in Python is a bit better
  - heapq (Lec 4)
  - For more, <a href="https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/mit6_006f11_lec02/"> check online notes </a>

## Document Distance

"Given D1 and D2, compute d(D1, D2)"
<br> Motivation/Usages:

- As Google, when cataloging the web, you'd like to know when two web pages are identical
  - cuz then you'd store only 1
  - and you present it differently to the user ("there's this canonical document, then there's these extra copies")
- There are millions of mirrors of Wikipedia, which they found by hand, but you could do that using Document Distance
- Can find if two problem sets are identical for automated test
- Web search: Given some search text (which can be seen as a short document), want to get most similar docs (Document Distance would be least)

Definitions:

- document = sequence or vector of words
- word = string of alphanumeric chars
- idea: docs are similar if they have lots of shared words
  - there can be other definitions too
- D[W] gives number of occurences of W in D
  - so it's a vector of numbers, where the number is the occurence
  - we can plot this vector in W-dimensional space

<br>
Ideas for function d(D1, D2):

- from Vector Calculus, we can calculate similarity of two vectors using dot-product (or inner product)
  - it calculates commonality or similarity (inverse of distance)
  - d(D1, D2) = D1 . D2 = sum over W ( D1[w] . D2[w] )
  - issue:
    - 2 docs of 1M length with only 50% of words in common gives a score of 500K
    - 2 docs of 100 length with all 100% of words in common gives a score of only 100
    - not scale-invariant
- cosine of angle b/w two vectors (solves dot-product's issue)
  - d(D1, D2) = (D1 . D2) / (|D1| . |D2|)
  - AKA normalize the vectors by dividing by their length
  - my note: this means angle is scale-invariant

Algorithm:

<pre>
1) Split docs into words
2) Compute word frequencies (document vectors)
3) dot product
</pre>

They have around 8 different implementations of the same algo above.
Runtimes for these implementations on 2 docs of around 1MB:

1. 228.1s
2. 164.7s
3. 123.1s
4. 71.7s
5. 18.3s
6. 11.5s
7. 1.8s
8. 0.2s

Some of these improvements are algorithmic, some are better coding (improving the Θ(1) i.e. constants)

Implementation of Algo:

- Step 2 (this was discussed first):

  ```python
  for word in doc:
      count[word] += 1  # O(|word|), to reduce our word which can be really long down to a "machine word"
  ```

  - Takes O(Σ |word|) = O(|doc|)
    - linear time with high probability
  - another implementation:
    - sort the words
    - run through the sorted list and count words that occur in a row (identical words would be put together)
      - e.g. [a b a a c d b] -> [a a a b b c d]
      - can easily count them by running through the list once

- Step 1

  - `re.findall(r'\w+', doc)`
    - but `re` takes exponential time in general
    - `re` is not always linear time, so be careful in using it
  - scan through and look for alphanumerics

- Step 3 has a formula so it's implementation wasn't discussed I guess
