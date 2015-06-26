from pyramid.view import view_config

@view_config(route_name="portada",
             renderer='ejemplo:templates/portada.html')
def portada(request):
    saludo = 'Hola mundo!!'
    if request.POST:
        nombre = request.params.get('nombre', saludo)
        if nombre:
            saludo = "Hola {0}".format(nombre)

    return {'saludo': saludo}

@view_config(route_name="formulario", 
             renderer='ejemplo:templates/formulario.html')
def formulario(request):
    return {}