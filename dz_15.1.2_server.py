import socket
import logging


def server():
    port = 54321
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))

    server_socket.listen(10)
    logging.info('Server started')

    while True:
        try:
            connection, address = server_socket.accept()
            logging.info('Connection: %s', address)

            client_message = str(connection.recv(1024), encoding='UTF-8')
            if client_message == 'close':
                connection.close()
                logging.warning('Server closed by client')
                break

            server_message = input('Enter message: ')
            logging.info('Sending message')
            connection.send(bytes(server_message, encoding='UTF-8'))
            connection.close()
            logging.info('Message sent')
        except Exception as error:
            logging.error('Error', exc_info=error)


server()
