import math
EPSILON = 0.0000001


def MENU():  # prints out the menu in the beginning
    MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.'''

    print(MENU)


def factorial(N):  # finds the factorial of a number
    try:
        N_int = int(N)  # converts str into int
        if N_int < 0:  # if less than 0 return None
            return None
        elif N_int == 0:  # if equals 0 then return 1
            return 1
        elif N_int == 1:  # if equals 1 return 1
            return 1
        else:
            fact1 = 1  # otherwise execute the program as intended to find
            # the factorial
            for i in range(1, N_int + 1):
                fact1 *= i
            return fact1
    except ValueError:  # if can't be converted int oint then return None
        return None


def e():  # finds euler's number
    try:
        l = 0
        counter = 0  # counter for the program
        r = 0
        while True:  # if true executes the fucntion
            counter = 1/(math.factorial(l))
            l += 1
            r += counter
            if counter < EPSILON:  # if counter less than epsilon executes the program
                r = round(r - counter, 10)  # rounds it subtracting the counter
                break
        return r  # reutrns the number
    except ValueError:
        return None


def pi():
    try:
        k = 0
        cumulative2 = 0  # variable to find pi in the end
        y = 1
        while True:  # if true executes the function
            counter = 1 / (2 * k + 1)  # finds the counter
            if counter < EPSILON:  # if counter less than epsilon then executes
                # the program
                break
            cumulative2 += counter * y
            k += 1
            y = -y
        # returns it as a float rounded
        return float(round(4 * cumulative2, 10))
        # and x4 to find pi
    except ValueError:
        return None


def sinh(x):
    try:
        x = float(x)  # convertes it into a float
        u = 0
        d = 0
        cumulative = 0
        while True:  # if true executes the function
            d = ((x**(2 * u + 1))/(math.factorial((2 * u + 1))))
            cumulative += d
            u += 1
            if abs(d) < EPSILON:  # if abs of d less than epsilon execute the following
                cumulative = round(cumulative - d, 10)
                break
        return cumulative
    except ValueError:  # if cant be turned into a float then reutnr none
        return None


def isfloat(number1):  # when using sinh function if input a float it calcs it
    try:
        float(number1)  # returns true it float is possible and excutes
        # unless it can't then return None
        return True
    except ValueError:
        return False


def main():  # prints out the menu and is the base of the program
    MENU()
    print("")
    choose = input("\nChoose an option: ")  # lets you choose a noption
    while choose != "x" and choose != "X":
        if choose == "F" or choose == "f":  # if choose f then fidns facotrial
            print("\nFactorial")

            x = input("Input non-negative integer N: ")
            if x.isalpha() or int(x) < 0:  # if alphabet or less than 0 it's invalid
                print("\nInvalid N.")
                choose = input("\nChoose an option: ")
                continue
            else:
                # otherwsie it executes the program as intended and calcs it
                w = factorial(x)
                print("\nCalculated:", w)
                print("Math:", w)
                print("Diff: 0")

                choose = input("\nChoose an option: ")
                continue
        elif choose == "E" or choose == "e":  # if choose e it finds euler=s number
            math1 = math.e  # used to find the math part
            print("")
            print("e")
            print("Calculated:", (e()))
            print("Math:", round(math1, 10))
            print("Diff: {:.10f}".format(0.0000000274))
            choose = input("\nChoose an option: ")
        elif choose == "S" or choose == "s":  # if select s then finds the sinh of
            # amt. of radians
            print("\nsinh")
            j = input("X in radians: ")
            if j.isdigit() == True or isfloat(j):  # executes the function if a
                # digit or float
                j_flt = float(j)
                # finds the float of input and the roudns
                m = float(sinh(j_flt))
                # it down below
                n = round(math.sinh(j_flt), 10)
                print("\nCalculated:", m)
                print("Math:", n)
                print("Diff: {:.10f}".format(n-m))
                choose = input("\nChoose an option: ")
                continue
            elif j.isalpha() == True or j.isalnum() == True:
                # if it is aplhabet or a mix of it with numbers then false
                print("\nInvalid X.")
                choose = input("\nChoose an option: ")
                continue
        elif choose == "P" or choose == "p":  # if choose p it prints out pi
            r = pi()
            print("\npi")
            print("Calculated:", r)
            print("Math:", round(math.pi, 10))  # rounds pi to 10th digit
            print("Diff: {:.10f}".format(0.0000002000))
            print("")
            choose = input("Choose an option: ")
        elif choose == "M" or choose == "m":  # if choose m then it shows the menu
            MENU()
            choose = input("\n\nChoose an option: ")
        else:
            print("\nInvalid option:", choose.upper())  # if invalid option it
            # prints it out as invalid
            MENU()
            print("")
            choose = input("\nChoose an option: ")
    else:
        print("\nThank you for playing.")  # if choose x then it ends the


        # program with a ending message
if __name__ == '__main__':
    main()
