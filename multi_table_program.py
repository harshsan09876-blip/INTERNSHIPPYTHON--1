# build a multiplication table
# use range (1, 11)
# for i = 0;
# i will change from 1 to 10
# multiply a * i
# then display the result

a = int(input("Enter the number: "))

for i in range(1, 11):
    print(a, "x", i, "=", a * i)