from paste.httpserver import serve
from pyramid.configuration import Configurator
from pyramid.response import Response

def hola_mundo(request):
    nombre = request.matchdict.get('nombre', 'mundo')
    return Response('Hola {0}!'.format(nombre))

if __name__ == '__main__':
   config = Configurator()
   config.add_route('index', '/')
   config.add_route('hola', '/{nombre}')
   config.add_view(hola_mundo, route_name='hola')
   config.add_view(hola_mundo, route_name='index')

   app = config.make_wsgi_app()
   serve(app, host='0.0.0.0')