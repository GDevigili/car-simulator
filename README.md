# car-simulator
 
## Running Instructions


### 0.1. Prerequisites for Python
Make sure that you have all the [requirements]([requirements](https://github.com/GDevigili/car-simulator/blob/main/requirements.txt)) installed. If you don't, you can install them with the following command:

```bash
pip install -r requirements.txt
```

### 0.2. Database Creation

Using a mysql root
```bash
mysql -u root -p
```
execute the SQL script in database/db_create.sql

### Running the Simulation

First you'll need to run the following command to start the rabbitMQ server:

```bash
sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

Then you'll need to start the consumer:

```bash
python3 src/subscriber.py
```

And then serve the consumer with the publisher:
```
python3 src/main.py
```

The interface to visualize the data can be runned with
```bash
python3 src/client.py
```