#theory of relativity - an introduction

# E = mc$$2
import numpy as np ## linear algebra library
import matplotlib.pyplot as plt
c = np.linspace(0., 1., 100)
m = 1
e = m * c **2
E
%matplotlib inline
plt.plot(c,E)