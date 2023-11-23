w=int(input("enter your weight in kgs :"))
h=int(input("enter your height in cm :"))
a=int(input("enter your age in years :"))
de=10 * w + 6.25 * h - 5 * a + 5
c=w*1.7
print("your calorie intake :",de)
print("your protein intake :",c)
input("")