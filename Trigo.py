from matplotlib import pyplot as plt
import math

def sin(x):
    l = math.radians(x)
    return math.sin(l)
def cos(x):
    l = math.radians(x)
    return math.cos(l)
def tan(x):
    l = math.radians(x)
    return math.tan(l)
def sec(x):
    c = cos(x) 
    if c == 0:
        return float('nan') 
    return 1 / c
def cosec(x):
    s = sin(x)
    if s == 0:
        return float('nan')
    return 1 / s
def cot(x):
    t = tan(x)
    if t == 0:
        return float('nan')
    return 1 / t

x_values = []
y_values_sin = []
y_values_cos = []
y_values_tan = []
y_values_sec = []
y_values_cosec = []
y_values_cot = []

for x in range(-3600,3610):
    x_values.append(x)
    y_values_sin.append(sin(x))
    y_values_cos.append(cos(x))
    y_values_tan.append(tan(x))
    y_values_sec.append(sec(x))
    y_values_cosec.append(cosec(x))
    y_values_cot.append(cot(x))


m = ['sin', 'cos' , 'tan' , 'sec' , 'cosec' , 'cot']
for i in m:
    plt.plot(x_values,globals()['y_values_'+i])

plt.grid(True)
plt.ylim(-10,10)
plt.xlim(-360,360)
plt.show()


