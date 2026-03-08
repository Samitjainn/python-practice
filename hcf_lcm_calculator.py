num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a = num1
b = num2

# HCF
while b != 0:
    temp = b
    b = a % b
    a = temp

hcf = a

# LCM
lcm = (num1 * num2) // hcf

print("HCF =", hcf)
print("LCM =", lcm)
