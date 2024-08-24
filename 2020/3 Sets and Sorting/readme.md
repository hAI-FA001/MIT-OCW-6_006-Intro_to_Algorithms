# Lec 3 - Sets and Sorting

## Set Interface

- Container
  - `build(A)`: build sequence from items in A
  - `len()`: return number of items
- Static
  - `find(k)`: return the stored item with key `k`
- Dynamic
  - `insert(x)`: add x to set or replace item with key `x.key` if it exists
  - `delete(x)`: remove and return the stored item with key `k`
- Order
  - `iter_ord()`: return the stored items one by one in key order
  - `find_min()`: return the stored item with smallest key
  - `find_max()`: return the stored item with largest key
  - `find_next(k)`: return the stored item with smallest key larger than `k`
  - `find_prev(k)`: return the stored item with largest key smaller than `k`

## Implementing Set Interface

### Unordered Array

- A giant array of the objects
- unordered -> store objects in no particular order
- `find(k)`
  - need to iterate through the array
  - `O(n)` in the worst case
  - other option is to sort it first and use binary search but that's discussed later
- all operations take `O(n)`
  - `build(A)`: takes `O(n)` to reserve `n` slots of memory, a/c to our model
  - `insert(x)`: even considering amortization, it takes `O(n)` because we also need to find if an element with `x.key` already exists or not

### Sorted Array

- Impose an order on the keys
- Asymptotic complexity:
  - Container operations: `O(nlg(n))`
    - tradeoff: building the array takes more time now
  - Static operations: `O(lg(n))`
    - we apply binary search, which takes `O(lg(n))`
  - Dynamic operations: `O(n)`
  - Order operations
    - `find_min/max()`: `O(1)`
      - because it's sorted
      - min is the first element, max is the last element
    - `find_prev/next(k)`: `O(lg(n))`

### Comparison

<table>
<thead><tr><th>Data Structure</th><th colspan="5">Operations O(.)</th></tr></thead>
<tbody>
<tr><td></td><td>Container</td><td>Static</td><td>Dynamic</td><td colspan="2">Order</td></tr>
<tr><td></td><td>build(A)</td><td>find(k)</td><td>insert(x)<br>delete(x)</td><td>find_min()<br>find_max()</td><td>find_prev(k)<br>find_next(k)</td></tr>
<tr><td>Array</td><td>n</td><td>n</td><td>n</td><td>n</td><td>n</td></tr>
<tr><td>Sorted Array</td><td style="background-color: darkred; color: white;">nlg(n)</td><td>lg(n)</td><td>n</td><td style="background-color: darkblue; color: white;">1</td><td>lg(n)</td></tr>
</tbody>
</table>

## Sorting

<pre>
In: Array "A" of "n" numbers/keys
Out: Sorted array "B"
</pre>

### Sorting Vocabulary

- Destructive: Overwrites input array
  - overwrites array `A` with a sorted version of array `A`
    - doesn't reserve new memory for sorted array `B` to then copy the elements into `A`: it directly modifies `A`
  - this is done in C++
  - e.g. dumbest destructive sort would be to call a non-destructive sort and copy it to `A`
    - would require `O(n)` space
- In-place: Uses `O(1)` extra space
  - destructive but also doesn't use extra memory
  - We can use variables
    - `O(1)` means the number of variables doesn't scale with the array's length

### Sorting Algorithms

#### Permutation Sort

```python
def permutation_sort(A):
    for B in permutations(A):
        if is_sorted(B):
            return B
```

##### Issues:

- Enumerate the permutations
  - for array of `n` elements, total permutations is `n!`
    - takes `Ω(n!)` i.e. at least `n!`
      - takes more time if, e.g., listing the permutations themselves takes `O(n)`
- Check if permutation is sorted

  - <pre>for i = 1 to n-1
        B[i] <=<sub>?</sub> B[i+1]</pre>
  - takes `Θ(n)`

- So, our algo takes `Ω(n! * n)`

- For our Sorted Array data structure, `build(A)` will take `Ω(n! * n)`

#### Selection Sort

##### Parts:

- Find biggest element with `index <= i`
- Swap
- Sort `1, ..., i-1`

##### Helper Functions:

```python
def prefix_max(A, i):
    if i > 0:
        j = prefix_max(A, i-1)
        if A[i] < A[j]:
            return j
    return i
```

