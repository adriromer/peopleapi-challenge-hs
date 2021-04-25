FROM mariadb:latest
COPY people.sql /docker-entrypoint-initdb.d/
RUN sed -i 's/#max_connections        = 100/max_connections        = 1000/g' /etc/mysql/mariadb.conf.d/50-server.cnf 
