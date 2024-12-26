def numbeOfBits(n):
    count = 0
    while (n):
      count += 1
      n >>= 1
    return count
number = int(input("enter your number : "))
print("tottal bits :",numbeOfBits(number))
