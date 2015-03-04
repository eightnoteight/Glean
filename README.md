# Glean
Glean is a simple script to improve the workflow of competitive programming.
It basically runs your code upon the input that has been embeded in the code
itself as a comment. It can run multiple testcases and print the output.
This Program doesn't print a character to the stdout, so that the output from
the code would be clear to understand.
I have designed this to automate the task in IDE's like vim, pycharm etc, in
which you can run this script with shortcut.
currently it supports running cpp, c, python.

## Instructions
All you have to do is keep the input between the start and end strings
specified in the config file, or just adapt to the defaults.


## python files
keep your input between "'''input" and "'''".

###example python file
```
#!/usr/bin/env python
'''input
hello input!
hello input!
'''
print repr(raw_input())
print repr(raw_input())
```
###output:
```
'hello world!'
'hello world!'
```

## cpp/c files
The lines between '/\*input' and '\*/' will be sent as stdin to a.out

###example c++ file
```
#include <bits/stdc++.h>
using namespace std;
/*input
hello input!
*/
int main(int argc, char** argv)
{
    string str;
    cin >> str;
    cout << str;
return 0;
}
```

###output:
```
hello input!
```
