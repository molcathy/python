# pip & pacakges
* packages are modules that have been published and are stored in online repositories
* packages/modules extend python functionality
* they are focused on accomplishing specific tasks
* once installed and imported they can be used in a similar manner as any other modules
* pip is a package manager for Python packages the same way brew is a macOS package manger
* pip lets manage python packages e.g.:
    - search for packages
    - install packages
* example of repository where you can search for packages https://pypi.org/project/pip/

```sh
#! NOTE INSTEAD OF pip you might have to run pip3
## help
pip help         # general help
pip help install # help for a specific command here for install

## list
pip list
pip list --outdated  # only outdated packages

## search
pip search myPackages

## install
pip install myPackages

## upgrade
pip install --upgrade myPackages

## uninstall
pip uninstall myPackages
```
