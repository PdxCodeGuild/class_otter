from django.shortcuts import render, get_object_or_404
from .models import Pokemon
# # Create your views here.
# from django.http.response import JsonResponse
# from django.shortcuts import get_object_or_404, render

# # Create your views here.
# from .models import Pokemon


def base_edit(request):
    return render(request, 'pokemon/edit.html')

def base_delete(request):
    return render(request, 'pokemon/delete.html')

def base_add(request):
    return render(request, 'pokemon/add.html')

def pokemonedit(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    context = {
        'pokemon': pokemon
    }
    return render(request, '/pokemon.html', context)


# def api_list(request):
#     pokemon = Pokemon.objects.all()
#     response = {'data': []}
#     for mon in pokemon:
#         response['data'].append({
#             'name': mon.name,
#             'number': mon.number,
#             'height': mon.height,
#             'weight': mon.weight,
#             'image_front': mon.image_front,
#             'image_back': mon.image_back
#         })
#     return JsonResponse(response)


# def api_updated(request, number):
#     pokemon = get_object_or_404(Pokemon, number=number)
#     db_types = pokemon.types.all()
#     types = []
#     for type in db_types:
#         types.append(type.name)
#     response = {
#         'name': pokemon.name,
#         'number': pokemon.number,
#         'height': pokemon.height,
#         'weight': pokemon.weight,
#         'image_front': pokemon.image_front,
#         'image_back': pokemon.image_back,
#         'types': types
#     }

#     return JsonResponse(response)