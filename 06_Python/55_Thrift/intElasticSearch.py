from thrift import Thrift
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.protocol.TBinaryProtocol import TBinaryProtocolAccelerated


from elasticsearch import Rest
from elasticsearch.ttypes import *

import json

socket = TSocket.TSocket("localhost", 9500)
transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocolAccelerated(transport)
client = Rest.Client(protocol)


transport.open()


## Creamos un índice
request = RestRequest(method=1, uri="/linuxmagazine", 
                      headers={}, body="")
client.execute(request)

## Cargamos un modelo de documento
mapping = json.dumps({'properties': { 
            'titulo' : {'type' : 'string', 'store' : 'yes'}}})
request = RestRequest(method=2, uri="/linuxmagazine/articulo", 
                      headers={}, body= mapping)
client.execute(request)


## Cargamos un documento 
articulo = json.dumps({'titulo' : 'Thrift, Python y ElasticSearch'})
request = RestRequest(method=2, 
                      uri='/linuxmagazine/articulo/1', 
                      headers={}, 
                      body= articulo)
respuesta = client.execute(request)


## Buscamos la cadena thrift
ruta = "/linuxmagazine/articulo/_search?q=thrift"
for i in range(0, 100):
    request = RestRequest(method=0, 
                          uri=ruta, 
                          headers={}, 
                          body= '')
    respuesta = client.execute(request)

print json.loads(respuesta.body)["hits"]["hits"]


transport.close()