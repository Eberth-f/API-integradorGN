
-- create integrador default database
CREATE USER integradorgn WITH PASSWORD 'integradorgn';
CREATE DATABASE integradorgn WITH OWNER postgres;
\connect  integradorgn;
CREATE SCHEMA integradorgn AUTHORIZATION postgres;

-- create datalake database
CREATE DATABASE datalake WITH OWNER postgres;
\connect datalake;
CREATE SCHEMA vendas AUTHORIZATION postgres;

-- check this permissions
-- GRANT USAGE ON SCHEMA some_schema_ TO some_user_ ;
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO some_user_;
-- GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO some_user_;

