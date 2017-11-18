import matplotlib.pyplot as plt
# Evaluate the function value and its derivative for values from -10 to 10 with step 0.1
i = list(range(-100, 101))
f = list(range(-100, 101))
f_derivative_val = list(range(-100, 101))

for bla in i:
    x = bla/10
    # print(x)
    f[bla+100] = x**2 + 2*x + 5
    
    # Define f_derivative_val
    f_derivative_val[bla+100] = 2*x + 2

# Plot the function f
fig2 = plt.figure(2)
plt.plot(i, f, label='f(x)')
plt.legend(loc='best')
fig2.show()

# Plot the derivative of the function f
plt.plot(i, f_derivative_val, label='derivative')
plt.legend(loc='best')
fig2.show()
