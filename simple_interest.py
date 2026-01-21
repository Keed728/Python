"""
simple interest= (P*R*T)/100
p=principal amount
r=rate of interest
t=time duration

"""
principal = float(input("enter the principal amount"))
rate = float(input("enter the rate of interest"))
time=float(input("enter the time duration"))
si=(principal*rate*time)/100
print("simple interest",si)