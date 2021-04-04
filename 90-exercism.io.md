# [exercism](https://exercism.io/my/tracks)

## 1st time setup
```sh
#1. Install Exercism CLI https://exercism.io/cli-walkthrough
brew install exercism

#2. Configure Exercism Token https://exercism.io/my/settings
exercism configure --token=<TOKEN>

#3. Configure Custom Workspace
    # replace <USERNAME> with your username
    # you can find your username with the command 'whoami'
    # set 'workspace' to /Users/<USERNAME>/repos/github.com/molcathy/exerscism
code ~/.config/exercism/user.json

#4. Configure Repository
cd ~/repos/github.com/molcathy
git clone git@github.com:molcathy/exerscism.git
cd exerscism
git branch <myBranch>
git checkout <myBranch>

#5. Configure Virtual Environment And Install pytest
python3 -m venv venv
source venv/bin/activate

#6. Install pytest
pip install pytest

#7. Document Installed Packages
pip freeze > requirements.txt
```

## WORKING EXERCISES

The process was exemplified with the `hello-world` exercise.
Replace `hello-world` with your exercise name as need it.

```sh
#1. Change Directory To exercism Workspace
cd ~/repos/github.com/molcathy/exerscism/

#2. Activate venv *IF* Not Active
source venv/bin/activate

#3. Choose & Download Exercise https://exercism.io/my/tracks/python
exercism download --track=python --exercise=hello-world

#4. Open The Exercise In VSCode
cd python/hello-world
code .

#5. SOLVE - Only Once All Test Pass The Exercise Is Complete!
pytest hello_world_test.py          # test

#6. Submit
exercism submit hello_world.py

#7. Update Your Remote Branch
cd ~/repos/github.com/molcathy/exerscism/
git add --all
git commit -m 'completed exercise hello-world'
git push
```