# dictionary - used to store data values in key:value pairs
#ordered
#changable
# does not allow duplicate values
mydictionary = {
    "name":"abcd",
    "age":"20",
    "percent":80.2
}
print(mydictionary)
age = mydictionary.get("age")
print(age)
keys = mydictionary.keys()
print(keys)
value = mydictionary.values()
print(value)
items = mydictionary.items()
print(items)
mydictionary["roll no"] = 11
print(mydictionary)
mydictionary.update({"age":33})
print(mydictionary)
mydictionary.pop("age")
print(mydictionary)
mydictionary.popitem()
print(mydictionary)
