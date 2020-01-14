from django.shortcuts import render

# Create your views here.
from dono.forms import DonoForm


def cadastro(request):
    form = DonoForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args['msg'] = 'Cadastro Realizado com sucesso'
    return render(request, 'cadastro.html', args)

def delete_people(request, id):
    pessoa = Dono.objects.get(id=id)

    args = {
        'dono': pessoa
    }

    dono.delete()
    return render(request, 'delete_pessoa.html', args)

def update_people(request, id):
    pessoa = Dono.objects.get(id=id)
    form = DonoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(f'../detail/{pessoa.id}')

    args = {
        'dono': pessoa,
        'form':form
    }
    return render(request, 'update_pessoa.html', args)