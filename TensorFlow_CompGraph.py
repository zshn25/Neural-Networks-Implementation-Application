%matplotlib inline
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


### Define a simple comp. graph (note that all its components are special TensorFlow objects)
# Specify an input x to the comp. graph
values = np.arange(-10.0,10.0,0.1)
_shape = values.shape
#x = tf.Variable([.3], dtype=tf.float32)
x = tf.Variable(values, tf.float32)

# Specify f(x) = x^2 + 2x + 5 
f_x = x**2 + 2*x + 5

# Take derivative of f with respect to x. That will be very important in the future, since you will only
# need to specify forward pass of your neural network, and all derivatives will be determined automatically by 
# TensorFlow.
derivative = tf.gradients(f_x, x)

### Execute the comp. graph
# Create a TensorFlow session
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# Evaluate the function value and its derivative for values from -10 to 10 with step 0.1
fx = sess.run(f_x, {x: values})
der = sess.run(derivative)
der = np.array(der).reshape(_shape) # Reshape the der to be same as values
    
# Plot the function f (use matplotlib library)
fig1 = plt.figure(1)
plt.plot(values, fx, label='f(x)')
plt.legend(loc='best')
fig1.show()

# Plot the derivative of the function f
plt.plot(values, der, label='derivative')
plt.legend(loc='best')
fig1.show()
