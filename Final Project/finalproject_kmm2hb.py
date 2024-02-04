#Kaden Marshall
#query HR_database - Project 2
#Name of Application HRCheck
import mysql.connector

#1 Working
def EmployeesPerCountry(mycursor):
    country = str(input("\nType the name of a country OR type ALL to see all countries: \n"))


    if(country.casefold() == "all"):
        #create query
        sql_query = "SELECT * FROM EmployeesPerCountry"
        #execute the query
        mycursor.execute(sql_query)
        #get the query result
        query_result = mycursor.fetchall()
        #loop through results
        for record in query_result:
            print(f"Country: {record[0]} \nNumber of Employees: {record[1]} \n")
        return
    
    else:
            sql_query = "SELECT * FROM EmployeesPerCountry WHERE country_name = %s"
            name = (country,)
            mycursor.execute(sql_query, name)
            query_result = mycursor.fetchall()
            for record in query_result:
                print(f"Country: {record[0]} \nNumber of Employees: {record[1]} \n")
            return



    
    # elif(country.title() == "United Kingdom"):
    #     #create query
    #     sql_query = "SELECT * FROM EmployeesPerCountry WHERE country_name = 'United Kingdom';"
    #     #execute the query
    #     mycursor.execute(sql_query)
    #     #get the query result
    #     query_result = mycursor.fetchall()
    #     #loop through results
    #     for record in query_result:
    #         print(f"Country: {record[0]} \nNumber of Employees: {record[1]} \n")
    #     return
    

    # elif(country.title() == "Canada"):
    #     #create query
    #     sql_query = "SELECT * FROM EmployeesPerCountry WHERE country_name = 'Canada';"
    #     #execute the query
    #     mycursor.execute(sql_query)
    #     #get the query result
    #     query_result = mycursor.fetchall()
    #     #loop through results
    #     for record in query_result:
    #         print(f"Country: {record[0]} \nNumber of Employees: {record[1]} \n")
    #     return
    
    # elif(country.title() == "Germany"):
    #     #create query
    #     sql_query = "SELECT * FROM EmployeesPerCountry WHERE country_name = 'Germany';"
    #     #execute the query
    #     mycursor.execute(sql_query)
    #     #get the query result
    #     query_result = mycursor.fetchall()
    #     #loop through results
    #     for record in query_result:
    #         print(f"Country: {record[0]} \nNumber of Employees: {record[1]} \n")
    #     return
    
    # elif(country.title() == "United States"):
    #     #create query
    #     sql_query = "SELECT * FROM EmployeesPerCountry WHERE country_name = 'United States';"
    #     #execute the query
    #     mycursor.execute(sql_query)
    #     #get the query result
    #     query_result = mycursor.fetchall()
    #     #loop through results
    #     for record in query_result:
    #         print(f"Country: {record[0]} \nNumber of Employees: {record[1]} \n")
    #     return
    
       #SELECT * FROM EmployeesPerCountry Where country_name" + 'country name' ";"
       # Can I do this? https://www.drupal.org/forum/support/module-development-and-code-questions/2007-03-16/d-and-s-in-sql-queries
    

   
#2 Working
def managers(mycursor):
    department = str(input("\nType the name of a Department OR type ALL to see all Departments: \n"))


    if(department.casefold() == "all"):
        #create query
        sql_query = "SELECT department_name, COUNT(first_name) AS 'Number of Managers' FROM managers GROUP BY department_name ORDER BY COUNT(first_name) DESC;"
        #execute the query
        mycursor.execute(sql_query)
        #get the query result
        query_result = mycursor.fetchall()
        #loop through results
        for record in query_result:
            print(f"Department: {record[0]} \nNumber of Employees: {record[1]} \n")
        return
    
    else:
            sql_query = "SELECT department_name, COUNT(first_name) AS 'Number of Managers' FROM managers WHERE department_name = %s"
            name = (department,)
            mycursor.execute(sql_query, name)
            query_result = mycursor.fetchall()
            for record in query_result:
                print(f"Department Name: {record[0]} \nNumber of Managers: {record[1]} \n")
            return

