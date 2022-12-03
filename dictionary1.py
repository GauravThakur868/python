dict1 = {"one":1,"two":2, "three":3}
dict2 = {"four":4, "five":5, "six":6}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

dict4 = {
    "class":{
        "student:":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}
a = dict4.get("class".get("students".get("marks")))
print(a)