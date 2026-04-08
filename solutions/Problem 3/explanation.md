# Largest Prime Factor

## The Problem

> The prime factors of 13195 are 5,7,13 and 29.  
> What is the largest prime factor of the number 600851475143?

## The Solution

**[Code](./main.py)**

To find the largest prime factor, we repeatedly divide the number $n$ by its smallest possible divisor. Every time we find a divisor, we reduce $n$ by dividing it, effectively stripping away its smaller prime factors. By the time the loop finishes, the remaining value of $n$ is the largest prime factor.

I used the following logic:

- Any integer greater than 1 is either a prime number of can be represented as a product of prime numbers.
- If a number $n$ has a divisor, at least one of those divisors must be less than or equal to $\sqrt{n}$. This is why I use the condition `d*d<=n` (which is the same as $d\geq\sqrt{n}$). Once $d$ exceeds the square root, what is left of $n$ must be prime.

I then made the following optimisations:

1. It handles the number 2 as a special case first. Since 2 is the only even prime, we can remove all factors of 2 at the start.
2. After removing all factors of 2, the code only checks odd numbers as potential divisors (`d+=2`). This cuts the number of iterations in the loop by 50%.

This means that instead of checking every number up to `600,851,475,143`, the loop only needs to check numbers up to the updated square root of the reducing $n$. For large numbers with small prime factors, this happens almost instantaneously.
