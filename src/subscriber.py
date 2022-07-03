import pika

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
        print(type(message))

        if message['type'] == 'simulation':
            print(f" [x] Received simulation message: {message}")
        # if the message is a time message
        elif message['type'] == 'time':
            print(f" [x] Received time message: {message}")
        # if the message is a car state message
        elif message['type'] == 'car':
            print(f" [x] Received car state message: {message}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
