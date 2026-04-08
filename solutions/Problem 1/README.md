# Multiples of 3 or 5
  
## The Problem

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.  
> Find the sum of all multiples of 3 or 5 below 1000.

## The Solution

**[Code](./main.py)**

The goal is to find the sum of all natural umbers below `1,000` that are multiples of either 3 of 5. This is a classic "FizzBuzz" style logic problem where the primary challenge is ensuring that numbers divisible by both 3 and 5 (like 15, 30, and 45) are not counted twice.

I used the following logic:

- I used a `for` loop to check every integer form 0 up to 999.
- I used the modulo operator to check for divisibility. If `i%5==0`, the number is a multiple of 5.
- By using an `if` statement for 5 and an `elif` (else if) for 3, we ensure that if a number is divisible by 5, it is added to the total and the program immediately moves to the next number. This prevents multiples of 15 from being added twice, once for the 3 check and once for the 5 check.

The function has the following complexity:

- A time complexity of $O(n)$, where $n$ is the upper limit. The program performs one operation per number in the range.
- A space complexity of $O(1)$, as I only store a single integer (`x`) regardless ogf how large the range becomes.
