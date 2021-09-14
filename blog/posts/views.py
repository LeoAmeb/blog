from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render


class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Leonardo Amaya Escobedo',
            'age': 22,
            'codes': ['Python', 'php', 'javascript', 'C++']
        }
        return render(request, 'hello_world.html', context = data)