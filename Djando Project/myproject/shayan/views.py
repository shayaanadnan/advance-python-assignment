import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Helper functions
def handle_post_request(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method allowed only"}, status=405)
    try:
        return json.loads(request.body), None
    except json.JSONDecodeError:
        return None, JsonResponse({"error": "Invalid JSON data"}, status=400)

def calculate_per_person_amount(total, count):
    return round(total / count, 2) if count else 0

# View functions
@csrf_exempt
def split_evenly(request):
    data, error_response = handle_post_request(request)
    if error_response:
        return error_response

    user_ids = data.get('user_ids', [])
    total_bill = data.get('total_bill', 0)
    
    if not user_ids or total_bill <= 0:
        return JsonResponse({"error": "Invalid user_ids or total_bill"}, status=400)

    per_person_bill = calculate_per_person_amount(total_bill, len(user_ids))
    return JsonResponse({"bill_per_person": per_person_bill})

@csrf_exempt
def split_unevenly(request):
    data, error_response = handle_post_request(request)
    if error_response:
        return error_response

    contributions = data.get('contributions', [])
    total_bill = data.get('total_bill', 0)

    if not contributions or total_bill <= 0:
        return JsonResponse({"error": "Invalid contributions or total_bill"}, status=400)

    per_person_bill = calculate_per_person_amount(total_bill, len(contributions))
    
    result = [{
        "user_id": user.get("user_id"),
        "total_bill_to_pay": per_person_bill,
        "user_pay_bill": user.get("contribution", 0),
        "receive_from_other": max(0, user.get("contribution", 0) - per_person_bill),
        "pay_to_other": max(0, per_person_bill - user.get("contribution", 0))
    } for user in contributions]

    return JsonResponse({"bill_details": result})

@csrf_exempt
def split_evenly_include_tip_tax(request):
    data, error_response = handle_post_request(request)
    if error_response:
        return error_response

    user_ids = data.get('user_ids', [])
    total_bill = data.get('total_bill', 0)
    tip_percentage = data.get('tip_percentage', 0)
    tax_percentage = data.get('tax_percentage', 0)

    if not user_ids or total_bill <= 0:
        return JsonResponse({"error": "Invalid user_ids or total_bill"}, status=400)

    total_with_tip_tax = total_bill * (1 + (tip_percentage + tax_percentage) / 100)
    per_person_bill = calculate_per_person_amount(total_with_tip_tax, len(user_ids))
    return JsonResponse({"bill_per_person_with_tip_tax": per_person_bill})

@csrf_exempt
def split_evenly_include_discount(request):
    data, error_response = handle_post_request(request)
    if error_response:
        return error_response

    user_ids = data.get('user_ids', [])
    total_bill = data.get('total_bill', 0)
    discount_percentage = data.get('discount_percentage', 0)

    if not user_ids or total_bill <= 0:
        return JsonResponse({"error": "Invalid user_ids or total_bill"}, status=400)

    total_with_discount = total_bill * (1 - discount_percentage / 100)
    per_person_bill = calculate_per_person_amount(total_with_discount, len(user_ids))
    return JsonResponse({"bill_per_person_with_discount": per_person_bill})

@csrf_exempt
def split_include_shared_items(request):
    data, error_response = handle_post_request(request)
    if error_response:
        return error_response

    items_detail = data.get('items_detail', [])
    
    if not items_detail:
        return JsonResponse({"error": "Missing items_detail"}, status=400)

    result = [{
        "user_id": user_id,
        "per_person_amount": calculate_per_person_amount(item.get("item_price", 0), len(item.get("share_with", [])))
    } for item in items_detail for user_id in item.get("share_with", [])]

    return JsonResponse({"amount_due_of_each_user": result})
