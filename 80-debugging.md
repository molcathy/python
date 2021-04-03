# debugging
* debugging allows you to:
    - pause and resume your program as need it
    - look into what your program is doing e.g. what are the values of the variables at any step of the execution
* the 'manual' way of debugging to print out to the console messages like:
    - 'executing myFunction'
    - 'the value of myVar is {myVar}'
* debugging is useful when your program does not behave as expected and you need to understand why is so
* IDE (Integrated Development Environments) such as PyCharm and codding text editors such as VSCode come with built-in debuggers that let you track your program
* [VSCode debugging documentation](https://code.visualstudio.com/docs/editor/debugging)
* tutorials:
    - https://youtu.be/7qZBwhSlfOo

## terminology
**project**
: directory or folder

## actions
* continue: run the program until the next breakpoint
* step over: moves debugger to the next line of code
* step into: steps into the inner scope of the current object if any e.g. if your code executes a function the debugger moves inside that function
* step out of:
    - opposite of step into
    - steps out of current scope
    - if you are at the top level would step out of the program
* restart
* stop
* hoovering over vars during debugging shows their current value

## sections
* variables
* call stack
* watch
* breakpoints

## configurations
* first time when you start debugging in a project you should create a debugging configuration
* for the new configuration choose "Python Current File: Debug Current Python File"

## variables
* shows the value of variables in the program at the current execution point
* shows both global and local variables

## breakpoints
* can be:
    - added
    - activated/deactivated
    - removed
* pause the program execution
* give you a chance to manually execute the program step by step
* typically you would use them just before the line in the program you want to investigate
* you can use multiple breakpoints
* all available breakpoints are listed in the "BREAKEPOINTS" pane
* can be temporarily disabled in the "BREAKEPOINTS" pane
* without adding any breakpoints the program will run without pausing

## call stack
* lists:
    - all scoops e.g.:
        - num_doubler (a function)
        - main (the main function)
        - module
    - highlight the current scope of execution
    - shows scopes in the order in you are going to move into

## watch
* allows defining of vars or expression based
* the value of vars and expressions is going to be updated and displayed accordingly

## examples
* see `80-debugging/debugger.py`