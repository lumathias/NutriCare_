FROM mariadb:10.5
COPY ./nutricare.mysql /docker-entrypoint-initdb.d/

EXPOSE 3306
CMD ["mysqld"]