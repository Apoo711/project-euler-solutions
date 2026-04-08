# Smallest Multiple

## The Problem

> 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
> What is the smallest positive number that is **evenly divisible** by all of the numbers from 1 to 20?

## The Solution

**[Code](./main.py)**

The goal is to find the Least Common Multiple (LCM) of the number 1 through 20. The two approaches demonstrate the difference between iterative searching and using number theory.

### Approach 1

Instead of checking every single number (1,2,3..), this approach use a leap-frog method.

- I know the answer must be a multiple of the smallest multiple for 1 through 10, which si 2520. By incrementing the `counter` by 2520 in each step, I skip thousands of unnecessary checks.
- The `for` loop checks divisors from 20 down to 11. I stopped at 11 because any number divisible by 11-20 is automatically divisible by 1-10 (e.g., if it's divisible by 20, it's divisible by 2, 4, 5, and 10)
- Checking the largest divisors first (20,19,18...) is faster because numbers are more likely to fail those checks early, allowing the loop to `break` sooner.

### Approach 2

This approach is mathematically optimal, finding the answer in a single pass without any guessing.

- The Least Common Multiple of two number $a$ and $b$ can be found using their Greatest COmmon Division (GCD):

$$
LCM(a,b)=\dfrac{\lvert a\times b\rvert}{gcd(a,b,)}
$$

- The code calculates the LCM of 1 and 2, then the LCM of that result and 2, and so on, all the way up to 20.
- This is $O(n)$ where $n$ is the upper limit. It is nearly instantaneous regardless of how large the target range becomes.

*[Formula Source](https://mathworld.wolfram.com/LeastCommonMultiple.html#:~:text=(-,13,-))*

---
While Approach 1 is clever, its runtime depends on how far away the answer is. Approach 2's runtime depends only on how many numbers are in the range, making is significantly more scalable for larger problems.
