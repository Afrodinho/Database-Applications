-- 1. Write a query to create a view named “EmployeesPerCountry” that shows the country_name and the number of employees from that country in a column called “Number of Employees”. Display your results in descending order of number of employees.
--WORKING

CREATE VIEW EmployeesPerCountry AS SELECT country_name, COUNT(employee_id) AS "Number of Employees" FROM employees e, departments d,locations l,countries c,regions r WHERE r.region_id = c.region_id AND c.country_id = l.country_id AND d.location_id = l.location_id AND e.department_id = d.department_id GROUP BY country_name ORDER BY COUNT(employee_id) DESC;

--Query the EmployeesPerCountry to show the number of employees from the United Kingdom .

SELECT * FROM EmployeesPerCountry WHERE country_name = "United Kingdom";

-- 2. Write a query to create a view named “managers” to display all the managers. Include the manager’s name (first, last), phone number, email, job title, and department name.
--WORKING
CREATE VIEW managers AS
SELECT e.first_name, e.last_name, e.phone_number, e.email, j.job_title, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN jobs j ON e.job_id = j.job_id
WHERE e.employee_id IN (SELECT manager_id from employees);

--Query the managers view to show the number of managers in each department.

SELECT department_name, COUNT(first_name) AS "Number of Managers" FROM managers GROUP BY department_name ORDER BY COUNT(first_name) DESC;

-- 3. Write a query to create a view named DependentsByJobTitle to get a count of how many dependents there are for each job title. Show job titles even if they do not have dependents. Place the number of dependents in a column called "Number of Dependents". HINT: Remember directional Joins (LEFT & RIGHT), you will have to use one of those.
-- Query the DependentsByJobTitle view to show the job titles(s) with the largest number of dependents. This should show the job title and the number of dependents. HINT: Think about using a nested query for this because there are multiple job titles with the max number of dependents.
--WORKING
CREATE VIEW DependentsByJobTitle AS SELECT job_title, COUNT(dependents.first_name) AS "NumberOfDependents" FROM jobs,employees,dependents WHERE employees.job_id = jobs.job_id AND employees.employee_id = dependents.employee_id GROUP BY job_title ORDER BY COUNT(dependents.first_name) DESC;

SELECT * FROM DependentsByJobTitle WHERE NumberOfDependents = (SELECT MAX(NumberOfDependents) FROM DependentsByJobTitle) GROUP BY job_title ORDER BY NumberOfDependents DESC;

-- 4. Write a query to create a view named “HiresByYear” that calculates the number of employees hired each year. Remember the SQL $year function.

CREATE VIEW DepartmentHiresByYear AS  
SELECT YEAR(e.hire_date) AS "year", d.department_name, COUNT(e.employee_id) AS "Employees Hired"
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
GROUP BY YEAR(e.hire_date), d.department_name
ORDER BY d.department_name;

-- Query the DepartmentHiresByYear view to show department hires in 1998.
SELECT *
FROM DepartmentHiresByYear
WHERE year = 1998;

--5. Write a query to create a view named “AvgSalaryByJobTitle” to calculate the average salary for each job title. Display the job title, average salary in a column named "Average salary", and number of employees with that title in a column called "Number of Employees". Display results in descending order by average salary. HINT: You can use both the AVG() and COUNT() functions in the Select clause of your query.

CREATE VIEW AvgSalaryByJobTitle AS SELECT j.job_title, AVG(e.salary) AS "Average Salary", COUNT(j.job_title) AS "Number of Employees" FROM jobs j JOIN employees e ON j.job_id = e.job_id GROUP BY j.job_title ORDER BY AVG(e.salary) DESC;

-- Query the AvgSalaryByJobTitle view to show the average salary for the Programmers.
SELECT * FROM AvgSalaryByJobTitle WHERE job_title = "Programmer";


-- 6.Write a query to create a view named “AvgSalaryByDepartment” to calculate average salaries for each department. Display the department name, average salary in a column named "Average salary", and number of employees with that title in a column called "Number of Employees"

CREATE VIEW AvgSalaryByDepartment AS
SELECT d.department_name, AVG(e.salary) AS "Average Salary", COUNT(d.department_name) AS "Number of Employees"
FROM departments d, employees e
WHERE e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY AVG(e.salary) DESC;

--Query the AvgSalaryByDepartment view to show the department name and average salary for the department with the lowest average salary.
SELECT * FROM AvgSalaryByDepartment ORDER BY `Average Salary` LIMIT 1;

-- 7. Write a query to create a view named “EmployeeDependents” that calculates the number of dependents each employees has. This query should show employees even if they have 0 dependents. Display the employee name (first, last), email, phone number, and number of dependents. Hint: left or right join.
--Query the EmployeeDependents view to show employees with no children". Show employee name (first, last), email, phone number, and number of dependents.
--WORKING
CREATE VIEW EmployeeDependents AS SELECT e.first_name, e.last_name, e.email, e.phone_number, COUNT(d.first_name) AS "NumberOfDependents" FROM employees e LEFT JOIN dependents d ON e.employee_id = d.employee_id GROUP BY e.first_name,e.last_name,e.email,e.phone_number ORDER BY COUNT(d.first_name);

SELECT * FROM EmployeeDependents WHERE NumberOfDependents = 0;

-- 8. Write a query to create a view named “CountryLocation” that calculates the number of locations in each country. This query should show countries even if they have 0 locations. Display the country name and number of locations.
--Query the LocationByRegion view to show regions with no locations". Show region name and number of locations.

CREATE VIEW CountryLocation AS SELECT r.region_name, COUNT(l.location_id) AS "NumberofLocations" FROM regions r JOIN countries c ON r.region_id = c.region_id LEFT JOIN locations l ON c.country_id = l.country_id GROUP BY r.region_name ORDER BY COUNT(l.location_id) DESC;

SELECT * FROM CountryLocation WHERE NumberofLocations = 0;