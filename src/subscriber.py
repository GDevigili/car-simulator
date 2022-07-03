import pika

import database.db_access as db

db_connection = db.connect()
if db_connection:
    print(" [x] Connection to the database successful")
else:
    print(" [x] Error connecting to the database")

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    # if the message is a dictionary
    message = body.decode('utf-8')
    # if the message is a simulation message
    if '{' in message:
        message = eval(message)

        if message['type'] == 'simulation':
            # print(f" [x] Received simulation message")
            if db.insert_scenario(db_connection, message):
                # print(f"   [x] Simulation data inserted in the database successfully")
                pass
            else:
                print(f"   [x] Error inserting simulation data in the database")
        # if the message is a time message
        elif message['type'] == 'time':
            # print(f" [x] Received time message")
            if db.insert_tick(db_connection, message):
                # print(f"   [x] Time data inserted in the database successfully")
                pass
            else:
                print(f"   [x] Error inserting time data in the database")
        # if the message is a car state message
        elif message['type'] == 'car':
            # print(f" [x] Received car state message")
            if db.insert_car_state(db_connection, message):
                # print(f"   [x] Car state data inserted in the database successfully")
                pass
            else:
                print(f"   [x] Error inserting car state data in the database")
    else:
        print(f" [x] Received message: {message}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
