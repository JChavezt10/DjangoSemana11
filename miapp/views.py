from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango"> Mostrar Números [a,b]</a>
        </li>
    </ul>
    <hr/>
"""
def index(request):
    estudiantes = ['David Rosado',
                'Jhon Tapia', 
                'Leonardo Vera',
                'Yhamir Maldonado']
    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto web en Django',
        'estudiantes' : estudiantes
        })

def saludo(request):
    return render(request,'saludo.html',{
        'titulo':'Saludo',
        'autor_saludo':'Mg. Flor Elizabeth Cerdán León'
        })

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })

def rango2(request,a=0,b=100):
    if a>b:
        return redirect('rango2',a=b, b=a)
    resultado = f"""
        <h2> Números de [{a},{b}] </h2>"""
    return HttpResponse(layout + resultado)