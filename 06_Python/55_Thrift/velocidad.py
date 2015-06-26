import sys
sys.path.append('./gen-py')
 
from hola import Saludos
from hola.ttypes import *
from hola.constants import *
 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


transport = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

cliente = Saludos.Client(protocol)

transport.open()

 
for i in range(0,10000):
  cadena = cliente.hola("mundo")

transport.close()