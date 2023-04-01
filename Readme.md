### Before install dependency:

Mac OS:
```commandline
brew install postgresql
```

Unix like:

```commandline
sudo apt-get install libpq-dev python-dev
```

### Run all containers with databases:
```commandline
make up
```
### To run particular container check [Makefile](Makefile)

### Stop all containers:
```commandline
make down
```

### Useful links:
[Postgres](https://www.psycopg.org/docs/usage.html#basic-module-usage)

[MongoDB](https://pymongo.readthedocs.io/en/stable/tutorial.html)

[Mysql](https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html)