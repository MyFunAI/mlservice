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

    print 'ping server ...'
    client.ping()

    print 'send build model req for dataset1 ...'
    client.buildModel('dataset1', None)

    print 'send predict req using model 1 ...'
    result = client.predict('model1', {1: 0.1, 2: 0.2})

    print 'prediction result', result

    transport.close()

if __name__ == '__main__':
    main()
