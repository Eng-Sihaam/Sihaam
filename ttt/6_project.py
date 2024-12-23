import csv
import os
import pandas as pd

def login():
    print("Welcome to Attendance System")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    if username == "sihaam" and password == "1423":
        print("\nSelect a Subject for Attendance:")
        print("1. Python")
        print("2. Computer Application")
        print("3. Introduction to Computer")
        
        absent_students = []
        choice = input("Enter your choice (1/2/3): ")
        subjects = {1: "Python", 2: "Computer Application", 3: "Introduction to Computer"}
        sub = subjects.get(int(choice))

        students = [
            {"ID": "b5SC1670", "Name": "Asma Maxamed"},
            {"ID": "b5SC1671", "Name": "Zack Daahir"},
            {"ID": "b5SC1672", "Name": "Fatima Noor"},
            {"ID": "b5SC1673", "Name": "Hassan Mohamed"},
            {"ID": "b5SC1674", "Name": "Maryam Ali"},
            {"ID": "b5SC1675", "Name": "Abdullahi Isse"},
            {"ID": "b5SC1676", "Name": "Khadija Abdi"},
            {"ID": "b5SC1677", "Name": "Mohamud Yusuf"},
            {"ID": "b5SC1678", "Name": "Abdirahman Omar"},
            {"ID": "b5SC1679", "Name": "Sahra Hassan"}
        ]

        if choice == '1':
            print(f"\nTaking Attendance for {sub}\n")
            for student in students:
                print(f"ID: {student['ID']} - Name: {student['Name']}")
                status = input("Is the student absent? (y/n): ").lower()
                if status == 'y':
                    absent_students.append(1)
                elif status == 'n':
                    absent_students.append(0)
                else:
                	return "Furaha Ma Jiro"
            
            df = pd.read_excel("Students_List1.xlsx")
            df['Python'] = df['Python'] + absent_students
            
            with pd.ExcelWriter("Students_List1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='overlay') as au:
                df.to_excel(au, index=False)
        
        elif choice == '2':
            print(f"\nTaking Attendance for {sub}\n")
            for student in students:
                print(f"ID: {student['ID']} - Name: {student['Name']}")
                status = input("Is the student absent? (y/n): ").lower()
                if status == 'y':
                    absent_students.append(1)
                elif status =='n':
                	absent_students.append(0)
                else:
                    return "Furaha Ma Jiro"
                    
            
            df = pd.read_excel("Students_List1.xlsx")
            df['Computer Application'] = df['Computer Application'] + absent_students
            
            with pd.ExcelWriter("Students_List1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='overlay') as au:
                df.to_excel(au, index=False)
        
        elif choice == '3':
            print(f"\nTaking Attendance for {sub}\n")
            for student in students:
                print(f"ID: {student['ID']} - Name: {student['Name']}")
                status = input("Is the student absent? (y/n): ").lower()
                if status == 'y':
                    absent_students.append(1)
                elif status =='n':
                	absent_students.append(0)
                else:
                    return "Furaha Ma Jiro"          
            df = pd.read_excel("Students_List1.xlsx")
            df['Intro Cs'] = df['Intro Cs'] + absent_students
            
            with pd.ExcelWriter("Students_List1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='overlay') as au:
                df.to_excel(au, index=False)

y = login()
print(y)
