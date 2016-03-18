from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from schemas.mlservice import MLService


def main():
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = MLService.Client(protocol)

    transport.open()

    client.ping()
    print('ping()')

    transport.close()

if __name__ == '__main__':
    main()