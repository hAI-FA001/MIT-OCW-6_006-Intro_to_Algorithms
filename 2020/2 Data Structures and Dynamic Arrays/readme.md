# Lec 2 - Data Structures and Dynamic Arrays

## Interface vs Data Structure

| Interface (API/ADT)                              | Data Structure                 |
| ------------------------------------------------ | ------------------------------ |
| What u want to do (Specification)                | How you do it (representation) |
| What data u can store                            | How to store data              |
| What operations are supported and what they mean | Algos to support them          |
| Think as problem statement                       | Think as algorithmic solution  |

## Main Interfaces

### Set

- We care about their values
- Not focus of this lecture

### Sequence

- We care about representing a particular sequence

- Care about the order

## Main DS Approaches

- Arrays
- Pointer-based

## Examples

### Static Sequence

- Maintain a sequence of items `x0, ..., x(n-1)`
- Number of items doesn't change
- The items themselves can change
- Operations:
  - `build(X)`: Make new DS for items in `X`
  - `len()`: Return `n`
  - `iter_seq()`: output `x0, ..., x(n-1)`
  - `get_at(i)`: return `x_i`
  - `set_at(i, x)`: set `x_i` to `x`
  - special cases of prev functions:
    - `get_first()`
    - `get_last()`
    - `set_first(x)`
    - `set_last(x)`
    - we care about this from an algorithms standpoint: we may be able to come up with more efficient algorithms for these cases than the one used in the generic functions

### Static Arrays

- The "Solution" to the Static Sequence interface problem/spec
- Remember the RAM Model
  - Memory is an array of w-bit words
  - "array" = consecutive chunk of memory
  - `arr[i]` means `memory[address of arr + i]`, so `i` acts as an offset
    - this access is `Θ(1)`
      - because RAM Model is assumed to work with w-bit words in `Θ(1)`
      - assuming "w" is at least lg(n)
        - word size "w" has to grow with "n"
        - need at least w = lg(n) to address 2<sup>w</sup> locations in `Θ(1)`
        - In real world, amount of RAM doesn't grow but here we have to think of it as growing asymptotically
- Invariant: `A[i] = x_i`
- `O(1)` time for:
  - `get_at`
  - `set_at`
  - `len` (we can store it along with its address)
  - `get_first`
  - `get_last`
  - `set_first`
  - `set_last`
- `O(n)` time for:
  - `build`
    - Why it takes linear time: Memory allocation model
      - Assume you can allocate an array of size "n" in `Θ(n)` time
      - Would also take `Θ(n)` to initialize the array to empty zeroes
      - In Memory Allocation Model, space is `O(time)`
  - `iter_seq`

### Dynamic Sequence

- Static Sequence, plus:
  - `insert_at(i, x)`: make `x` the new `x_i`, shifting ` x_i -> x(i+1) -> ... -> x(n-1) -> x(n``-1) `, where ` n`` = n+1 `
  - `delete_at(i)`: shift ` x_i <- x(i+1) <- ... <- x(n``-1) <- x_(n-1) `, where ` n`` = n-1 `
  - `insert_first(x)`
  - `insert_last(x)`
    - doesn't change indices
  - `delete_first()`
  - `delete_last()`

### Linked List

- Solution for Dynamic Sequence interface spec
- <pre>[x0|-]->[x1|-]-> ... ->[x(n-1)|/]</pre>
  - each Node has data and next ptr
  - last Node has `None` as its next ptr
- the next ptrs give us the order
  - the Nodes themselves are stored in arbitrary order in the memory
- the Linked List could just store `head` (ptr to first Node), `tail` (ptr to last Node) and `len`
- this is a Pointer-based DS
- we rely on the fact that pointers can be stored in 1 word, so we can dereference them in `Θ(1)`

#### Dynamic Sequence Operations Analysis

