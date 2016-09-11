students = [{'first_name': 'Michael', 'last_name': 'Jordan'},
            {'first_name': 'John', 'last_name': 'Rosales'},
            {'first_name': 'Mark', 'last_name': 'Guillen'},
            {'first_name': 'KB', 'last_name': 'Tonel'}]
def people():
    for student in students:
        print student['first_name'] + ' ' + student['last_name']
people()

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def ppl():
     for key, data in users.items():
         print key
         index = 1
         for students in data:
             name = students['first_name'] + ' ' + students['last_name']
             name_length = len(name) - name.count(' ')
             print str(index) + ' - ' + name + ' - ' + str(name_length)
             index += 1
ppl()
