def solution():
    x=0
    for i in range(1000):
        if i%5==0:
            x+=i
        elif i%3==0:
            x+=i
    print(x)

if __name__ == "__main__":
    solution()