def find_num():
    num_found = False
    counter=2520
    num_works = False
    counter2=0
    while num_found==False:
        for i in range(1,20):
            if counter%i!=0:
                num_works = False
            else:
                num_works = True
                counter2+=1
        if num_works and counter2==20:
            num_found = True
        else:
            num_found = False
            counter+=1
    return counter

if __name__ == "__main__":
    print(find_num())