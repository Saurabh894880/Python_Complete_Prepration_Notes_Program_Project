#6. Write a python function which converts inches to cms.
def inchesToCm(n) :
    return n*2.54

inches=float(input("Enter the inch :"))
print(f"{inches} inches = {inchesToCm(inches)} cm.")