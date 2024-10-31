import json


students = [{"Last name" : "Svetiukha", "Grades" : [8, 9, 10, 7, 8]},
            {"Last name" : "Kropyvnytskyi", "Grades" : [4, 10, 11, 12, 5]},
            {"Last name" : "Mykytenko", "Grades" : [8, 7, 9, 9, 10]},
            {"Last name" : "Belik", "Grades" : [1, 5, 8, 3, 12]},
            {"Last name" : "Ponomariov", "Grades" : [8, 7, 5, 10, 12]},
            {"Last name" : "Getman", "Grades" : [7, 4, 12, 10, 6]},
            {"Last name" : "Dvornik", "Grades" : [3, 9, 8, 7, 10]},
            {"Last name" : "Elnikova", "Grades" : [9, 12, 6, 8, 9]},
            {"Last name" : "Kyrychenko", "Grades" : [10, 12, 11, 9, 9]},
            {"Last name" : "Kyslyi", "Grades" : [2, 6, 8, 1, 12]}]

jsonData = json.dumps(students)
with open("data.json", "wt") as file:
    file.write(jsonData)
file.close

while True:    
    print("Select an option:\n 1 - Add data\n 2 - View data\n 3 - Find students with max or min summa of the grades\n 4 - Exit") 
    x = input("Choose an option:\n") 
    x = int(x)

    if x == 1:
            def add_employee(data):
                print("Add: ")
                Name = input("Last name: ")
                Grades = []
                for i in range(5):
                    g = int(input(f"Enter grade [{i + 1}]: "))
                    Grades.append(g)
                data.append({"Last name": Name, "Grades": Grades})
                return data
            
            with open("data.json", "rt") as file:
                students = json.loads(file.read())

            students = add_employee(students)
            jsonData = json.dumps(students)

            with open("data.json", "wt") as file:
                file.write(jsonData)

    if x == 2:
        with open("data.json", "rt") as file:
            students = json.loads(jsonData)
            print(*students, sep='\n')

    if x == 3:
        with open("data.json", "rt") as file:
            students = json.loads(jsonData)
            b = max(students, key=lambda student: sum(student['Grades']))
            print(f"Учень з найбільшою сумою оцінок: {b['Last name']} ({sum(b['Grades'])})")
            data = [{'Last name' : b['Last name']}, {'Grades' : sum(b['Grades'])}]
            jsond = json.dumps(data)
            with open("data_2.json", "wt") as file:
                file.write(jsond)
            file.close

            w = min(students, key=lambda student: sum(student['Grades']))
            print(f"Учень з найменшою сумою оцінок: {w['Last name']} ({sum(w['Grades'])})")
            data = [{'Last name' : w['Last name']}, {'Grades' : sum(w['Grades'])}]
            jsond = json.dumps(data)
            with open("data_2.json", "at") as file:
                file.write(jsond)
            file.close

    if x == 4:
        quit(0)