| Static Array                                               | Linked List                                        |
| ---------------------------------------------------------- | -------------------------------------------------- |
| `insert/delete_at(i)` costs `Θ(n)`                         | `insert/delete_first()` are `Θ(1)`                 |
| - Reason 1: Need to shift indices, esp. if `insert_at(0)`  | `get/set_at(i)` takes `Θ(i)` (`Θ(n)` worst case)   |
| - Reason 2: Need to allocate a new array of size n         | `insert_last()` takes `Θ(1)` if we maintain `tail` |
| - Reason 3: Also need to copy elements over into new array | `delete_last()` still takes `Θ(n)`                 |
| Great at random access, but not dynamic stuff              | Great at dynamic stuff, but not random access      |

### Dynamic Arrays

- List in Python
- Idea: Relax the constraint that `size(array) = n`
- Enforce `size(array) = Θ(n)` and `>= n`
  - size will be at most a constant times n, e.g. 2n, 11n, etc
  - we use 2n
- still maintain `A[i] = x_i`
- Visual: `[n | size | A -]----->[ x0 | x1 | ... | x(n-1) | blank | blank | ...]`
  - maintain another DS to store len `n` and ptr to array `A`
  - `size` is the actual size we allocated
  - `size` >= `n`
    - `size` is representation size
    - `n` is interface size
- `insert_last(x)`: set `A[n] = x`, `n += 1`, _unless n = size_

  - if `n = size`, allocate a new array of size `2 * size`
    - we need to pay `Θ(n)` cost of allocating like in static arrays, but now we only allocate a few times
    - if we used `new size = size + 5`, then we'd need to pay `Θ(n)` cost more often
      - this is still `Θ(n)` like in static array, but we're changing the constant factors in `Θ(n)`
  - on `n` calls to `insert_last(x)`:

    - resizing will occur at size=1, 2, 4, 8, 16, ...
    - so, resize cost = `Θ(1 + 2 + 4 + 8 + 16 + ...)`

      - `= Θ(Σ(2^i) from i=0 to lg(n))`
      - `= Θ(2`<sup>`(lg(n)+1)`</sup>` - 1)`
        - `Σ(2^i)` from i=0 to k = 2<sup>k+1</sup> - 1
        - think of it like:
          - `Σ(2^i)` is like setting first `k` bits to 1: `[0 0 0 0 0 1 1 ... 1 1 1 1]`
          - If we set `k+1`th bit: `[0 0 0 0 1 0 0 ... 0 0 0 0 ]`
          - and subtract 1: `[0 0 0 0 0 1 1 ... 1 1 1 1]`
          - We get the same thing as LHS
      - `= Θ(2`<sup>`(lg(n))`</sup>`)`
      - `= Θ(n)`

    - so, `n` calls give `Θ(n)` time, it's _kind of_ constant time

- if you insert and then delete "n" times, `size` would still be `Θ(n)`
  - deleting = decrease value of `n` (doesn't actually delete the array from memory)

## Amortization

- "Operation takes `T(n)` amortized time if any `k` operations take `<= k * T(n)` time"
- In Dynamic Arrays, `n` operations cost `Θ(n)` time => `O(1)` (constant) amortized time
- Amortize = averaging over the sequence of operations
  - For Dynamic Arrays, `insert_at(i, x)` is expensive if we insert near the end due to resizing (will take `Θ(n)` for this 1 operation), but most of the operations are cheap (`Θ(1)`)

## Summary

<table>
<thead>
<th>Data Structure</th>
<th colspan="5">Operation, Worst Case O(.)</th>
</thead>
<tbody>
<tr><td></td><td colspan="1">Static</td><td colspan="3">Dynamic</td></tr>
<tr><td></td><td>get_at(i), set_at(i, x)</td><td>insert_first(x), delete_first()</td><td>insert_last(x), delete_last()</td><td>insert_at(i, x), delete_at(i)</td></tr>
<tr><td>Array</td><td style="background: darkblue; color: white;">1</td><td>n</td><td>n</td><td>n</td></tr>
<tr><td>Linked List</td><td>n</td><td style="background: darkblue; color: white;">1</td><td>n</td><td>n</td></tr>
<tr><td>Dynamic Array</td><td style="background: darkblue; color: white;">1</td><td>n</td><td style="background: darkblue; color: white;">1<sub>(a)</sub></td><td>n</td></tr>
</tbody>
</table>
