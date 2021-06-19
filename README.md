# MQTT Python MySql Subscriber

MQTT Subscriber save to MySql with Python

## Description

This code provides a minimal use of Eclipse Paho MQTT Python client library as Subscriber and stored data received into MySqL

## Getting Started

### Dependencies

- Python 3.8.8
- MariaDB 10.4

### Installing

- Install paho-mqtt [1.5.1](https://pypi.org/project/paho-mqtt/1.5.1/)
- Install mysqlclient [2.0.3](https://pypi.org/project/mysqlclient/2.0.3/)

### Executing program

- Execute query t make a tabel

  ```sql
      CREATE TABLE tableName (
          value varchar(255)
      );
  ```

- Open Python command prompt
- Change the variable before executing the code

  ```python
    # MQTT
    broker_address = "broker.emqx.io"
    port = 1883
    topic = "same/topic"

    # MySql
    db_address = "localhost"
    db_user = "root"
    db_pass = ""
    db_name = ""
  ```

- Execute code

  ```console
    python3 mqtt_sub_mysql.py
  ```

  or

  ```console
    python mqtt_sub_mysql.py
  ```

## Help

- Access denied for user
  [ref](https://stackoverflow.com/questions/39281594/error-1698-28000-access-denied-for-user-rootlocalhost)

  > (1698, "Access denied for user 'root'@'localhost'")

  ```sql
    USE mysql;
    UPDATE user SET plugin='mysql_native_password' WHERE User='root';
    FLUSH PRIVILEGES;
  ```

## Authors

Contributors names and contact info

[@zuhairatoir](https://twitter.com/zuhairatoir)

## Version History

- 1.0
  - Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.

- [Eclipse paho](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)
