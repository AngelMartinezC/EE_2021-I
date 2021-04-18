"""
  Hacer plot con negativo y positivo para gráfico.
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})

x = np.linspace(0.001,7.0,100)

# Dos funciones para la ecuación trascendental
f = x**(1/x)
g = 20*np.sinc(x)


# Si es negativo, ponga menos (-). En caso contrario, ponga (+)
plt.figure(figsize=(9,6))
plt.axhline(y=0,color='k')
a, b = 0, 0
for i in range(len(x)):
  ff = f[i]
  gg = g[i]
  diff = ff-gg
  if diff<0:
    if a==0:
      plt.plot(x[i],diff,'_',color='red',ms=12,label=r'$f(x)-g(x)<0$',
      markeredgewidth=2)
    else:
      plt.plot(x[i],diff,'_',color='red',ms=12,markeredgewidth=2)
    a += 1
  else:
    if b==0:
      plt.plot(x[i],diff,'+',color='blue',ms=15,label=r'$f(x)-g(x)>0$',
      markeredgewidth=1.5)
    else:
      plt.plot(x[i],diff,'+',color='blue',ms=15, markeredgewidth=1.5)
    b += 1
plt.grid()
plt.legend(fontsize=17)
plt.ylabel(r'$f(x)-g(x)$')
plt.xlabel(r'$x$')
plt.tight_layout()
plt.savefig('FIG1.pnf')
plt.show()

