<a href="../../../../index.html">Go back to index</a>

<a href="../../base.html">Go back to Python Portal</a>

  

# Using pylab for plotting - tips and tricks

pylab as plt can be used in console or interactive windows. The plots will be overlaid, however, if we plot in this way: 

```python
import pylab as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [100, 200, 300, 400, 500]

plt.plot(x, y)
plt.plot(x, z)
plt.show()
```

![](Figure_1.webp)

Instead, we can plot in this way:

```
plt.figure("one")
plt.plot(x, y)
plt.figure("two")
plt.plot(x, z)
plt.show()
```
The final plt.show() call displays both figures simultaneously:

![](one.webp) ![](two.webp)

This way, each plot has its own scale depending on the range of the list. The way `plt.figure("name")` works is that it initializes it the first time it is called, and every subsequent time it changes the scope to the existing figure so any plt.function() calls are applied to the scoped figure - this is useful for labeling, titling, scaling, setting limits and so on. 

Some caveats:

* The figure window is persistent, so if a procedure was applied to a figure but then removed, the feature will stay. Remember to clear figures before redrawing using `plt.clf()`
* The colors are the same because each figure is independent and starts on the same default initial color

Other tips:

* use `label = "label name"` in `plt.plot()` in combination with adding `plt.legend(loc = 'upper left')` (loc is optional) to get a legend for each named curve
* use `plt.yscale('log')` to use log scale with powers of 10 as labels.

# Controlling more display parameters

* changing color or style of data sets (curves)
  * use matplot style syntax: for example, use `'ro'` to specify red points; use `'g--'` to specify a green dashed line, etc. 
* width of lines and displays
* using subplots
  * use `plt.subplot(rci)` where r (rows), c(columns) and i (index) are all digits. 

```python
plt.figure("one")
plt.clf()
plt.plot(x, y, "r--", linewidth = 10, label = 'test label')
plt.show()
```
![](one1.webp)

```python
plt.clf()
plt.subplot(121)
plt.plot(x, y, "b^", linewidth = 10, label = 'test label')
plt.subplot(122)
plt.plot(x, z, "go", linewidth = 10, label = 'test label 2')
plt.legend()
plt.show()
```

![](subplot.webp)