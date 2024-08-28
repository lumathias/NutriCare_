FROM mariadb:10.5
COPY ./tables.sql /docker-entrypoint-initdb.d/
# COPY ./others/ /docker-entrypoint-initdb.d/

EXPOSE 3306
CMD ["mysqld"]