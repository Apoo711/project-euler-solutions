# Sum Square Difference

## The Problem

> The sum of the squares of the first ten natural numbers is,

$$
1^2+2^2+\dots+10^2=385
$$

>The square of the sum of the first ten natural numbers is,

$$
(1+2\dots+10)^2=55^2=3025
$$

> Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025-385=2640$. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## The Solution

**[Code](./main.py)**

The Objective is to find the difference between the square of the sum of the first $n$ natural numbers and the sum of squares of those same numbers.

### Approach 1

This is the most straightforward method. It uses a single for loop to traverse every number from 1 to $n$, accumulating the two total simultaneously.

- Pros: Very readable and requires no prior mathematical knowledge.
- Cons: As $n$ grows larger, the number of operations increases linearly. If $n$ were in the billions, this would take several seconds (or longer) to compute.

### Approach 2

This approach bypasses the loop entirely by using closed-form summation formulas.

- Sum of the first $n$ numbers: Known as the Triangle number formula (or Gaussian Sum):

$$
\sum^n_{i=1}i=\dfrac{n(n+1)}{2}
$$

- Sum of the first $n$ squares: Known as the Square Pyramidal Number Formula:

$$
\sum^n_{i=1}i^2=\dfrac{n(n+1)(2n+1)}{6}
$$

- Because these are simple algebraic expressions, the computer only performs a handful of multiplications and divisions regardless of how large $n$ is. This is known as constant time complexity.

*[Formula 1 Source](https://mathworld.wolfram.com/PowerSum.html#:~:text=(-,31,-))*  
*[Formula 2 Source](https://mathworld.wolfram.com/PowerSum.html#:~:text=(-,32,-))*

---

In Project Euler, you will often that "Brute Force" (Approach 1) works for the specific limit given in the problem, but "Mathematical Insight" (Approach 2) is what allows you to solve much larger version of the same puzzle.
