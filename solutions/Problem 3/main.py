def original_solution(n) -> int:
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
        else:
            divisor += 1
    return n

def optimized_solution(n) -> int:
    while n % 2 == 0:
        n //= 2
    
    d = 3
    while d * d <= n:
        if n % d == 0:
            n //= d
        else:
            d += 2
    return n

if __name__ == "__main__":
    print(optimized_solution(600851475143))