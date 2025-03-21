from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
from .models import Subscriber

 # Disable CSRF for simplicity (use proper CSRF handling in production)
def subscribe(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            print("This is the data", data)
            name = data.get('name')
            email = data.get('email')

            # Validate email
            validate_email(email)

            # Check if email already exists
            if Subscriber.objects.filter(email=email).exists():
                return JsonResponse({'status': 'error', 'message': 'Email already subscribed!'}, status=400)

            # Save to database
            Subscriber.objects.create(name=name, email=email)

            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Thank you for subscribing!'})

        except ValidationError:
            return JsonResponse({'status': 'error', 'message': 'Invalid email address!'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method!'}, status=405)