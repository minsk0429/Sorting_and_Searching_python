# Sorting_and_Searching_python

Algorithms implemented in Python (Sorting and Searching)

---

# Sorting Algorithms

## 📋 What is Sorting?

**Sorting** is the process of arranging elements in a particular order — typically ascending or descending. Sorting is a fundamental operation in computer science and improves the efficiency of other algorithms such as searching and merging.

---

## Basic Sorting Algorithms

### ✅ Selection Sort

- Repeatedly selects the minimum element and places it at the beginning.
- Time Complexity: O(n²)
- In-place, but not stable.

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

---

### ✅ Insertion Sort
- Builds the final sorted array one item at a time.
- Time Complexity: O(n²) worst, O(n) best (when nearly sorted)
- In-place and stable.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
```

---

### ✅ Bubble Sort
- Repeatedly swaps adjacent elements if they are in the wrong order.
- Time Complexity: O(n²)
- Simple but inefficient.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

---

## Sorting Use Cases

Data visualization and analysis
Preprocessing before binary search
Sorting names, numbers, objects by key
Improving human readability of data

---

# Searching Algorithms

## 📋 What is Searching?

**Searching** is the process of finding the location of a target value within a data structure. It is fundamental to many applications, including databases, compilers, and operating systems.

---

## Basic Searching Algorithms

### 🔍 Sequential (Linear) Search
- Checks every element until it finds the target.
- Time Complexity: O(n)

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

---

### 🔍 Binary Search
- Works only on sorted arrays.
- Repeatedly divides the search range in half.
- Time Complexity: O(log n)

```python
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

---

### 🔍 Interpolation Search
- Improves binary search by estimating the position of the target.
- Works well when elements are uniformly distributed.
- Time Complexity: O(log log n) best, O(n) worst

```python
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((target - arr[low]) * (high - low) //
                     (arr[high] - arr[low]))
        if pos >= len(arr):
            return -1
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
```

---

## Advanced Searching: Hashing

Hashing is a technique that maps data to a fixed-size table using a hash function. It allows constant-time average case insertion, deletion, and search.

### Hash Table (using Python dictionary)

```python
hash_table = {}
hash_table["apple"] = 5
print(hash_table["apple"])  # Output: 5
```

---

### Collision Resolution Strategies

When two keys hash to the same index (a collision), we resolve it with:

- Chaining: store multiple elements at a single index using a list
- Open Addressing: find another empty slot using methods like:
- Linear Probing
- Quadratic Probing
- Double Hashing

---

### Use Cases of Searching

- Looking up user records in databases
- Real-time search suggestions
- Keyword matching in documents
- Caching and memory management
- Symbol resolution in compilers

---

## 🚀 Summary

| Algorithm Type   | Name                | Time Complexity              | Data Requirements         | Notes                              |
|------------------|---------------------|-------------------------------|----------------------------|-------------------------------------|
| Sorting          | Selection Sort      | O(n²)                         | Unsorted data             | Simple, inefficient                 |
| Sorting          | Insertion Sort      | O(n²) worst, O(n) best        | Nearly sorted is fast     | Stable, in-place                    |
| Sorting          | Bubble Sort         | O(n²)                         | Unsorted data             | Mainly for educational purposes     |
| Searching        | Linear Search       | O(n)                          | Unsorted or sorted        | Very basic, slow on large datasets  |
| Searching        | Binary Search       | O(log n)                      | **Sorted** data required  | Fast and efficient                  |
| Searching        | Interpolation Search| O(log log n) best, O(n) worst| Uniformly distributed      | Better than binary in ideal cases   |
| Hashing          | Hash Table Lookup   | O(1) avg, O(n) worst          | Key must be hashable      | Collision resolution required       |

---
The attached codes are sorting and searching implemented in Python including Selection sort algorithm, insertion sort algorithm, bubble sort algorithm, insert, ==, union operation of a set using a sorted array, sequential search algorithm, binary search algorithm (recursive structure), interpolation search algorithm, example of hash function for string, insertion, search, deletion operation of linear search method, overflow handling using chaining.
