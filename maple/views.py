from django.shortcuts import render, redirect
from .models import Menu, Application, Chicken, Beef
from .forms import MenuForm, ChickenForm, BeefForm

# Create your views here.
def index(request):
    menu_object = Menu.objects.all()
    return render(request, 'maple/index.html', {'menu_object': menu_object})

def menu_list(request):
    menu_object = Menu.objects.all()
    chicken_object = Chicken.objects.all()
    beef_object = Beef.objects.all()
    return render(request, 'maple/menu_list.html', {'beef_object': beef_object, 'chicken_object': chicken_object,
                                                    'menu_object': menu_object})

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        school = request.POST.get('school', '')
        references = request.POST.get('references', '')
        previous_work = request.POST.get('previous_work', '')
        job_position = request.POST.get('job_position', '')
        profile = Application(name=name, email=email, phone=phone, school=school, references=references,
                              previous_work=previous_work, job_position=job_position)
        profile.save()
    return render(request, 'maple/accept.html')

def menu_detail(request, menu_id):
    item = Menu.objects.get(pk=menu_id)
    return render(request, 'maple/menu_detail.html', {'menu': item})

def chicken_detail(request, chicken_id):
    item = Chicken.objects.get(pk=chicken_id)
    return render(request, 'maple/menu_detail.html', {'menu': item})

def beef_detail(request, beef_id):
    item = Beef.objects.get(pk=beef_id)
    return render(request, 'maple/menu_detail.html', {'menu': item})

def create_item(request):
    form = MenuForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('maple:menu_list')

    return render(request, 'maple/menu-form.html', {'form': form})

def create_chicken(request):
    form = ChickenForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('maple:menu_list')

    return render(request, 'maple/menu-form.html', {'form': form})

def create_beef(request):
    form = BeefForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('maple:menu_list')

    return render(request, 'maple/menu-form.html', {'form': form})

def update_item(request, id):
    item = Menu.objects.get(id=id)
    form = MenuForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('maple:menu_list')

    return render(request, 'maple/menu-form.html', {'form': form, 'item': item})

def update_chicken(request, id):
    item = Chicken.objects.get(id=id)
    form = ChickenForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('maple:menu_list')

    return render(request, 'maple/menu-form.html', {'form': form, 'item': item})

def update_beef(request, id):
    item = Beef.objects.get(id=id)
    form = BeefForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('maple:menu_list')

    return render(request, 'maple/menu-form.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = Menu.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('maple:menu_list')

    return render(request, 'maple/item-delete.html', {'item': item})