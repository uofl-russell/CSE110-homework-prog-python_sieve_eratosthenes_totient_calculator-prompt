import sys #import the sys module to access command line arguments

#The function below creates a list of all primes less than n
def createPrimeNumberArray(n):
    primes = [] #create an empty list to store the prime numbers
    isPrime = [True] * n #create a list of n elements, all set to True
    for i in range(2, n): #iterate through the list of numbers from 2 to n
        if isPrime[i]: #check if i is prime
            primes.append(i) #add the prime number to the list
            #starting with i^2, mark all multiples of i as False 
            #(this is a shortcut to help avoid checking redundant multiples)
            for j in range(i * i, n, i): 
                isPrime[j] = False
    return primes

def totient(n, primes):
    #below calculates the result of the product of (1 - 1/p) for each prime p that divides n
    result = 1
    for prime in primes:
        if prime > n:
            break
        if n % prime == 0: # determine if prime evenly divides n
            result = result * (1 - 1 / prime)
    #At this point, the variable result is the product of (1 - 1/p) for each prime p that divides n

    return result  #<---------------THE ERROR IS RIGHT HERE!!! MAKE ONE SMALL CHANGE TO FIX THE ERROR.  

    #ONCE YOU FIX IT HERE ARE MORE HINTS TO FINISH THE PROGRAM
        #The totient function is supposed to return an integer value, not a floating point (decimal) value. 
        #You can use the int() function to convert the result to an integer before returning it.
        


#make sure the number of command line arguments is correct
numCommandArgs = len(sys.argv)
if numCommandArgs != 2: # the program name and the two arguments
    print("You must provide an integer (n) to be evaluated -> Usage: python sieve_totient.py n")
    sys.exit()

#make sure the command line argument is an integer greater than 2
n = int(sys.argv[1]) #get the integer from the command line
if n < 2: #make sure the integer is greater than 2
    print("The integer must be greater than 2")
    sys.exit()

#call the functions to create the prime number array and calculate the totient value
primeArray = createPrimeNumberArray(n) #create the prime number array
totientValue = totient(n, primeArray) #calculate the totient value
print("There are {0!s} prime numbers less than {1!s}".format(len(primeArray),n)) #print the number of primes less than n
print("The totient function of {0!s} is {1!s}".format(n,totientValue)) #print the totient value of n
