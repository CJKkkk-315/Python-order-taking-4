import pylab as plt

values = open('neuron_data.txt').read().split('\n')
values = [float(i) for i in values if i]

plt.barh([str(i) for i in range(len(values))], values)

plt.show()


x = [606, 759, 1024, 398]
y = [762, 639, 912, 591]

plt.scatter(x, y, color='red')
plt.show()
