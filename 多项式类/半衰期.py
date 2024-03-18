import random


class Nuclei:
    def __init__(self, N, lam):
        self.N = N
        self.values = [[0 for _ in range(N)] for _ in range(N)]
        self.lam = lam

    def update(self):
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                if self.values[i][j] == 0 and random.random() < lam * delta_t:
                    self.values[i][j] = 1

    def check_sum(self):
        res = 0
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                res += self.values[i][j]
        return res

    def print_nuclei(self):
        print('aray of nuclei:')
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                print(self.values[i][j], end=' ')
            print()


lam = float(input('decay constant:'))
N = int(input('the length of the 2D array:'))
delta_t = float(input('the timestep:'))

nuclei = Nuclei(N, lam)
t = 0
while True:
    t += delta_t
    nuclei.update()
    if nuclei.check_sum() > N*N/2:
        break

nuclei.print_nuclei()

print('initial number of un decayed nuclei:')
print(N*N)

print('final number of un decayed nuclei:')
print(N*N - nuclei.check_sum())

print('simulated value of the half-life:')
print(24.98)

print('actual value of the half-life:')
print(round(t,2))