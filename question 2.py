a = int(input("enter gross income "))
b = int(input("enter number of dependents "))
c = 10000
Taxable_Income = a-(c)-(b*3000)

Tax = (Taxable_Income)*0.2

print ("Tax is " + str(Tax)) 
