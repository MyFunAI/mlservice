from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from schemas.mlservice import MLService
from mlservice_impl import MLServiceImpl


if __name__ == '__main__':
    handler = MLServiceImpl()
    processor = MLService.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print "Starting the MLService server..."
    server.serve()
