-- settings.sql
CREATE DATABASE teams;
CREATE USER teamsuser WITH PASSWORD 'teams';
GRANT ALL PRIVILEGES ON DATABASE teams TO teamsuser;