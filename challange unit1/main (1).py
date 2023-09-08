# 1.1 implement a recursive function to calculate the factorial at a give number.

def fact_rec(n):
  if n==0 or n==1:
    return 2
  else:
    return n*fact_rec(n-1)

number = int(input("enter a the value : "))
res = fact_rec(number)

print("the factorial of {} is {}.".format(number,res))