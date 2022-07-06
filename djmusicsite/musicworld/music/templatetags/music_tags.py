from django import template
from music.models import *
register = template.Library()
menu = [
        {'title':'Співаки', 'url_name':'singers'},
        {'title':'Автори', 'url_name':'authors'},
        {'title':'Бібліотеки', 'url_name':'libraries'},
        {'title':'Рейтинг', 'url_name':'rating'},
        {'title':'Додати інформацію', 'url_name':'add'},
        {'title':'Завдання', 'url_name':'task'},
        {'title':'Вхід', 'url_name':'authorization'},
]


@register.inclusion_tag('music/list_menu.html')
def show_menu(menu_selected=0):
    return {'menu': menu, 'menu_selected': menu_selected}


@register.inclusion_tag('music/list_genres.html')
def show_genres(sort=None, genre_id=0):
    if not sort:
        genres = Genre.objects.all()
    else:
        genres = Genre.objects.order_by(sort)
    return {'genres': genres, 'genre_id': genre_id}