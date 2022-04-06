#sum of N natural numbers
from ex6 import factorial
def sumN(n):
  if(n==1):
    return 1
  else:
    return(n+sumN(n-1))

if __name__=='__main__':
  print("The sum of N natural numbers is:",sumN(5))
  print("The facotrial of n is:",factorial(5))
