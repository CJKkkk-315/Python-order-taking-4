import matplotlib.pyplot as plt
x = [i/10 for i in range(-10,21)]
y = []
for i in x:
    if i < 0:
        y.append(i+1)
    elif 0 <= i <= 1:
        y.append(2*i+1)
    else:
        y.append(i**2+2*i)
plt.ylim(0,8)
plt.plot(x,y)
plt.show()