<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to General topics portal</a>

  

# Databases

* sqlite 

```sql
CREATE TABLE 'table_name' ('id' integer, 'name' varchar(255));
INSERT INTO table_name ('id', 'name') VALUES (1, 'myname');
UPDATE table_name SET name = 'mysecondname' WHERE id = 1;
DELETE FROM table_name WHERE id = 1;
```

* Use libraries to escape user input - avoid using f strings to format sql strings, but rather use a library to plug in placeholder syntax with sanitization.
