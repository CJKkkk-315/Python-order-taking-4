import math
v0 = float(input('v0:'))
R = float(input('R:'))
P = float(input('P:'))
C = float(input('Cd:'))
m1 = float(input('m1:'))
m2 = float(input('m2:'))
g = 9.8
H = math.pi * R ** 2
k = 0.5*P*C*H
f = k*v0**2
L1 = 0.5 * (m2*g*k/m1) ** 0.5 * (v0**4 + 4*k/(m1*v0**2)) ** 0.5
L2 = 0.5 * (m2*g*k/m1) ** 0.5 * ((v0**4 + 4*k/(m1*v0**2)) ** 0.5 - v0**2)
L3 = 0.5 * (m2*g*k/m1) ** 0.5 * ((v0**4 + 4*k/(m1*v0**2)) ** 0.5 + v0**2)
print('L1:',L1)
print('L2:',L2)
print('L3:',L3)
