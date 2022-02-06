from operator import attrgetter

class User(object):
    def __init__(self, name):
        self.age = 0
        self.wealth = 0
        self.name = name

    def __repr__(self):
        return "name: {}, age: {}, wealth {}".format(self.name, self.age, self.wealth)


def custom_sorter(object):
    return object.age * object.wealth


if __name__=="__main__":
    u1 = User("A")
    u1.age = 10
    u1.wealth = 100
    u2 = User("B")
    u2.age = 20
    u2.wealth = 200
    u3 = User("C")
    u3.age = 40
    u3.wealth = 40
    users = [u1, u2, u3]
    ''' Sort by age '''
    print(sorted(users, key=attrgetter('age')))
    ''' Sort by wealth '''
    print(sorted(users, key=attrgetter('wealth'), reverse=True))
    ''' Sort by custom rule 2*age + 3*wealth '''
    print(sorted(users, key=lambda x: custom_sorter(x)))