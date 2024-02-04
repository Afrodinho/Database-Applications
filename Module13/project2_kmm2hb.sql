-- 1. Write a query to create a view named “EmployeesPerRegion” that shows the region_name and the number of employees from that region in a column called “Number of Employees”.
-- Query the EmployeesPerRegion to show the number of employees from the Americas.

CREATE VIEW EmployeesPerRegion AS SELECT region_name, COUNT(employee_id) AS "Number of Employees" FROM employees e, departments d,locations l,countries c,regions r WHERE r.region_id = c.region_id AND c.country_id = l.country_id AND d.location_id = l.location_id AND e.department_id = d.department_id GROUP BY region_name ORDER BY COUNT(employee_id) DESC;

SELECT * FROM EmployeesPerRegion WHERE region_name = "Americas";

-- 2. Write a query to create a view named “managers” to display all the managers. Include the manager’s name (first, last), phone number, email, job title, and department name.
-- Query the managers view to show the number of managers in each department.

CREATE VIEW managers AS SELECT first_name,last_name, phone_number,email,job_title,department_name FROM employees e JOIN jobs j ON j.job_id = e.job_id JOIN departments d ON d.department_id = e.department_id WHERE NOT job_title LIKE '%accountant%' AND job_title NOT LIKE '%Public%' AND phone_number IS NOT NULL AND salary >= 8000;

SELECT department_name, COUNT(first_name) AS "Managers in Department" FROM managers GROUP BY department_name ORDER BY COUNT(first_name) DESC;

-- 3. Write a query to create a view named “DependentsByDepartment” to get a count of how many dependents there are in each department.
-- Query the DependentsByDepartment view to show the department with the largest number of dependents. This should show the department name and the number of dependents.

CREATE VIEW DependentsByDepartment AS SELECT department_name, COUNT(dependents.first_name) AS "NumberOfDependents" FROM departments,employees,dependents WHERE departments.department_id = employees.department_id AND employees.employee_id = dependents.employee_id GROUP BY department_name ORDER BY COUNT(dependents.first_name) DESC;

SELECT * FROM DependentsByDepartment WHERE NumberOfDependents = (SELECT MAX(NumberOfDependents) FROM DependentsByDepartment) GROUP BY department_name ORDER BY NumberOfDependents DESC;
-- 4. Write a query to create a view named “HiresByYear” that calculates the number of employees hired each year. Remember the SQL $year function.
-- Query the HiresByYear view to show the number of hires in 1997.

CREATE VIEW HiresByYear AS SELECT YEAR(hire_date) AS "Year", count(first_name) AS "Employees Hired" FROM employees GROUP BY YEAR(hire_date) ORDER BY YEAR(hire_date) ASC;

SELECT * FROM HiresByYear WHERE Year ="1997";

-- 5. Write a query to create a view named “SalaryByDepartment” to calculate total salaries for each department.
-- Query the SalaryByDepartment view to show the total salary for the Finance department.

CREATE VIEW SalaryByDepartment AS SELECT department_name, SUM(salary) AS "Total Salary" FROM employees e JOIN departments d ON d.department_id = e.department_id GROUP BY department_name ORDER BY SUM(salary) DESC;

SELECT * FROM SalaryByDepartment WHERE department_name = "Finance";

-- 6.Write a query to create a view named “SalaryByJobTitle” to calculate total salaries for each job title.
-- Query the SalaryByJobTitle view to show the job title and total salary for the title with the highest total salary.

CREATE VIEW SalaryByJobTitle AS SELECT job_title, SUM(salary) AS "Total Salary" FROM employees e JOIN jobs j ON j.job_id = e.job_id GROUP BY job_title ORDER BY SUM(salary) DESC;

SELECT * FROM SalaryByJobTitle WHERE job_title = "Accountant";

-- 7. Write a query to create a view named “EmployeeDependents” that calculates the number of dependents each employees has. This query should show employees even if they have 0 dependents. Display the employee name (first, last), email, phone number, and number of dependents. Hint: left or right join.
-- Query the EmployeeDependents view to show employees with no children". Show employee name (first, last), email, phone number, and number of dependents.

CREATE VIEW EmployeeDependents AS SELECT e.first_name, e.last_name, e.email, e.phone_number, COUNT(d.first_name) AS "NumberOfDependents" FROM employees e LEFT JOIN dependents d ON e.employee_id = d.employee_id GROUP BY e.first_name,e.last_name,e.email,e.phone_number ORDER BY COUNT(d.first_name);

SELECT * FROM EmployeeDependents WHERE NumberOfDependents = 0;

-- 8. Write a query to create a view named “CountryLocation” that calculates the number of locations in each country. This query should show countries even if they have 0 locations. Display the country name and number of locations.
-- Query the CountryLocation view to show countries with no locations". Show country name and number of locations.

CREATE VIEW CountryLocation AS SELECT country_name, COUNT(city) AS "NumberofLocations" FROM countries c LEFT JOIN locations l ON c.country_id = l.country_id GROUP BY country_name ORDER BY country_name ASC;

SELECT * FROM CountryLocation WHERE NumberofLocations = 0;