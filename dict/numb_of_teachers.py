data = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
  'Kenneth Love': ['Python Basics', 'Python Collections']}

def num_teachers(data):
    number=0
    for teacher in data.keys():
        number += 1
    print(number)
    return(number)


num_teachers(data)


def num_courses(data):
    courses=0
    for teacher in data.keys():
        courses=courses+len(data[teacher])
    print(courses)
    return(courses)


num_courses(data)
