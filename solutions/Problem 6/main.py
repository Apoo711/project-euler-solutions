def sum_square():
    sum_squares=0
    square_sum=0

    for i in range (1,101):
        sum_squares+=i*i
        square_sum+=i
    square_sum*=square_sum
    return square_sum-sum_squares

if __name__ == "__main__":
    print(sum_square())