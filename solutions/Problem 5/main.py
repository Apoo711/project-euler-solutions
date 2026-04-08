import math
def approach_1():
    counter=2520
    while True:
        for i in range(20,10,-1):
            if counter%i!=0:
                break
        else:
            return counter
        counter+=2520

def approach_2():
    ans=1
    for i in range(1,21):
        ans=abs(ans * i) // math.gcd(ans, i)
    return ans

if __name__ == "__main__":
    print(approach_1())
    print(approach_2())