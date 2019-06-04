data = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
  'Kenneth Love': ['Python Basics', 'Python Collections']}

def num_teachers(data):
    number=0
    for teacher in data.keys():
        number += 1
    print(number)
    return(number)

num_teachers(data)
print("*"*40)

def num_courses(data):
    courses=0
    for teacher in data.keys():
        courses=courses+len(data[teacher])
    print(courses)
    return(courses)

num_courses(data)
print("*"*40)

def courses(data):
    value=[]
    for teacher in data.keys():
        value=value+data[teacher]
    return(value)

courses(data)
print("*"*40)

def most_courses(data):
    best=dict()
    max=0
    for x, y in data.items():
        best[x]=len(data[x])
        if best[x]>max:
            max=best[x]
            best_name=x
    print(best_name,max)
    return best_name

most_courses(data)
print("*"*40)


