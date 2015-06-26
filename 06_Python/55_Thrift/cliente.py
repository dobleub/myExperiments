import sys
from hola import Saludos
from hola.ttypes import *
from hola.constants import *
 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
 
try:
  transport = TSocket.TSocket('localhost', 9090)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)


  cliente = Saludos.Client(protocol)
 
  ## Conectamos
  transport.open()
 
  cadena = cliente.hola("mundo")
  print cadena

  ## Cerramos la conexión
  transport.close()
except Thrift.TException, tx:
  print "%s" % (tx.message)