from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos

from web.formularios.formularioEmpleados import FormularioEmpleados

from web.models import Platos

from web.models import Empleados

# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def PlatosVista(request):


    #Rutina para consulta de platos
    platosConsultados=Platos.objects.all()
    print(platosConsultados)


    #Esta vista va a utilizar un formulario de django
    #DEBO CREAR ENTONCES UN OBJETO DE LA CLASE FormularioPlatos()
    formulario=FormularioPlatos()

    #CREAMOS UN DICCIONARIO PARA ENVIAR EL FORMULARIO AL HTML(TEMPLATE)
    data={
        'formulario':formulario,
        'bandera':False,
        'platos':platosConsultados
    }

    if request.method=='POST':
        #deberiamos capturar los datos del formulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosPlato=datosDelFormulario.cleaned_data
            #creamos un objeto del tipo MODELO PLATO
            platoNuevo=Platos(
                nombre=datosPlato["nombre"],
                descripcion=datosPlato["descripcion"],
                imagen=datosPlato["fotografia"],
                precio=datosPlato["precio"],
                tipo=datosPlato["tipo"]
            )
            #Intentamos llevar el objeto platoNuevo a LA BD
            try:
                platoNuevo.save()
                data["bandera"]=True
                print("EXITO GUARDANDO LOS DATOS")
            
            except Exception as error:
                print("error",error)
                data["bandera"]=False

    return render(request,'menuplatos.html',data)


def EmpleadosVista(request):
    empleadosConsultados = Empleados.objects.all()
    print(empleadosConsultados)

    formularioEmpleados = FormularioEmpleados()

    data={
        'formulario':formularioEmpleados,
        'bandera':False,
        'empleados':empleadosConsultados
    }

    if request.method=='POST':
        datosDelFormulario=FormularioEmpleados(request.POST)

        if datosDelFormulario.is_valid():
            datosEmpleado=datosDelFormulario.cleaned_data
            empleadoNuevo = Empleados(
                nombre = datosEmpleado["nombre"],
                apellido = datosEmpleado["apellido"],
                cargo = datosEmpleado["cargo"]
            )

            try:
                empleadoNuevo.save()
                data["bandera"]=True
                print("Exito guardando los datos")
            
            except Exception as error:
                print("error",error)
                data["bandera"]=False

    return render(request,'menuempleados.html',data)

