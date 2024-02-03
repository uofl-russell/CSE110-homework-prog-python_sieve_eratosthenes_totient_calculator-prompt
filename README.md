# Sieve of Eratosthenes and Euler's Totient Function
This assignment will demonstrate how to implement the Sieve of Eratosthenes and Euler's Totient Function from a very easy sequential Python3 implementation.  

# Product Owner Statement
As a person very interested in mathematics and the Python programming language I decided to create a simple program that will calculate the totient function for a given value. I believe I am close to completing my simple project but my code has an error in it.  I need your help and knowledge of the General Totient Function Formula to finish my project.

My code runs when I use the command line argument below:
```
python sieve_totient.py 600
```
I know my program should give the following:
```
There are 109 prime numbers less than 600
The totient function of 600 is 160
```
Unfortunately it prints out the following:
```
There are 109 prime numbers less than 600
The totient function of 600 is 0.2666666666666667
```

# Acceptance Criteria
The following must be implemented to receive credit for this assignment.

-  The code provided does not need to be altered significantly to complete the assignment. Before you start making changes make sure you read the code comments.  There may be hints on how to fix the program.
-  The final output for a totient value should be an integer and correct.

# Have Fun With it
Once you complete the assignment take a moment to recoginize the code is not optimized at all.  Yet it is still able to calculate a the totient value for very large values (and the required prime list to do it).  Try calculating the totient function for 100, then one million, and finally ten million.  Notice the time differences. Remember Python is very slow.  Just imagine implementing this with faster languages using optimizations.