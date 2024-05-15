SELECT person.firstName, person.lastName, address.city, address.state 
FROM person 
LEFT JOIN address 
ON Person.personId = Address.personId