from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
from .models import PartnerForm

@csrf_exempt
def submit_partner_form(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            print("Received data:", data)  # Debugging

            # Extract form data
            name = data.get('name')
            organization = data.get('organization')
            email = data.get('email')
            message = data.get('message')

            # Validate required fields
            if not name or not organization or not email or not message:
                return JsonResponse({'status': 'error', 'message': 'All fields are required!'}, status=400)

            # Validate email
            validate_email(email)

            # Save to database
            PartnerForm.objects.create(
                name=name,
                organization=organization,
                email=email,
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