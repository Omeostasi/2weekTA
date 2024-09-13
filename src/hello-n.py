
# this asks the user for a number and turns the answer
# into an integer
n = int(input("How many times should I loop?\n "))

# Now, print "Hello, World!" n times.
for x in range(n):
    print('Hello, World!')

x= input('do you want to stop?\n')
while x != 'yes': #!= means 'different'
    x=input('do you want to stop?\n')    
