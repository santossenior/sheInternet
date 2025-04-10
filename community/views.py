from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
from .models import SheInternetForm


def submit_form(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            print("Received data:", data)  # Debugging

            # Extract form data
            name = data.get('name')
            email = data.get('email')
            country = data.get('country')
            description = data.get('description')
            interested = data.get('interested')
            about = data.get('about')

            # Validate required fields
            if not name or not email or not country or not description or not interested or not about:
                return JsonResponse({'status': 'error', 'message': 'All fields are required!'}, status=400)

            # Validate email
            validate_email(email)

            # Save to database
            SheInternetForm.objects.create(
                name=name,
                email=email,
                country=country,
                description=description,
                interested=interested,
                about=about
            )

            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Thank you for submitting the form!'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data!'}, status=400)
        except ValidationError:
            return JsonResponse({'status': 'error', 'message': 'Invalid email address!'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method!'}, status=405)