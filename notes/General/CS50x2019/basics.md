<a href="../../../index.html">Go back to index</a>
<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
</head>

# Week 1

A few tidbits picked up from the intro on C. I'm not going to include too much on cpp since I don't have a compiler and it's probably too much trouble since I have access to an online compiler for the time being. 

* The curly braces encapsulate nested code similar to identation in Python.
* get_string is a user-defined function that is a wrapper around stdin
* `int main(void)` - no real counterpart to this in Python. `if __name__ == "__main__":` in Python is a related concept but not analogous either.
* floats and doubles can't represent numbers perfectly. For example, 2/10 which should be 0.2, has inaccuracies after 7 or 15 decimal points in the float and double data types, respectively. 
  
```cpp
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("What is your name?\n");
    printf("hello, %s\n", name);
}
```

For loops

```cpp
for (int i = 0; i < 50; i++)
{
  printf("Number %s", i)
}
```

function definitions - do a dummy reference to function so the main definition can go elsewhere.

```cpp

void do_thing(int n);

int main(void)
{
  int num = 2 + 2;
  do_thing(num);
}

void do_thing(int n)
{
  printf("Num is %s", n);
}
```

do-while loop

```cpp
int n = 0;
do
{
  n ++;
}
while (n < 10)
```
