def calc_palindrome(upper, lower):
    largest = 0
    for i in range(upper, lower - 1, -1):
        if i * i <= largest:
            break
            
        for j in range(i, lower - 1, -1):
            product = i * j
            if product <= largest:
                break
            if str(product) == str(product)[::-1]:
                largest = product
    return largest

if __name__ == "__main__":
    print(calc_palindrome(999,100))