Idea: Biggest element in `0, ..., i` is

- Either at index `i`
- or at index < `i`

###### Inductive Proof

- Inductive Hypothesis: Either max is at index `i` or < `i`
- Base case: `i = 0`
  - there's only 1 element and that element is the max
- Induction:
  - Assume I.H. is true for step `i-1`
  - Our algo gave the max in `0, ..., i-1`
  - We compare the max with element at `i` and return the greater of the two

###### Runtime

- `S(1) = Θ(1)`
  - If `i = 0` (only 1 element), algo just returns `i` -> `Θ(1)`
- `S(n) = S(n-1) + Θ(1)`
  - we call the algo recursively and do a constant amount of work
- We hypothesize that `S(n) =`<sup>`?`</sup>` cn`
  - By Substitution: `cn =`<sup>`?`</sup>` c(n-1) + Θ(1)`
  - `cn = cn - c + Θ(1)`
  - `1 = -c + Θ(1)`
  - `c = Θ(1) - 1`
  - `c = Θ(1)` (True, as this says `c` is a constant)

##### Algorithm

```python
def selection_sort(A, i=None):
    if i is None: i = len(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selection_sort(A, i-1)
```

##### Runtime

- `T(n) = T(n-1) + Θ(n)`

  - we call `selection_sort` on `i-1` and also call `prefix_max`
    - the `Θ(n)` swallowed the `Θ(1)` computations for swapping

- We know `1 + 2 + ... + n = Θ(n`<sup>`2`</sup>`)`
- `T(n)` is also doing `Θ(n) + Θ(n-1) + Θ(n-2) + ...`
- Hypothesize that `T(n) =`<sup>`?`</sup>` Θ(n`<sup>`2`</sup>`)`
  - `T(n) = cn`<sup>`2`</sup>
  - By Substitution: `cn`<sup>`2`</sup>` =`<sup>`?`</sup>` c(n-1)`<sup>`2`</sup>` + Θ(n)`
    - `cn`<sup>`2`</sup>` = cn`<sup>`2`</sup>` - 2cn + c + Θ(n)`
    - `0 = -2cn + c + Θ(n)`
    - `Θ(n) = 2cn - c` (True, as it says `Θ(n)` is an `O(n)` expression)

#### Insertion Sort

- Essentially, opposite of Selection Sort
- Also `O(n`<sup>`2`</sup>`)`

#### Merge Sort

```python
def merge_sort(A, a=0, b=None):
    if b is None: b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b)
```

- Compute middle index `c`
- Sort everything to the left of `c` and everything to the right of `c`

```python
def merge(L, R, A, i, j, a, b):
    # if start index of merged array A < end index of merged array A
    if a < b:
        # if there is no element in R or (there are elements in L and last element in L is greater than last element in R)
        if (j <= 0) or (i > 0 and L[i-1] > R[j-1]):
            A[b-1] = L[i-1]
            i = i -1
        # this branch is reached if there's no elements in L or last element in L is smaller than last element in R
        else:
            A[b-1] = R[j-1]
            j = j - 1
        merge(L, R, A, i, j, a, b-1)
```

- Run from end of `L = A[a:c]` and `R = A[c:b]` to the beginning
- In the merged array `A`, put the greater of `L[i-1]` and `R[j-1]`
- Then move the corresponding index
- `b` indexes the merged array `A`
  - this is where the element will be put

##### Runtime of merge

- `S(n) = S(n-1) + Θ(1)`
- From prev proof, `S(n) = Θ(n)`

##### Runtime of merge_sort

- `T(1) = Θ(1)`
  - array of length 1 is already sorted
- `T(n) = 2T(n/2) + Θ(n)`
  - algo makes 2 recursive calls on arrays of half the original length, and then calls `merge`
- Hypothesize that `T(n) =`<sup>`?`</sup>`Θ(nlg(n))`
  - `cnlg(n) = 2c(n/2)lg(n/2) + Θ(n)`
  - `cnlg(n) = cn(lg(n) - lg(2)) + Θ(n)`
  - `cnlg(n) = cnlg(n) - cnlg(2) + Θ(n)`
  - `0 = -cnlg(2) + Θ(n)`
  - `Θ(n) = cnlg(2)` (True, as it says Θ(n) is O(n), as `c` and `lg(2)` are constants)
