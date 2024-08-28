FROM mariadb:10.5
COPY ./table.sql /docker-entrypoint-initdb.d/
#COPY ./nutricare.mysql /docker-entrypoint-initdb.d/
#COPY ./AlimentosBrasileiros.csv /docker-entrypoint-initdb.d/

EXPOSE 3306
CMD ["mysqld"]