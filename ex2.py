# Parameterized functions
def mult(x,y=10,z=12):
  multiply=x*y*z
  print("The product of {a} * {b} * {c} is {d}".format(a=x,b=y,c=z,d=multiply))

if __name__=='__main__':
  mult(x=6,y=5,z=10)