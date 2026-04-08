def approach_1(n):
    sum_squares=0
    square_sum=0

    for i in range (1,n+1):
        sum_squares+=i*i
        square_sum+=i
    square_sum*=square_sum
    return square_sum-sum_squares

def approach_2(n):
    sum_n = (n * (n + 1)) // 2
    square_sum = sum_n ** 2
    
    sum_squares = (n * (n + 1) * (2 * n + 1)) // 6
    
    return square_sum - sum_squares

if __name__ == "__main__":
    print(approach_1(100))
    print(approach_2(100))