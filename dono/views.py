from django.shortcuts import render,redirect

# Create your views here.
from dono.forms import DonoForm


def cadastro(request):
    form = DonoForm(request.POST or None)
    args = {
        'form':form
    }

    return redirect('/', kwargs={'msg':'Cadastrado com sucesso'})

    
    if form.is_valid():
        form.save()
        args['msg'] = 'Cadastro Realizado com sucesso'

    
     
    return render(request, 'cadastro.html', args) 
