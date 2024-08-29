d0 = {66, 5451, "esg"}
type(d0)

# dict
d = {}
type(d)
d1 = {"key": "sudh"}
d1
type(d1)

d2 = {"key": "sudhanshu", "email": "ss@gmaol.com", "number": 33456}
d2

d3 = {
    233: "ef",
    "eg": "Evdf",
    True: "dsg",
}  # key can be int/str/bool but not special case char
d3

d3[233]
d3["eg"]
d3[1]  # 1 == True


d4 = {"name": "sudha", "email_id": "ss@gmailcom", "name": "vikash"}
d4[
    "name"
]  # if duplicate key will be there it will console the last elemwnt --overwrite
# so that's why key should be unique to avoid overwrite


d5 = {
    "company": "pwskills",
    "course": ["web Dev", "data Science", "Java with dsa and system design"],
}
d5
d5["course"]  # dict can store the list also
d5["course"][2]  # dict->list


# nesting of dict/list in dict is allowed
d6 = {
    "number": [2, 32, 5, 2, 5],
    "assignment": (1, 2, 3, 4, 5, 6),
    "launch_date": {28, 12, 14},
    "class_timing": {"web dev": 8, "DataScience": 8, "java with system design": 7},
}
d6


d6["class_timing"]
d6["class_timing"]["DataScience"]

# adding new key to dict
d6["mentor"] = ["Sudanhsu", "krish", "anurag", "hyder"]
d6
d6["mentor"]

# delete a key
del d6["number"]
d6

d6.keys()
list(d6.keys())  # typecast to list
d6.values()
tuple(d6.values())  # typecast to tuples
list(d6.values())

d6.items()  # keys nd values bth

list(d6.items())

d6.pop("mentor")  # return bfr del --#need to give a key
d6


marks = input("enter ur marks")  # default typecast to str
type(marks)

marks = int(input("enter ur marks"))  # default typecast to str
type(marks)



number = 42
print(f"The answer to life, the universe, and everything is {number}.")