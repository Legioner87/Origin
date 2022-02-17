#Составьте одно любое выражение, использующее UNION!!(вывод списка всех напитков и продуктов)
SELECT name as Список_всех_напитков_и_продуктов
FROM drinks
UNION
SELECT productName
FROM products;

#Составьте одно любое выражение,
	#использующее CTE (оператор WITH), внутри которого будет использован JOIN
    #Вывод всех служащих офиса у которых присутствует адрес проживания!!!!))))
with cte_offices_employees as(
select concat(e.lastName,'   ',e.firstName) as Фамилия_и_имя,
e.email,
o.phone as Телефон,
e.jobTitle as Должность,
o.city as Город,
concat(o.addressLine1,'     ',o.addressLine2) as Адрес_проживания
from offices o
	join employees e
		using(officeCode)
where addressLine1 and addressLine2 is not null
order by Фамилия_и_имя
)
select *
from cte_offices_employees




