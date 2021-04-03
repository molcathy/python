import subprocess

def listwd():
    return subprocess.check_output(['ls']).split()

def main():
    print(listwd())


if __name__ == "__main__":
    main()