#3 Working
def DependentsByTitle(mycursor):
    title = str(input("\nType the Job Title OR type ALL to see all Jobs: \n"))


    if(title.casefold() == "all"):
        #create query
        sql_query = "SELECT * FROM DependentsByJobTitle WHERE NumberOfDependents = (SELECT MAX(NumberOfDependents) FROM DependentsByJobTitle) GROUP BY job_title ORDER BY NumberOfDependents DESC;"
        #execute the query
        mycursor.execute(sql_query)
        #get the query result
        query_result = mycursor.fetchall()
        #loop through results
        for record in query_result:
            print(f"Job Title: {record[0]} \nNumber of Dependents: {record[1]} \n")
        return
    
    else:
            sql_query = "SELECT * FROM DependentsByJobTitle WHERE job_title = %s"
            job = (title,)
            mycursor.execute(sql_query, job)
            query_result = mycursor.fetchall()
            for record in query_result:
                print(f"Job Title: {record[0]} \nNumber of Dependents: {record[1]} \n")
            return
#4 Semi Working
def HiresByYear(mycursor):
    hires = input("\nType all to see all Hires OR type a year: \n")


    if(hires.casefold() == "all"):
        #create query
        sql_query = "SELECT * FROM DepartmentHiresByYear ORDER BY year;"
        mycursor.execute(sql_query)
        #get the query result
        query_result = mycursor.fetchall()
        #loop through results
        for record in query_result:
            print(f"Department: {record[0]} \nYear: {record[1]} \n")
        return
    
    else:
            sql_query = "SELECT * FROM DependentsByJobTitle WHERE year = %u;"
            year = (hires,)
            mycursor.execute(sql_query, year)
            query_result = mycursor.fetchall()
            for record in query_result:
                print(f"Department: {record[0]} \nYear: {record[1]} \n")
            return
#5 Working
def SalaryByJob(mycursor): 
    title = str(input("\nType the Job Title OR type ALL to see all Jobs: \n"))


    if(title.casefold() == "all"):
        #create query
        sql_query = "SELECT * FROM AvgSalaryByJobTitle GROUP BY job_title;"
        #execute the query
        mycursor.execute(sql_query)
        #get the query result
        query_result = mycursor.fetchall()
        #loop through results
        for record in query_result:
            print(f"Job Title: {record[0]} \nNumber of Dependents: {record[1]} \n")
        return
    
    else:
            sql_query = "SELECT * FROM AvgSalaryByJobTitle WHERE job_title = %s"
            job = (title,)
            mycursor.execute(sql_query, job)
            query_result = mycursor.fetchall()
            for record in query_result:
                print(f"Job Title: {record[0]} \nAverage Salary: {record[1]} \n")
            return  
#6 Working
def SalaryByDepartment(mycursor): 
    department = str(input("\nType the Department OR type ALL to see all Departments: \n"))


    if(department.casefold() == "all"):
        #create query
        sql_query = "SELECT * FROM AvgSalaryByDepartment;"
        #execute the query
        mycursor.execute(sql_query)
        #get the query result
        query_result = mycursor.fetchall()
        #loop through results
        for record in query_result:
            print(f"Job Title: {record[0]} \Average Salary: {record[1]} \n")
        return
    
    else:
            sql_query = "SELECT * FROM AvgSalaryByDepartment WHERE department_name = %s"
            sal = (department,)
            mycursor.execute(sql_query, sal)
            query_result = mycursor.fetchall()
            for record in query_result:
                print(f"Department: {record[0]} \nAverage Salary: {record[1]} \n")
            return  
#7 semi work
def EmployeeDependents(mycursor):
    edp = str(input("\nType Employee First Name or Type All \n"))


    if(edp.casefold() == "all"):
        #create query
        sql_query = "SELECT first_name, last_name, NumberOfDependents FROM EmployeeDependents;"
        #execute the query
        mycursor.execute(sql_query)
        #get the query result
        query_result = mycursor.fetchall()
        #loop through results
        for record in query_result:
            print(f"Employee Name: {record[0]} {record[1]} - Number of Dependents: {record[2]}\n")
        return
    
    else:
            sql_query = "Select first_name, last_name, NumberOfDependents FROM EmployeeDependents WHERE first_name = %s"
            first = (edp,)
            mycursor.execute(sql_query, first)
            query_result = mycursor.fetchall()
            for record in query_result:
                print(f"Employee Name: {record[0]} {record[1]} - Number of Dependents: {record[2]}\n")
            return
