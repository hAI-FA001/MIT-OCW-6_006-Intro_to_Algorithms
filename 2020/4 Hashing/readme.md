# Lec 4 - Hashing

- We will:
  - Prove that u can't `find(k)` faster than `O(lg(n))`
    - caveat: if we're in the restricted Model of Computation
  - Show how to `find(k)` faster than `O(lg(n))`
    - if we're no longer in that restricted MoC

## Comparison Model

- The stored objects are black boxes, and the only way to distinguish is to do a comparison on keys.
- The sort algos in prev lectures were comparison-based.
  - At some point, we compared 2 keys
- Operations: `=`, `<`, `>`, `>=`, `<=`, `!=`
  - All these only give 2 outputs: `True` or `False`
- For any algo, eventually, we need to perform comparisons to determine if the given key is stored in the set

  - This makes a binary tree
    - Each internal node is a comparison, which has 2 branches corresponding to `True` or `False`
    - The number of leaves is `n+1`
      - Number of items or the indices of the items
        - Algo needs to return an item or index of the item corresponding to the given key
      - Plus 1 if the item isn't there
        - Algo needs to be able to tell that the item doesn't exist
  - The height of this binary tree is `Θ(lg(n))`
    - This means our algo needs to do at least `lg(n)` comparisons to find out whether the key is in the set or not

- Even if each internal node had more than 2 branches, height is still bounded by a `log(n)`
- To improve on this, we need to be able to branch a non-constant amount
  - in RAM Model, we can go to any location in memory in `Θ(1)`
  - We can store item with key `k` at index `k-1`, then use random access to get it in `Θ(1)`

## Direct Access Array

- An item with key `k` is put at index `k-1` (`k`th place in the array)
- Now we can only insert 1 item with key `k`
  - Inserting again would replace it
  - This is also the semantics of our Set interface
- `find(k)` takes `Θ(1)`
- `insert/delete_at()` takes `Θ(1)`

### Why don't we all use this?

- We don't know how high the keys can be
  - If keys have 9 digits, then our array must span the entire space of 9 digits
  - Bad when `n < size of k`
- `build(X)`, `find_min/max/prev/next()` take a ton of time
  - `O(u)`, where `u >> n`

### Other limitations

- Our keys need to be integer or we can't use them as addresses
- To look up these keys in `Θ(1)`, we need to have `u < 2`<sup>`w`</sup>

## Improving the Data Structure

- If we had unique locations for all keys, it would take too much space i.e. `O(u)` where `u >> n`
- We want to map the space of our keys ( size `u`) to a compressed space (size `m = Θ(n)`)
  - need a function `h: {0, ..., u-1} -> {0, ..., m-1}`
    - maps from `0, ..., u-1` to `0, .., m-1`
- Our keys won't be directly used as indices
  - they'll first be passed through function `h` to map it to the compressed space

### Multiple Items in Same Place

- if `u > n`<sup>`2`</sup>, `n` of them will map to the same place (by pigeonhole principle)
  - so we can't avoid that 1 place will have more than 1 item
  - a bad function `h` would map all items to same place
- want a _hash function_ `h` that will evenly distribute the keys
- But we can't store 2 items in 1 memory location (2nd item will overwrite the first)
- 2 options:
  - choose `m` > `n` so there's extra space
    - so we find another place in the existing array to put the value
      - _"open addressing"_
        - notoriously difficult to analyze
      - python uses this
  - store a data structure in the _hash table_ (compressed space)
    - instead of storing the items, we store a pointer to another DS
      - these DS are called _"chains"_
    - for collisions, we'll store the items in the DS associated with that place
    - want to make our chains have small length

## Hash Functions

### Division Hash Function

- Easiest way to map to the compressed space
- Modulus operation
- `h(k) = k mod m`
- Good if our keys are uniformly distributed in the original space
  - this imposes a requirement on our distribution
- Python does this essentially
  - also jumbles the key for a fixed amount of jumbling
  - there's some sequence of inserts that give bad performance
    - the collisions will be large
    - they use this `h` for other reasons
      - like wanting a deterministic `h`
  - gives good performance when your data is sufficiently uncorrelated with `h`
    - this is usually the case

