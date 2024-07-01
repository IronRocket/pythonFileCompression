# What is it?
PythonFileCompression is a very simple compression tool that
removes comments and trailing spaces in a python file.

# Example

## Here is an uncompressed python file
### t.py
```python
# MIT license; Copyright (c) 2100-2101 Marie Curie
# Publication time -> 1719809516.1829143
# "Javascript is the collective failure of software developers represented in one programming language" - Marie Curie

import time # import time library

print(time.time()) #print the current unix time to the terminal
```

## Command
```bash
pythonFileCompression t.py
```


## Output
```python
import time
print(time.time())
```