#8 Semi working
def CountryLocation(mycursor):
    location = str(input("\nType the name of a country OR type ALL to see all countries: \n"))


    if(location.casefold() == "all"):
        #create query
        sql_query = "SELECT * FROM CountryLocation"
        #execute the query
        mycursor.execute(sql_query)
        #get the query result
        query_result = mycursor.fetchall()
        #loop through results
        for record in query_result:
            print(f"Country: {record[0]} \nNumber of Locarions: {record[1]} \n")
        return
    
    else:
            sql_query = "SELECT * FROM CountryLocation WHERE region_name = %s"
            name = (location,)
            mycursor.execute(sql_query, name)
            query_result = mycursor.fetchall()
            for record in query_result:
                print(f"Country: {record[0]} \nNumber of Locations: {record[1]} \n")
            return

#9 ?
#Look for Values like when printing the results to get inputs
def addDependent(mycursor):
    first_name = input("Enter Dependent First Name: \n")
    last_name = input("Enter Dependent Last Name: \n")
    relationship = input("Enter Relationship: \n")
    eID = input("Enter EmployeeID Number: \n")

    try:
        sql_query = f"INSERT INTO dependents(first_name, last_name, relationship, employee_id) VALUES ('{first_name}', '{last_name}', '{relationship}', '{eID}');"
        #execute the query
        mycursor.execute(sql_query)
        mycursor.commmit()
    except Exception as err:
        print(f"Error Occured: {err} Returning to main menu")
        return

#10. Reading but not inserting?
# Look for Values like when printing the results to get inputs
def addJob(mycursor):
    job_title = str(input("Enter Job Title: \n"))
    minimum = int(input("Enter Minimum Salary: \n"))
    maximimum = int(input("Enter Maximum Salary: \n"))

    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to Project 2 database! Loading HR Resources...")
        sql_query = "INSERT INTO jobs(job_title, min_salary, max_salary) VALUES (%s, %s, %s);"
        #execute the query
        mycursor.execute(sql_query,(job_title,minimum,maximimum))
        #I think this commits changes like you would in github
        mydb.commmit(sql_query)
        print(mycursor.rowcount, "record inserted")
    except Exception as err:
        print(f"Error Occured: {err} Returning to main menu")
        return
    
def deleteEmployee(mycursor):
    first_name = str(input("Enter first name: \n"))
    last_name = str(input("Enter last name: \n"))

    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to Project 2 database! Loading HR Resources...")
        sql_query = "DELETE from employees WHERE first_name = %s AND last_name = %s;"
        #execute the query
        mycursor.execute(sql_query,(first_name, last_name))
        #I think this commits changes like you would in github
        mydb.commmit(sql_query)
        print(mycursor.rowcount, "record inserted")
    except Exception as err:
        print(f"Error Occured: {err} Returning to main menu")
        return

def deleteDependent(mycursor):
    first_name = str(input("Enter first name: \n"))
    last_name = str(input("Enter last name: \n"))

    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to Project 2 database! Loading HR Resources...")
        sql_query = "DELETE from dependents WHERE first_name = %s AND last_name = %s;"
        #execute the query
        mycursor.execute(sql_query,(first_name, last_name))
        #I think this commits changes like you would in github
        mydb.commmit(sql_query)
        print(mycursor.rowcount, "record inserted")
    except Exception as err:
        print(f"Error Occured: {err} Returning to main menu")
        return
    
def updateEmployeeFN(mycursor):
    first_name = str(input("Enter first name: \n"))
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to Project 2 database! Loading HR Resources...")
        sql_query = "UPDATE from employees SET first_name = %s;"
        #execute the query
        mycursor.execute(sql_query,(first_name))
        #I think this commits changes like you would in github
        mydb.commmit(sql_query)
        print(mycursor.rowcount, "record inserted")
    except Exception as err:
        print(f"Error Occured: {err} Returning to main menu")
        return
    
def updateEmployeeLN(mycursor):
    first_name = str(input("Enter first name: \n"))
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to Project 2 database! Loading HR Resources...")
        sql_query = "UPDATE from employees SET last_name = %s;"
        #execute the query
        mycursor.execute(sql_query,(first_name))
        #I think this commits changes like you would in github
        mydb.commmit(sql_query)
        print(mycursor.rowcount, "record inserted")
    except Exception as err:
        print(f"Error Occured: {err} Returning to main menu")
        return

