# !/Python

import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
y = (1, 3, 5, 7, 9, 11)
x = range(len(y))

plt.plot(x, y, 'b-')

plt.show()


import pylab as pl
y = (1, 3, 5, 7, 9, 11)
x = ['A', 'B', 'C', 'D', 'E', 'F']
z = (11, 0, 7, 5, 3, 1)
a, = pl.plot(x, y, 'r-')
b, = pl.plot(x, z, 'b-')
pl.xlabel('x axis')
pl.ylabel('y axis')
pl.title('Plot of y vs. x')
pl.legend([a, b], ('red line', 'green circles'), numpoints=1)# make legend
savefig('foo.png')
pl.show()

import pylab as pl
def plot_ma(TITLE, MA5, MA10, DATE):
    pl.title(TITLE)
    a, = pl.plot(DATE, MA5, 'r-')
    b, = pl.plot(DATE, MA10, 'b-')
    pl.legend([a, b], ('MA5', 'MA10'), numpoints=1)
    pl.savefig('stock/%s.png' % TITLE)
    print('Plot %s success' % TITLE)
pl.show()
