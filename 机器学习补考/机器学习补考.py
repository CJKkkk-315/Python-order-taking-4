from scipy.optimize import minimize
import numpy as np
from scipy.special import gammaln
a = np.exp()
print(a)
def poissonRegressionNegLogLikelihood():
    pass
X = 0
y = 0
beta_start = 0
# Minimize the appropriate likelihood function
mle = minimize(poissonRegressionNegLogLikelihood, beta_start, args=(X,y),jac = True,method="Powell")
# Extract the maximum likelihood estimates from the optimizer.
betas = mle.
# gammaln()