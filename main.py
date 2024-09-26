# first_line = input("Type in the first line of your favourite song\n")
#
# print(len(first_line))
# start_idx = int(input("start number"))
# end_idx = int(input("end number"))
# print(first_line[start_idx:end_idx])
#
# print(first_line.strip())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return "name:{}, age:{}".format(self.name, self.age)

class Student(Person):
    def id(self, id):
        self.id = id
        return id

hzy = Student("hzy", 22)
print(hzy.info())
print(hzy.id(299))