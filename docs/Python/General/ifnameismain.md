
  🏠 Home
  🐍 Python

# Using `if __name__ == "__main__"
Given two files:
`controlling.py`
```python
def controltest(func, x):
    for i in range(0, x):
        func(x)
if __name__ == "__main__":

    controltest(testfunc, 3)
```
`testing.py`
``` python
def testfunc(i):
    print("This is twice what you entered: ", 2 * i)
if __name__ == "__main__":
    testfunc("nice")

```
```bash
python controlling.py
This is twice what you entered:  6
This is twice what you entered:  6
This is twice what you entered:  6
python controlling.py
This is twice what you entered:  nicenice
```
* I had forgotten that you can pass a function to another function