# pytest-blue

A pytest plugin that one fixture:

* blue

This fixtures can be used to `print` a string in blue.
It will also report the test file and function.

And it works even when pytest is capturing output.

Example **test_example.py**: 

```
def test_blue(blue):
    blue('should be blue')
```
