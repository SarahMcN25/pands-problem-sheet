# this program displays a plot of functions f(x)=x, g(x)=x² and h(x)=x³ in range [0, 4]
# on one set of axes
# Author: Sarah McNelis

import numpy as np 
import matplotlib.pyplot as plt 

xpoints = np.array(range(0, 4))
yOne = xpoints
yTwo = xpoints * xpoints
yThree = xpoints * xpoints * xpoints

plt.plot(yOne, yTwo, yThree,) # add color here
plt.title('Functions')
plt.legend()
plt.show()
