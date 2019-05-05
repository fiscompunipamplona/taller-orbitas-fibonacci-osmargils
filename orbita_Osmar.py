G=6.67e-11
M=1.989e30
pi=3.1416

r_p=float(input("digite el radio del perihelio"))
v_p=float(input("digite la velocidad del perihelio"))

v_a=(((2*G*M)/(v_p*r_p))+(((2*G*M)/(v_p*r_p))**2+4*((v_p**2-2*G*M)/r_p))**1/2)/2
r_a=(r_p*v_p)/v_a
d=(r_p+r_a)/2
f=(r_p*r_a)**(1/2)
T=(2*pi*d*f)/(r_p*v_p)
e=(r_a-r_p)/(r_a+r_p)

print("la velocidad del afelio es:" ,v_a)
print("el radio del afelio:" ,r_a)
print("el semieje mayor es:" ,d)
print("el semieje menor es:" ,f)
print("el periodo orbital es:", T)
print("la excentricidad orbital es:" ,e)

