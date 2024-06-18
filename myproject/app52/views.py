from django.shortcuts import render
import math

def calculate_factorial(request):
    if request.method == 'POST':
        number = int(request.POST.get('number'))
        if 1 <= number <= 10:
            factorial = math.factorial(number)
            return render(request, 'result.html', {'number': number, 'factorial': factorial})
        else:
            error_message = "Please enter a number between 1 and 10."
            return render(request, 'index.html', {'error': error_message})
    return render(request, 'index.html')
