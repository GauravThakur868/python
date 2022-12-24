class person():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
person1 = person("abc",45)
print(person1._person__name)
