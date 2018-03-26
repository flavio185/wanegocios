from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .forms import NotaForm, UserQueryForm
from .models import Nota, UserQuery


# Create your views here.

#class CriaNota(CreateView):
#    model = NotasCompra
    #fields = ['numero', 'data', 'descricao', 'valor', 'tipo_gasto', 'imagem', 'imagem1'] 
#    fields = ['numero', 'data', 'descricao', 'valor', 'tipo_gasto'] 
#    template_name = "adiciona-nota.html"
 
# Create your views here.

def nota_list(request):
    notas = Nota.objects.all()
    context = {'notas': notas, 'media_url':"/media/"}
    return render(request, 'notas/nota_list.html', context)

def nota_query(request):
    #notas = Nota.objects.filter(data__range=[dados, "2018-03-31"])
    notas = Nota.objects.filter(data > "2018-03-31")
    #nota = get_object_or_404(Nota, pk=pk)

    context = {'notas': notas}
    return render(request, 'notas/nota_list.html', context)


def nota_filter(request):
    notas = Nota.objects.all()
    query = "Nota.objects.all()"

    if 'data_inicio' in request.GET and request.GET['data_inicio']:
        #message = 'You searched for: %r' % request.GET['data_inicio']
        data_inicio = request.GET['data_inicio']
        notas = notas.filter(data__gte=data_inicio)
        query += ".filter(data__gte='"+data_inicio+"')"

    if 'data_fim' in request.GET and request.GET['data_fim']:
        #message = 'You searched for: %r' % request.GET['data_inicio']
        data_fim = request.GET['data_fim']
        notas = notas.filter(data__lte=data_fim)
        query += ".filter(data__lte='"+data_fim+"')"

    
    context = {'notas': notas, 'query': query}
    
    return render(request, 'notas/nota_list.html', context)
        
    #else:
    #    message = 'You submitted an empty form.'
    #return HttpResponse(message)

def nota_filter_form(request):
    return render(request, 'notas/nota_filter_form.html')


def nota_nova(request):
    if request.method == "POST":
        form = NotaForm(request.POST, request.FILES)
        if form.is_valid():
            #numero = form.cleaned_data['numero']
            #data = form.cleaned_data['data']
            #descricao = form.cleaned_data['descricao']
            #valor = form.cleaned_data['valor']
            #tipo_gasto = form.cleaned_data['tipo_gasto']
            form.save()
            return redirect('notas/nota_detalhes.html', pk=numero.pk)
    else:
        form = NotaForm()
    return render(request, 'notas/nota_edit.html', {'form': form})    

def nota_edit(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == "POST":
        form = NotaForm(request.POST, request.FILES, instance=nota)
        if form.is_valid():
            #numero = form.cleaned_data['numero']
            #data = form.cleaned_data['data']
            #descricao = form.cleaned_data['descricao']
            #valor = form.cleaned_data['valor']
            #tipo_gasto = form.cleaned_data['tipo_gasto']
            form.save()
            return redirect('notas/nota_detalhes.html', pk=nota.pk)
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/nota_edit.html', {'form': form})

def nota_detalhes(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    return render(request, 'notas/nota_detalhes.html', {'nota': nota})

#salva query para colocar na home page dos usuarios. especifico pra cada usuario.
def nova_query(request):
    if requet.method == "POST":
        form = UserQueryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notas/nota_list.htm')
    else:
        form = UserQueryForm()
#corrigir aqui.
    return render(requet, 'notas/nota_list.html')
