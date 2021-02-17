def d2b(num) :
    if num>1:
        d2b(num//2)
    print(num%2 , end='')

dec_val=int(input("Enter the num: "))
d2b(dec_val) #to call the user define function
print()
