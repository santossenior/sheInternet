from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
from .models import VolunteerForm

@csrf_exempt
def submit_volunteer_form(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            print("Received data:", data)  # Debugging

            # Extract form data
            name = data.get('name')
            phone = data.get('phone')
            email = data.get('email')
            contribution = data.get('contribution')
            time_commitment = data.get('time_commitment')
            message = data.get('message', '')

            # Validate required fields
            if not name or not phone or not email or not contribution or not time_commitment:
                return JsonResponse({'status': 'error', 'message': 'All fields are required!'}, status=400)

            # Validate email
            validate_email(email)

            # Save to database
            VolunteerForm.objects.create(
                name=name,
                phone=phone,
                email=email,
                contribution=contribution,
                time_commitment=time_commitment,
                message=message
            )

            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Thank you for your submission!'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data!'}, status=400)
        except ValidationError:
            return JsonResponse({'status': 'error', 'message': 'Invalid email address!'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method!'}, status=405)