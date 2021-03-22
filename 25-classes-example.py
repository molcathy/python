import pickle

fName = input("What is your first name? ")
lName = input("What is your last name? ")
salary = input("What is your salary? ")
role = input("What is role worker (w) or manager (m)? ")

class Worker:
    'Common base class for all workers'
    company = "test.com"

    def __init__(self, fName, lName, salary):
        self.fName = fName
        self.lName = lName
        self.salary = salary
        self.email = self.fName + '.' + self.lName + '@' + Worker.company

    def clockIn(self):
        print('Clocked In')

    def work(self):
        print('Worked')

    def clockOut(self):
        print('Clocked Out')


class Manager(Worker):
    def __init__(self, fName, lName, salary):
        super().__init__(fName, lName, salary)

    def hireWorker(self):
        print('Hired.')

    def listWorkers(self):
        print('Listed')

    def fireWorkers(self):
        print('Fired.')

if role == 'w':
    wk = Worker(fName, lName, salary)
    print(wk.fName, wk.lName, wk.salary, wk.email)
    action = input("What do you wan to do: clock in (i), work (w) or clock out (o)? ")
    if action == 'i':
        wk.clockIn()
    elif action == 'w':
        wk.work()
    elif action == 'o':
        wk.clockOut()
    else:
        print("Invalid Action!")
elif role == 'm':
    mn = Manager(fName, lName, salary)
    print(mn.fName, mn.lName, mn.salary, mn.email)
    action = input("What do you wan to do: clock in (i), work (w) or clock out (o), manager workers (m)? ")
    if action == 'i':
        mn.clockIn()
    elif action == 'w':
        mn.work()
    elif action == 'o':
        mn.clockOut()
    elif action == 'm':
        action = input("What do you wan to do: hire (h), list (l) or fire (f)? ")
        if action == 'h':
            mn.hireWorker()
        elif action == 'l':
            mn.listWorkers()
        elif action == 'f':
            mn.fireWorkers()
        else:
            print("Invalid Action!")
    else:
        print("Invalid Action!")
else:
    print("Wrong Answer!")