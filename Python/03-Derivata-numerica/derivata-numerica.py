# %%
#Function to analyze
def f(x):
    return (x**3+5*x**2+3*x-6)

#Numerical approximation of derivative
def numerical_derivative(x, derivative_precision=0.01):
    return (f(x+derivative_precision)-f(x))/derivative_precision


x=2
f_value=f(x)
f_derivative=numerical_derivative(x)
print("The derivative of f(x) at ({},{}) is approximatively {:.3f}".format(x,f_value, f_derivative))
# %%
