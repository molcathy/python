# python
Using this repository to document my work of teaching Catherine Python including any tools she might need to learn Python.

## non-python topics
* shells - terminals
* brew macOS package manager
* text editors
* markdown
* git - github

## python topics
* virtual environments
* pip
* functions
* testing

## shells - terminals
### shells
* [shells](https://en.wikipedia.org/wiki/Shell_(computing)) are programs that allow users to interact with the operating system
* are named shells because it is the outermost layer around the operating system
* shells use either:
    - a command-line interface (CLI)
    - or graphical user interface (GUI)
* for the purpose of this tutorial when we are going to refer to shells we are going to refer to cli shells
* the shell is both an interactive command language and a scripting language
* for now will focus on the interactive of the shell
* there are many flavours of shells 2 of the most popular being:
    - bash: in most cases the default Linux shell, and on older versions of macOS
    - zsh: the default shell of the latest macOS (Big Sur)
* many aspects of bash and zsh are similar and for the purpose of this tutorial we are going to ignore their differences

### terminals
* [terminal emulators](https://en.wikipedia.org/wiki/Terminal_emulator) are computer programs that emulate [video terminals](https://en.wikipedia.org/wiki/Computer_terminal#Dumb_terminals)
* for the purpose of this tutorial when we are going to refer to terminal emulators as terminals
* your terminal lets you interact with your shell which through commands lets you interact with your operating system to perform various tasks e.g.:
    - creating, copying, moving, renaming, removing files and directories
    - download stuff
    - launch programs
* the most popular terminals are:
    - terminal: comes by default with macOS
    - [iTerm2](https://iterm2.com/): a very good replacement for the MacOS terminal

### terminal - shell - os
* basically `terminal --> shell --> commands --> operating system`
* to find out your shell you can execute the `echo $SHELL` in your terminal
```sh
## example running the echo command to find your default shell
❯ echo $SHELL
/usr/local/bin/bash
```

### bash commands syntax
* the basic syntax of a bash command is `command [flags] [subcommands] [flags] [argument]` - here the brackets means that whatever they enclose are optional and as you can see in many cases only the command name is required
* in many cases the command, subcommands and flags stand for something making it easier to remember e.g.:
    - `ls`: list
    - `-l`: long
* flags:
    - most of the time are optional
    - both commands and subcommands can have their own flag
    - they modify how a command works
    - some flags come in two different forms - when they do they are equivalent:
        + short which must be prepended by `-`: `-v`
        + long: which must be prepended by `--` `--verbose`
    - multiple short flags can be combined after one `-` e.g. the following are equivalent:
        + `ls -l -a -h`
        + `ls -lah`
* subcommands:
    - sometimes when one command is too complex whoever writes (makes or provides) the command into 1 command and one and more command + subcommand[s]
* arguments:
    - it is whatever the command or subcommand acts upon for example `git clone` command and subcommand acts upon a URL downloading it

```sh
# YOU CAN EXECUTE THESE COMMANDS INSIDE A TEST DIRECTORY TO SEE HOW FLAGS MODIFY ITS SUBCOMMAND BEHAVIOR
# command subcommand subcommandFlag  argument
git       clone                      https://github.com/molcathy/python.git
git       clone      -q              https://github.com/molcathy/python.git
git       clone      --quiet         https://github.com/molcathy/python.git
```

## useful bash commands
* there are many probably thousands of bash commands, but we are focus on the most basic one of the [most important ones](https://www.google.com/search?q=most+important+bash+commands)
* many commands do not come by default with any system and that is the case for MacOS
* most important bash commands can be installed on macOS with *brew* e.g. `brew install tree`

```sh
## print working directory i.e. current directory
pwd

## list files and directories
ls

## make directory
mkdir myDirectory

## change working directory - NOTE: note multiple directory names or files are separated by /
cd myDirectory
cd myDirectory1/myDirectory2

## list directories and files recursively as a tree
tree
tree -d    # list directories only
tree -L 3  # limit the number of directories and files you want displayed, here 3
tree -dL 3
tree --help # ! NOTE: often commands come with --help or -h flags that display a help menu
```


## brew macOS package manager
## text editors
## markdown
## git - github
## virtual environments
## pip
## functions
## testing