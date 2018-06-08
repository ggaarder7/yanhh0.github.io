# ggaarder.github.io
My Blog

## Wish List

[ ] 2018-04-05 View Raw/History: Link to glog repo
[ ] 2018-04-05 Render Equations in Markdown to MathML

SVM:
- how to get `b`?????
- Quadratic optimization
- Classification of images
- image segmentation
- recognize hand-written characters
- mathematically prove that SVM also holds on higher dimensions (than
  two)
- mathematically prove that '`w*xi - b >= 1` if and only if the point
  lies in the margin (so does `w*xi -b <= -1`)' also holds on higher
  dimensions (than two)
- SVC
- SVR
- Kernel trick

New words:
- tradeoff
- sufficiently
- Systolic BP?

- pattern recognition
- what model the curve in `2018-06-06_20-33-21.png` right is: special
  plot regarding to the chosen kernel function
- plot like `2018-06-06_20-33-21.png` right

- QR Code

Quotes in [SVM without
Tears][med.nyu.edu/chibi/sites/default/files/chibi/Final.pdf]:
- This tutorial is both *modest (it does not invent anything new)*

 [SVM without
 Tears][med.nyu.edu/chibi/sites/default/files/chibi/Final.pdf]:
- L2-norm is a typical way to measure length of a vector; *other
  methods to measure length also exist.* ??

diff:
- Hunt–McIlroy algorithm

- bsdgames
- dwarf fortress
- GTA
- Quake
- COD
- Half Life
  - CS
- War3
  - DotA

- graphviz
- xscreensaver-data-extra
  - xmatrix

# scipy
- Why 'jac'?
- `opt = {'disp':False}`: 'disp'?
- SLSQP?
- clf?

## svm.coef_?

Use the source luke!

![How can I know how to interpret the output coefficients (`coefs_`) from the model sklearn.svm.LinearSVC()? - Data Science Stack Exchange](https://datascience.stackexchange.com/questions/17970/how-can-i-know-how-to-interpret-the-output-coefficients-coefs-from-the-mode?newreg=ea4f8bf6fae44c458278877c84fad7d8)



> Here's one (admittedly hard) way.
>
> If you really want to understand the low-level details, you can always work through the source code. For example, we can see that the LinearSVC fit method calls _fit_liblinear. That calls train_wrap in liblinear, which gets everything ready to call into the C++ function train.
>
> So train in linear.cpp is where the heavy lifting begins. Note that the w member of the model struct in the train function gets mapped back to coef_ in Python.
>
> Once you understand exactly what the underlying train function does, it should be clear exactly what coef_ means and why we draw the lines that way.
>
> While this can be a little laborious, once you get used to doing things this way, you will really understand how everything works from top to bottom.

author: jncraton

*once you get used to doing things this way, you will really understand how everything works from top to bottom.*
