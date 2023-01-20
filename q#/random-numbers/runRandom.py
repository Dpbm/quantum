import sys


if __name__ == '__main__':  
    args = sys.argv

    if(len(args) < 2):
        print("Usage: python runRandom.py total-of-bits") 
        sys.exit(1)

    bits = int(args[1])

    if(bits < 1):
        print("Usage: total-of-bits needs to be >= 1") 
        sys.exit(1)

    import qsharp
    from Random import randomize

    random_number = randomize.simulate(totalBits=bits)

    print(f"total bits: {bits}")
    print("min number: 0")
    print(f"max number: {2**bits - 1}")
    print(f"random number is: {random_number}")