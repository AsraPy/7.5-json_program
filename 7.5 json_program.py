import json
file_path = "students.json"

def add_student():
    name = input("نام دانش اموز: ")
    age = input("سن: ")
    grade = input("نمره: ")

    student = {
        "name" : name,
        "age" : age,
        "grade" : grade
        }

    try:
        with open(file_path,"r",encoding="utf-8")as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
        
        students.append(student)

        with open(file_path,"w",encoding="utf-8")as file:
            json.dump(students,file,ensure_ascii=False,indent=4)
        print("دانش اموز ذخيره شد.")
def show_students():
    try:
        with open(file_path,"r",encoding="utf-8")as file:
            students = json.load(file)
            if not students:
                print("هيچ اطلاعاتي وجود ندارد")
                return
            print ("\nليست دانش اموزان")
            for s in students:
                print(f"نام:{s['name']},سن:{s['age']},نمره:{s['grade']}")
    except FileNotFoundError:
         print("فايل هنوز ساخته نشده")
def menu():
    while True:
        print("\n1.افزودن دانش اموز")
        print("2.نمايش دانش اموزان")
        print("3.خروج")

        choice = input("انتخاب:")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            print("خروج از برنامه")
            break
        else:
            print("گزينه نامعتبر")
menu()
