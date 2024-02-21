FROM mariadb:latest

ADD schema.sql /docker-entrypoint-initdb.d
