# Largest Palindrome Product

## Problem

> A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is $9009=91\times 99$.  
> Find the largest palindrome made from the product of two 3-digit numbers.

## Solution

**[Code](./main.py)**  

The goal is to find the largest palindrome made from the product of two 3-digit numbers. Instead of checking every possible combination, I iterate downwards from the maximum possible value (999). This ensure that I encounter larger product earlier in the process, allowing me to prune the search space.

I used the following logic:

- I used two loops to multiply number `i` and `j`. By starting the inner loop at `j=i`, I avoided calculating the same product twice (e.g., $991\times998$ and $998\times991$), effectively cutting the work in half.
- I converted the product to a string and used Python's slicing syntax `[::-1]` to reverse it. If the string matches its reverse, it is a palindrome.

I then made the following optimisations:

1. Because I am iterating `j` downwards, once `i*j` becomes less than or equal to our current `largest`, we know that any further (smaller) `j` values will also produce smaller products. We break the inner loop immediately.
2. If the square of the current `i` ($i\times i$) is smaller than the `largest` palindrome found so far, it is mathematically impossible for `i` or any smaller number to produce a new record. The entire function gets terminated.

This means that while a standard brute-force check would perform nearly `810,000` iterations for 3-digit numbers, these early breaks allow the algorithm to finish after checking only a tiny fraction fo those combinations.
