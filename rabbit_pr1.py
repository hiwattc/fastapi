import pika

class Publisher:
    def __init__(self):
        self.__url = '127.0.0.1'
        self.__port = 5672
        self.__vhost = '/'
        self.__cred = pika.PlainCredentials('guest', 'guest')
        self.__queue = 'test_q1'
        return

    def main(self):
        conn = pika.BlockingConnection(pika.ConnectionParameters(self.__url, self.__port, self.__vhost, self.__cred))
        chan = conn.channel()
        chan.basic_publish(
            exchange = 'amq.topic',
            routing_key = self.__queue,
            body = 'Hello RabbitMQ'
        )
        conn.close()
        return

publisher = Publisher()
publisher.main()
