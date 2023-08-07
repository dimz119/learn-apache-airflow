-- create the table
CREATE TABLE public.sample_table (
  id serial PRIMARY KEY,
  key VARCHAR ( 50 ) NOT NULL,
     value VARCHAR ( 50 ) NOT NULL
);

-- show table schema
SELECT 
   table_name, 
   column_name, 
   data_type 
FROM 
   information_schema.columns
WHERE 
   table_name = 'sample_table';

-- show data
select * from public.sample_table;
