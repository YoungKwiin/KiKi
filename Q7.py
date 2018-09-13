# Q7 : 구구단을 출력하는 프로그램을 작성하시오.

def gugudan():
    while True:
        try:
            num = input("Enter a number between 1 to 9: ")
            if num == "q":
                exit()

            a = int(float(num))
            float_num = float(num)

            if a >= 1 and a <= 9 and a == float_num:
                for x in range(1,10):
                    print("%s x %s is %s" % (a,x, a * x))
                return
            else:
                print("Please enter an integer from 1 to 9, moron")
        except SystemExit:
            print('exiting the program')
            exit()
        except KeyboardInterrupt:
            print('\nhit control-c, exiting')
            exit()
        except:
            print("Invalid input. Please try again")


print("Willkommen zu 구구단 9x9")
gugudan()
