Explain
SELECT customerNumber, contactFirstName, contactLastName
FROM customers
WHERE contactLastName ='King'and contactFirstName = 'Jean';
# Добавить составной индекс на таблицу customers. Он должен состоять из фамилии и имени
create index ix_last_name_and_firs_name
on customers (contactLastName,contactFirstName);
#В рамках транзакции выполнить удаление из таблицы shows и откатить изменения

start transaction;
delete  from shows;
rollback;
select * from shows;






