# Multiples of 3 or 5

**The Problem:**
> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
> Find the sum of all multiples of 3 or 5 below 1000.

**The Solution:** 
[Code](./main.py)

We begin by defining our `main()` function. Inside, we initialize a variable `x` to act as an accumulator for the sum of the multiples.  

A for loop is used to iterate through all integers from `0` up to (but not including) `1000`. For each number, we use the following logic:

- We first check if the number is divisible by `5`; if it is, we add it to our total.

- If it is not divisible by `5`, we then check if it is divisible by `3`.

By utilizing an `elif` statement, we avoid counting the same number twice. For example, since `15` is a multiple of both `5` and `3`, an `elif` ensures it is added to the sum only once when the first condition is met. Finally, we print the total value of `x`.
