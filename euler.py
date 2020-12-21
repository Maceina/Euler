import matplotlib.pyplot as plt
import numpy as np


# Given constantss
m = 10
v0 = 100
h0 = 30
k1 = 0.05
k2 = 0.01
g = 9.8


def h(t):
    global h_last, t_last

    h_current = h_last + v(t) * (t - t_last)
    h_last = h_current
    t_last = t

    return h_current


def v(t):
    global v_last

    v_current = v_last + a() * (t - t_last)
    v_last = v_current
    return v_current


def a():

    k = -k1 if v_last >= 0 else k2

    return ((v_last ** 2) * k - m * g) / m


steps = [1, 0.5, 0.1, 0.01, 0.001]
for step in steps:
    # Used for calculations
    v_last = v0
    a_last = 0
    h_last = h0
    t_last = 0

    x_range = np.arange(0, 40, step)
    y_range = [h(_x) for _x in x_range]

    y = [_y for _y in y_range if _y >= 0]
    x = x_range[:len(y)]

    print("[STEP=%.3f] Max height reached: %.2fm at %.2fs | Ground reached at %.2fs" % (step, max(y), x[y.index(max(y))], x[-1]))

    plt.plot(x, y, label=f'h(t) step = {step}')

plt.title("Projektinis aukštis laiko momentu")
plt.xlabel("t (s)")
plt.ylabel("h (m)")

plt.legend()
plt.show()