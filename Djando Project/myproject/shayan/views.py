from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sum_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        numbers = data.get('numbers', [])
            
        # Check Each element is num or not, in a list
        if not all(isinstance(num, (int, float)) for num in numbers):
            return JsonResponse({'error': 'All items must be numbers'}, status=400)
        total_sum = sum(numbers)  # Sum of a list
            
        return JsonResponse({'sum': total_sum})


@csrf_exempt
def average_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        numbers = data.get('numbers', [])
            
        # Check Each element is num or not, in a list
        if not all(isinstance(num, (int, float)) for num in numbers):
            return JsonResponse({'error': 'All items must be Number'}, status=400)
            
        # Average Code Logic:
        if numbers:
            average = sum(numbers) / len(numbers)
        return JsonResponse({'average': average})
        
@csrf_exempt
def product_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
            
        # Get a list of num in json format
        numbers = data.get('numbers', [])
            
        # Check if all elements of list are num or not
        if not all(isinstance(num, (int, float)) for num in numbers):
            return JsonResponse({'error': 'All items must be Number'}, status=400)
        
        # Multiplication of each number logic :
        product = 1
        for number in numbers:
            product *= number
        return JsonResponse({'Product': product})