<a href="../../../index.html">Go back to index</a>
<a href="../base.html">Go back to General topics portal</a>

  

# Interesting Python snippets

```python
x = 2
y = 3
print(f"x + y = {x + y}")
```

You can pass command line arguments using the argv module. E.g. 

```python
from sys import argv 
print(argv)
```

In the command line:

```bash
python myargvfile.py var_name
```

To switch two values, simply use

```python
x, y = y, x
```

Formatting strings can use a shorthand:

```python
print(f"x equals {x}")
```
