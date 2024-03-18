import matplotlib.pyplot as plt
import numpy as np


class MandelbrotSet:
    def __init__(self, max_iteration, x_min, x_max, y_min, y_max, gird_len):
        self.max_iteration = max_iteration
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.gird_len = gird_len
        self.gird = np.zeros((gird_len, gird_len))

    def check_all_point(self):
        x = np.linspace(self.x_min, self.x_max, self.gird_len)
        y = np.linspace(self.y_min, self.y_max, self.gird_len)
        xx, yy = np.meshgrid(x,y)
        z = xx + 1j * yy
        for i in range(len(z)):
            for j in range(len(z[0])):
                self.gird[i][j] = self.check_one_point(z[i][j])

    def check_one_point(self, c):
        z = 0 + 0j
        for i in range(self.max_iteration):
            z = z ** 2 + c
            if abs(z) > 2:
                return False
        return True

    def show(self):
        self.check_all_point()
        plt.imshow(self.gird)
        # plt.colorbar()
        plt.xticks(np.linspace(0, 512, 10), list(map(lambda x: round(x, 3),np.linspace(self.x_min, self.x_max, 10))))
        plt.yticks(np.linspace(0, 512, 10), np.linspace(self.y_min, self.y_max, 10))
        plt.show()


m = MandelbrotSet(255,-2.025,0.6,-1.125,1.125,512)
m.show()

