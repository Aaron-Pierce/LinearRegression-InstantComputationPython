# Linear Regression
With python and without an incremental algorithm this time
![Regression](img/screenshot.png)

Fits a best fit line to a dataset of fish height vs weight from [Aung Pyae](https://www.kaggle.com/aungpyaeap/fish-market/data)

This is computed by solving a system of linear equations given by

![partial derivative of cost function w.r.t theta0](img/djdtheta0.png)
![partial derivative of cost function w.r.t theta1](img/djdtheta1.png)

set to zero, so as to find the minimum of the cost function J,

![cost function](img/cost.png)

where x<sup>i</sup> and y<sup>i</sup> denote the i<sup>th</sup> fish height and weight, respectively, not exponentiation.
resulting in the following system

![resulting system](img/system.png)

The solution of this system results a vector of thetas that fits a linear hypothesis function to the dataset of fish heights and weights, corresponding to the function

![h function](img/h.png)

which, in the context of this dataset, suggests an increase in weight of about 100 grams for every centimeter increase in height of Bream
