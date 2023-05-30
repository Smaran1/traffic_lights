
import string
import random
import time
def main():
    l_alphabets = string.ascii_lowercase
    print(l_alphabets)
    u_alphabets = string.ascii_uppercase
    print(u_alphabets)
    symbols = string.punctuation
    print(symbols)
    number = "".join([str(num) for num in range(10)])
    print(number)
    
    randome_atleast = [random.choice(u_alphabets),
                    random.choice(l_alphabets),
                    random.choice(symbols),
                    random.choice(number)]

    listed = f"{l_alphabets}{u_alphabets}{symbols}{number}"

    remaining= random.sample(listed,10)


    combine = randome_atleast+remaining
    random.shuffle(combine)


    result  = ''.join(combine)
    print(result)



if __name__ == "__main__":
    while True:
        main()
        time.sleep(0.5)
