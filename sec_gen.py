import random
import string
import sys

def genKey(num):
    nums = []
    rng = random.SystemRandom()
    alpha = list(string.ascii_lowercase)
    num = int(num)

    for i in range(num):
        numlet = random.uniform(0, 1)
        if numlet >= 0.5:
            nums.append(rng.randint(1,10))
        elif numlet < 0.5:
            if numlet >= 0.25:
                nums.append(rng.choice(alpha).upper())
            else:
                nums.append(rng.choice(alpha))

    secret = ""

    for i in nums:
        i = str(i)
        secret += i
    print("\n" + secret + "\n")

def startMessage():
    message = """
    ~~~ SECRET GENERATOR ~~~
    -true random
    -unsaved
    -only built in dependencies (random, string)
    -can be run as a standalone script or used as a module
    -both takes a command line argument for the size of the secret and
    runs in the command line with user input choices
    """
    print(message)


def choices():
    choice = input("Choose the secret length: \n")
    quantity = input("Enter the quantity of keys: \n")
    for i in range(int(quantity)):
        genKey(choice)



startMessage()
# run loop
if __name__ == '__main__':
    choices()
