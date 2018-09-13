Q7 : 구구단을 출력하는 프로그램을 작성하시오.

print "Willkommen zu 구구단 9x9 "
def gugudan():  
  a = import("Enter a number between 1 to 9: ")
  if a >= 1 and a <= 9 and type(a) == 'int':
    print "%s x %s is %s" % (a,x, a * x)
  else:
    print "Please enter an integer from 1 to 9, moron"
    gugudan()

gugudan()
  
