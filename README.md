# Linear Regression
With python and without an incremental algorithm this time
![Regression](screenshot.png)

Fits a best fit line to a dataset of fish height vs weight from [Aung Pyae](https://www.kaggle.com/aungpyaeap/fish-market/data)

This is computed by solving a system of linear equations given by

![partial derivative of cost function w.r.t theta0](djdtheta0.png)
![partial derivative of cost function w.r.t theta1](djdtheta1.png)
set to zero, so as to find the minimum of the cost function J,
![cost function](cost.png),
where x<sup>i</sup> and y<sup>i</sup> denote the i<sup>th</sup> fish height and weight, respectively, not exponentiation.
resulting in the following system.
![resulting system](system.png)
The solution of this system gives a vector of thetas that fits a linear hypothesis function to the dataset of fish heights and weights
![h function](h.png)