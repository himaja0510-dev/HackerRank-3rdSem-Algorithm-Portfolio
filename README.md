# HackerRank 3rd Semester Algorithm Portfolio

## Student Information

| Details        | Information                            |
| -------------- | -------------------------------------- |
| **Name**       | Himaja G                               |
| **SRN**        | R25EF101                               |
| **Semester**   | 3rd Semester                           |
| **Branch**     | Computer Science and Engineering (CSE) |
| **University** | REVA University                        |
| **Location**   | Bengaluru, India                       |

## Profiles

* **HackerRank:** https://www.hackerrank.com/profile/himaja0510
* **GitHub Repository:** HackerRank-3rdSem-Algorithm-Portfolio

---

## About This Portfolio

This repository contains my solutions to five algorithmic problems completed as part of the 3rd Semester CSE HackerRank Algorithms & GitHub Coding Portfolio activity.

The portfolio demonstrates my understanding of fundamental problem-solving techniques including array processing, counting, insertion-based sorting, binary search, searching, sorting, greedy algorithms, and algorithmic complexity analysis.

All solutions were implemented in **Python** and tested before being added to this repository.

---

# Problems Completed

## 1. Mini-Max Sum

**Topic:** Arrays / Implementation

### Approach

The solution calculates the total sum of all elements and finds the minimum and maximum values. The minimum sum is obtained by subtracting the maximum element from the total sum, while the maximum sum is obtained by subtracting the minimum element.

### Complexity

* **Time Complexity:** O(N)
* **Auxiliary Space:** O(1)

### HackerRank

[Mini-Max Sum](https://www.hackerrank.com/challenges/mini-max-sum/problem)

### Solution

[View Solution](./01-Mini-Max-Sum/solution.py)

---

## 2. Birthday Cake Candles

**Topic:** Arrays / Counting

### Approach

The solution first finds the tallest candle using the maximum value in the array. It then counts how many candles have that maximum height.

### Complexity

* **Time Complexity:** O(N)
* **Auxiliary Space:** O(1)

### HackerRank

[Birthday Cake Candles](https://www.hackerrank.com/challenges/birthday-cake-candles/problem)

### Solution

[View Solution](./02-Birthday-Cake-Candles/solution.py)

---

## 3. Insertion Sort – Part 1

**Topic:** Sorting Algorithms

### Approach

The last element of the array is treated as the value that needs to be inserted into the already sorted portion of the array. Larger elements are shifted one position to the right until the correct position for the value is found.

### Complexity

For the single insertion operation required in Part 1:

* **Time Complexity:** O(N)
* **Auxiliary Space:** O(1)

### HackerRank

[Insertion Sort - Part 1](https://www.hackerrank.com/challenges/insertionsort1/problem)

### Solution

[View Solution](./03-Insertion-Sort-Part-1/solution.py)

---

## 4. Binary Search

**Topic:** Searching Algorithms

### Approach

Binary search is performed on a sorted array. The algorithm compares the target with the middle element and eliminates half of the remaining search space after each comparison.

If the target is smaller than the middle element, the search continues in the left half. If it is larger, the search continues in the right half.

### Complexity

* **Time Complexity:** O(log N)
* **Auxiliary Space:** O(1)

### HackerRank Search Evidence

An additional HackerRank searching problem, **Ice Cream Parlor**, was completed as supporting HackerRank evidence.

[Ice Cream Parlor](https://www.hackerrank.com/challenges/icecreamparlor/problem)

### Solution

[View Binary Search Solution](./04-Binary-Search/solution.py)

---

## 5. Mark and Toys

**Topic:** Greedy Algorithms / Sorting

### Approach

The toy prices are sorted in ascending order. The cheapest toys are purchased first because buying the least expensive toys maximizes the number of toys that can be purchased within the available budget.

### Complexity

* **Time Complexity:** O(N log N)
* **Auxiliary Space:** Depends on the sorting implementation

The sorting operation dominates the overall running time.

### HackerRank

[Mark and Toys](https://www.hackerrank.com/challenges/mark-and-toys/problem)

### Solution

[View Solution](./05-Mark-and-Toys/solution.py)

---

# Complexity Summary

| No. | Problem | Technique | Time Complexity | Auxi

