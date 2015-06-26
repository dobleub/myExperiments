#!/usr/bin/env python

import sys

from hola import Saludos
from hola.ttypes import *

from thrift.transport import TSocket
from thrift.server import TServer


## Servicio
class SaludosHandler:
    def hola(self,nombre):
        return "Hola {0}".format(nombre)


## Pasos necesarios para arrancar
## el servidor
handler = SaludosHandler()
processor = Saludos.Processor(handler)
transport = TSocket.TServerSocket(9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

## Arrancamos
servidor = TServer.TSimpleServer(processor, transport, tfactory, pfactory)


print 'Arrancando el servidor...'
servidor.serve()
print 'acabamos.'