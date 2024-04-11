from django.shortcuts import render
from .models import MenuItem

def draw_menu(request, menu_name):
    menu_items = MenuItem.objects.filter(parent=None)
    context = {
        'menu_items': menu_items
    }
    return render(request, 'menu/menu.html', context)