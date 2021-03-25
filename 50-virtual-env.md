# python virtual environments
* virtual environments are a way to mange your application dependencies (e.g. modules, packages):
    - it isolates your  application and its dependencies from the rest of the operating system
    - it creates a list a dependencies
* using environments allows other developers to reproduce your development environment exactly
* it is important for all the developers part of a project to run the program in the same environment - not doing so you end up with all kinds of bugs caused by your environment

```sh
## CREATE A VIRTUALENVIRONEMNT
## DO NOT:
##   - place source code file inside venv directory
##   - source control venv instead only sourcecontrol the requirements.txt

git clone _PROJECT
cd _PROJECT

## CREATE VIRTUAL ENVIRONMENT
python3 -m venv venv

## ACTIVATE VIRTUAL ENVIRONMENT
source venv/bin/activate

## INSTALL MODULES
pip install _MODULE


## FREEZE / INSTALL
pip freeze > requirements.txt
pip install -r requirements.txt  ## in a new project after setting up a new virt env


## DEACTIVATE
deactivate
```