def updateMinSal(mycursor):
    min_salary = int(input("Enter first name: \n"))
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to Project 2 database! Loading HR Resources...")
        sql_query = "UPDATE from employees SET min_salary = %d;"
        #execute the query
        mycursor.execute(sql_query,(min_salary))
        #I think this commits changes like you would in github
        mydb.commmit(sql_query)
        print(mycursor.rowcount, "record inserted")
    except Exception as err:
        print(f"Error Occured: {err} Returning to main menu")
        return

def updateMaxSal(mycursor):
    max_salary = int(input("Enter first name: \n"))
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to Project 2 database! Loading HR Resources...")
        sql_query = "UPDATE from employees SET min_salary = %d;"
        #execute the query
        mycursor.execute(sql_query,(max_salary))
        #I think this commits changes like you would in github
        mydb.commmit(sql_query)
        print(mycursor.rowcount, "record inserted")
    except Exception as err:
        print(f"Error Occured: {err} Returning to main menu")
        return
    
def print_menu():
    print("\nWelcome to HRCheck!\nPlease Select the Number That Corresponds to Your Request\n")
    print("\n----------------VIEW DATA----------------------")
    print("1. Display Number of Employees Per Country")
    print("2. Display Number of Managers By Department")
    print("3. Display Job Title(s) With the Most Dependents")
    print("4. Display Number of Hires in 1998")
    print("5. Display Average Salary of Programmer")
    print("6. Display Average Salary of lowest paid Department")
    print("7. Display Employees With No Dependents")
    print("8. Display Countries Where We Have NO Locations")
    print("\n----------------ADD DATA----------------------")
    print("9. Add a dependent")
    print("10. Add a Job")
    print("\n----------------DELETE DATA----------------------")
    print("11. Delete an Employee")
    print("12. Delete a Dependent")
    print("\n----------------UPDATE DATA----------------------")
    print("13. Update employee first name")
    print("14. Update employee last name")
    print("15. Update job minimum salary")
    print("16. Update job maximum salary")
    print("\n----------------EXIT----------------------")
    print("17. Exit Application")
    return


def get_user_choice():
    print_menu()
    choice = int(input("\nEnter Choice: "))
    return choice

def main():
#create a connector object
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to Project 2 database! Loading HR Resources...")
    except Exception as err:
        print(f"Error Occured: {err}\nExiting program...")
        quit()

    #create database cursor
    mycursor = mydb.cursor()


    while(True):
        try:
            user_choice = get_user_choice()
            if(user_choice == 1):
            #call the function to query employees per region
                EmployeesPerCountry(mycursor)
            elif(user_choice == 2):
            #call the function to query the managers
                managers(mycursor)
            elif(user_choice == 3):
            #call the function to query the DependentsByDepartment
                DependentsByTitle(mycursor)
            elif(user_choice == 4):
            #call the function to query the HiresByYear
                HiresByYear(mycursor)
            elif(user_choice == 5):
            #call the function to query the SalaryByDepartment
                SalaryByJob(mycursor)
            elif(user_choice == 6):
            #call the function to query the SalaryByJobTitle
                SalaryByDepartment(mycursor)
            elif(user_choice == 7):
            #call the function to query the EmployeeDependents
                EmployeeDependents(mycursor)
            elif(user_choice == 8):
            #call the function to query CountryLocation
                CountryLocation(mycursor)
            elif(user_choice == 9):
            #call the function to query CountryLocation
                addDependent(mycursor)
            elif(user_choice == 10):
            #call the function to query CountryLocation
                addJob(mycursor)
            elif(user_choice == 11):
            #call the function to query CountryLocation
                deleteEmployee(mycursor)
            elif(user_choice == 12):
            #call the function to query CountryLocation
                deleteDependent(mycursor)
            elif(user_choice == 13):
            #call the function to query CountryLocation
                updateEmployeeFN(mycursor)
            elif(user_choice == 14):
            #call the function to query CountryLocation
                updateEmployeeLN(mycursor)
            elif(user_choice == 15):
            #call the function to query CountryLocation
                updateMinSal(mycursor)
            elif(user_choice == 16):
            #call the function to query CountryLocation
                updateMaxSal(mycursor)
            elif(user_choice == 17):
                print("\nNow Exiting the Application! Thank You for Using HRCheck!\n")
                break
        except ValueError:
                print("\nThat is not an option. Try again.\n")

main()
    

