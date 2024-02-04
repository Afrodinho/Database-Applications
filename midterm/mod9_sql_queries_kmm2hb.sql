--1.Display the customer first name, last name, and movie titles the rented in 2006. Sort result by customer last name. 
SELECT DISTINCT title, first_name, last_name FROM customer,film,rental,inventory WHERE customer.customer_id = rental.customer_id AND rental.inventory_id = inventory.inventory_id AND inventory.film_id = film.film_id AND rental.rental_date BETWEEN '2006-1-1' AND '2006-12-31' ORDER BY last_name;

--2.How many films are in each category? List the category name in a column called "Category Name" and number of films in the category in a column called "Number of Films". Sort by number of films in descending order
SELECT category.name AS 'Category Name', COUNT(title) AS "Number of Films" FROM category,film,film_category WHERE film.film_id = film_category.film_id AND film_category.category_id = category.category_id GROUP BY category.name ORDER BY COUNT('title') DESC;

--3.Calculate each customer's total payments and display the top 15 customers in terms of total payments in descending order. Display the customer first and last name and total payment amount in a column called "Total Payments".
SELECT customer.first_name, customer.last_name, SUM(amount) AS "Total Payments" FROM customer,payment WHERE customer.customer_id = payment.customer_id GROUP BY customer.customer_id ORDER BY SUM(amount) DESC LIMIT 15;

--4.Calculate the total payments for each store. Display store id and total payments in a Column called Total Payments. Display results in descending order by total payments
SELECT store.store_id, SUM(amount) AS "Total Payments" FROM store,payment,staff WHERE store.store_id = staff.store_id AND staff.staff_id = payment.staff_id GROUP BY store_id ORDER BY SUM(amount) DESC;

--5.Which films are rented the most? Display the Film name and the total rentals in a column called "Total Rentals". Display results in descending order by total rentals.
SELECT title, COUNT(rental_date) AS "Total Rentals" FROM film,inventory,rental WHERE film.film_id = inventory.film_id AND inventory.inventory_id = rental.inventory_id GROUP BY title ORDER BY COUNT(rental_date) DESC;

--6.Which Film categories are rented the most? Display the category name and the total rentals in a column called "Total Rentals". Display results in descending order by total rentals.
SELECT category.name, COUNT(rental_date) AS "Total Rentals" FROM category, film_category, film,inventory,rental WHERE category.category_id = film_category.category_id AND film_category.film_id = film.film_id AND film.film_id = inventory.film_id AND inventory.inventory_id = rental.inventory_id GROUP BY category.name ORDER BY COUNT(rental_date) DESC;

--7.Display the inventory list of movie titles for store number 1. Display the film title and quantity in stock in a column named "In Stock". Display results in alphabetical order of the titles. 
SELECT film.title, COUNT(inventory_id) AS "In Stock" FROM film,inventory WHERE film.film_id = inventory.film_id AND store_id = 1 GROUP BY title ORDER BY title ASC; 

--8. Which actors have acted in the most movies? List the actor first and last name and the number of movies in a column named "Number of Movies". Display results in descending order by number of movies.
SELECT actor.first_name, actor.last_name, COUNT(film.title) AS "Number of Movies" FROM actor,film_actor,film WHERE actor.actor_id = film_actor.actor_id AND film_actor.film_id = film.film_id GROUP BY actor.actor_id ORDER BY COUNT(film.title) DESC;