### Non-Deterministic Hash Functions

- With deterministic `h`, collisions are still there
- Non-deterministic means we pick `h` randomly
  - it's harder for the user to give bad inputs
- Can we choose `h` from the space of all `h`?
  - No, there are `m`<sup>`u`</sup> such functions
    - for each number in `u`, we have to pick from `m` functions
  - so we fix the family of `h`

### Universal Hash Function

- "Universal" is a descriptor
  - there can be many functions that are UHF
- Satisfies the universal hash property
- Example: `h`<sub>`ab`</sub>`(k) = (((ak + b) mod p) mod m)`
- This is 1 fixed function, we want to generalize it to a family of hash functions
  - `H(p, m) = { h`<sub>`ab`</sub>`(k) | a, b ∈ {0, ..., p-1} and a != 0 }`
  - parametrized by:
    - length of the hash function `m`
    - a fixed large prime `p` > `u`
      - picked randomly when making the hash table
  - we choose a random `a` and `b` from the given range
  - if `a = 0`, we'd lose the `k` information

#### Property of Universality

- `Pr`<sub>`h ∈ H`</sub>`{ h(k`<sub>`i`</sub>`) = h(k`<sub>`j`</sub>`) } <= 1/m, ∀ k`<sub>`i`</sub>` != k`<sub>`j`</sub>` ∈ {0, ..., u-1}`
- Says probability of collision is <= `1/m`, for any 2 different keys in my universe
  - if I randomly pick the keys and randomly choose a hash function
- It's kind of a measure of how well distributed it is
- By proving that `H` satisfies this property, we can show that the chain length is expected to be constant length

#### Proof for Chain Length Expected to be Constant

- define a random indicator variable `X`<sub>`ij`</sub> over choice `h ∈ H`
  - `X`<sub>`ij`</sub>` = 1 if h(k`<sub>`i`</sub>`) = h(k`<sub>`j`</sub>`), 0 otherwise`
  - means if these hashes collide then it's 1
- Size of chain at `h(k`<sub>`i`</sub>`)`=`X`<sub>`i`</sub>` = Σ`<sub>`j=0`</sub><sup>`n-1`</sup>` X`<sub>`ij`</sub>
  - size is number of collisions
  - sum is from `0` to `n-1` cuz we're storing `n` keys
- Expected value of size: `E`<sub>`h ∈ H`</sub>`{X`<sub>`i`</sub>`}`
  - `= E`<sub>`h ∈ H`</sub>`{Σ`<sub>`j=0`</sub><sup>`n-1`</sup>` X`<sub>`ij`</sub>`}`
    - put the definition of `X`<sub>`i`</sub>
  - `= Σ`<sub>`j=0`</sub><sup>`n-1`</sup>`E`<sub>`h ∈ H`</sub>`{X`<sub>`ij`</sub>`}`
    - linearity of expectation: expectation of sum of variables = sum of expectation of individual variables
    - assuming each `X`<sub>`ij`</sub> is independent
  - `= Σ`<sub>`j != i`</sub>`(E`<sub>`h ∈ H`</sub>`{X`<sub>`ij`</sub>`}) + 1`
    - original sum sums from `0` to `u-1`
    - this includes the term `X`<sub>`ii`</sub>
    - the probability of collision of `h(k`<sub>`i`</sub>`)` with itself is 1, so we factor that out
  - `= Σ`<sub>`j != i`</sub>`(1/m) + 1`
    - we used universality property i.e. probability of collision for `j != i` is `1/m`
    - the expected value is sum over `outcome * probability of outcome`
      - for `X`<sub>`ij`</sub>, this is `1 * 1/m + 0 * (1 - 1/m) = 1/m`
        - outcome is either `0` or `1` for indicator variables
        - and we know probability of `1` (a collision) is `1/m`
  - `= 1 + (n-1)/m`
  - This is the result of the universality property

##### Result

- As long as we choose `m = Ω(n)`, chain length is expected to be constant
- How to ensure this?
  - If we have fixed `m`, then `n` will become > `m` at some point
  - We can do the same thing as Dynamic Array: rebuild the hash table with new `m`
  - We can prove this rebuilding operation isn't done too frequently
