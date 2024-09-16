from threading import Thread, Semaphore, Condition, RLock
from time import sleep

class UnisexBathroom(object):
    def __init__(self):
        self.in_use_by = None
        self.cond = Condition(RLock())
        self.max_emp_sem = Semaphore(3)
        self.num_emp_in_bathroom = 0

    def use_bathroom(self, name):
        print("\n{} is using bathroom, {} employees in bathroom".format(name, self.num_emp_in_bathroom))
        sleep(2)
        print("\n{} is done using bathroom".format(name))

    def male_use_bathroom(self, name):
        with self.cond:
            while self.in_use_by == "female":
                self.cond.wait()
            self.max_emp_sem.acquire()
            self.num_emp_in_bathroom += 1
            self.in_use_by = "male"
        self.use_bathroom(name)
        self.max_emp_sem.release()
        with self.cond:
            self.num_emp_in_bathroom -= 1
            if self.num_emp_in_bathroom == 0:
                self.in_use_by = None
            self.cond.notify_all()

    def female_use_bathroom(self, name):
        with self.cond:
            while self.in_use_by == "male":
                self.cond.wait()
            self.max_emp_sem.acquire()
            self.num_emp_in_bathroom += 1
            self.in_use_by = "female"
        self.use_bathroom(name)
        self.max_emp_sem.release()
        with self.cond:
            self.num_emp_in_bathroom -= 1
            if self.num_emp_in_bathroom == 0:
                self.in_use_by = None
            self.cond.notify_all()

if __name__=="__main__":

    unisex_bathroom = UnisexBathroom()
    female1 = Thread(target=unisex_bathroom.female_use_bathroom, args=("Female 1",))
    male1 = Thread(target=unisex_bathroom.male_use_bathroom, args=("Male 1",))
    male2 = Thread(target=unisex_bathroom.male_use_bathroom, args=("Male 2",))
    female2 = Thread(target=unisex_bathroom.female_use_bathroom, args=("Female 2",))
    female3 = Thread(target=unisex_bathroom.female_use_bathroom, args=("Female 3",))
    male3 = Thread(target=unisex_bathroom.male_use_bathroom, args=("Male 3",))
    male4 = Thread(target=unisex_bathroom.male_use_bathroom, args=("Male 4",))
    male5 = Thread(target=unisex_bathroom.male_use_bathroom, args=("Male 5",))
    male6 = Thread(target=unisex_bathroom.male_use_bathroom, args=("Male 6",))
    female4 = Thread(target=unisex_bathroom.female_use_bathroom, args=("Female 4",))
    female5 = Thread(target=unisex_bathroom.female_use_bathroom, args=("Female 5",))
    male7 = Thread(target=unisex_bathroom.male_use_bathroom, args=("Male 7",))
    female6 = Thread(target=unisex_bathroom.female_use_bathroom, args=("Female 6",))

    female1.start()
    male1.start()
    male2.start()
    female2.start()
    female3.start()
    male3.start()
    male4.start()
    male5.start()
    male6.start()
    female4.start()
    female5.start()
    male7.start()
    female6.start()

    female1.join()
    female2.join()
    female3.join()
    female4.join()
    female5.join()
    female6.join()
    male1.join()
    male2.join()
    male3.join()
    male4.join()
    male5.join()
    male6.join()
    male7.join()



