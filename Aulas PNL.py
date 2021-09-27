##Lista de exercícios 2
## Minimizar as funções abaixo a partir dos subgradientes
#a)f(x,y) = max{3x^2 + y^2, x+y+5}
#b) f(x,y) = max{x^2 + y^2, |x-2y|+1}
#c) f(x) = max{||x||, Exi + 5}

import matplotlib.pyplot as plt
import numpy as np
import pyuo.tools as tt

##letra a

def fun_a(x):
    if 3 * x[0] * x[0] + x[1] ** 2 > x[0] + x[1] + 5:
        val = 3 * x[0] * x[0] + x[1] ** 2
    else:
        val = x[0] + x[1] + 5
    return val

fig = plt.figure()
ax = fig.gca()
tt.plot(fun=fun_a, x=[-2,2], ax=ax, curves=True)
fig


#laboratorio dia 22/09/2021

