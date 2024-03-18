### BEGIN SOLUTION
from typing import Callable
def primitive(func:Callable[[float], float], epsilon:float=0.01) -> Callable[[float,float], float]:
    def riemann(a:float, b:float) -> float:
      i = a
      s = 0
      while i <= b:
        s += func(i)*epsilon
        i += epsilon
      return s
    return riemann
### END SOLUTION
import math

def one(x: float) -> float:
    return 1.0

def affine(x: float) -> float:
    return 2*x + 1

ONE = primitive(one, epsilon=0.5)
AFFINE = primitive(affine)
COSINE = primitive(math.cos, epsilon=0.001)

print(abs(ONE(1.0, 4.0) - 3.0) < 1e-2)
print(abs(AFFINE(3.0, 4.0) - 8.0) < 1e-2)
print(abs(COSINE(0.0, math.pi / 2.0) - 1.0) < 1e-2)