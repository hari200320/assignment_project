from django.shortcuts import render
import math

def calculate(request):
    n1 = 5
    square = n1 * n1
    factorial = math.factorial(n1)
    context = {
        'number': n1,
        'square': square,
        'factorial': factorial
    }
    return render(request, 'app51result.html', context)
