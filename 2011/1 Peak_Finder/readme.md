# Peak Finder

## One-Dimensional

Property: "Position i is a peak if and only if `arr[i] >= arr[i-1] and arr[i] >= arr[i+1]`"
<br> AKA look to your left, look to your right
<br> In general case, definition of peak may be different than "being greater"

<dl>

### Straightforward algo

<pre>Go through entire array to look for the peak
Worst Case: Θ(n)</pre>

### Divide and Conquer:

```python
if a[n/2] < a[n/2 - 1], look at 1...n/2 - 1
else if a[n/2] < a[n/2 + 1], look at n/2 + 1...n
else n/2 is a peak
```

<pre>
T(n) = T(n/2) + Θ(1)
base case: T(1) = Θ(1)
T(n) = Θ(1) + ... + Θ(1) = Θ(log(n))
       |---------------|
             log(n) times
</pre>

## Two-Dimensional

Property: "Position i is a peak if and only if `arr[i, j] >= arr[i-1, j] and arr[i, j] >= arr[i+1, j] and arr[i, j] >= arr[i, j-1] and arr[i, j] >= arr[i, j-1]`"
<br> AKA look to your left, right, up and down

<dl>

### Greedy Ascent

<pre>Starting from a point (i, j), look at (i-1, j), (i+1, j), (i, j-1) and (i, j+1) and pick direction with greatest value
Worst Case: Θ(nm), as it can end up touching all elements</pre>

### Divide and Conquer (1) (Efficient but Incorrect):

```python
Pick middle column j = m/2
Find 1D-peak at (i, j)
Use (i, j) as a start to find 1D-peak at row i
```

<pre>
Finding peak at column j = log(n)
Finding peak at row i = log(m)
Total = log(n) + log(m)

Problem: 2D Peak may not exist on Row i
</pre>

### Divide and Conquer (2):

```python
Pick middle column j = m/2
Find global max on column j at (i, j)
Compare (i, j-1), (i, j) and (i, j+1)
if (i, j-1) > (i, j), pick left columns
else if (i, j+1) > (i, j), pick right columns
else (i, j) is a 2D-peak
```

<pre>In the third condition, (i, j) is a 2D-peak as it's greater than or equal to (i, j-1), (i, j+1), and also (i-1, j) & (i+1, j) due to the first two steps

base case: T(n, 1) = Θ(n) <- work of finding max
        (There is a single column and we find the global max on that column)
T(n, m) = T(n, m/2) + Θ(n)
T(n, m) = Θ(n) + ... + Θ(n) = Θ(nlog(m))
          |---------------|
                log(m) times
</pre>
