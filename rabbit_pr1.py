import pika
import uuid
class Publisher:
    def __init__(self):
        self.__url = '192.168.56.22'
        self.__port = 5672
        self.__vhost = '/'
        self.__cred = pika.PlainCredentials('test', 'test')
        self.__queue = 'test_q1'
        #self.__queue = 'ha_test_q_1'
        return

    def main(self):
        conn = pika.BlockingConnection(pika.ConnectionParameters(self.__url, self.__port, self.__vhost, self.__cred))
        chan = conn.channel()
        while True:
            chan.basic_publish(
            exchange = 'amq.topic',
            #exchange = 'amq.fanout',
            routing_key = self.__queue,
            body = 'Hello RabbitMQ'+str(uuid.uuid1()))
        conn.close()
        return

publisher = Publisher()
publisher.main()
