# Parameterized functions with return
def mult(x,y=10,z=12):
  multiply=x*y*z
  return multiply

if __name__=='__main__':
  print("The product is:",mult(2,10,12))