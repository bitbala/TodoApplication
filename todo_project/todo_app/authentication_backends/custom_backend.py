import json
import requests
from django.contrib.auth.models import User
import os

class MicroserviceBackend:
    def authenticate(self, request, username=None, password=None):
        if not username or not password:
            return None
        
        # Forward authentication request to microservice
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'email': username, 'password': password})
        domain = os.environ.get('AUTH_DOMAIN')
        response = requests.post(f'http://{domain}/account/api/login/', headers=headers, data=data)

        # Check if authentication successful
        if response.status_code == 200:
            user_data = response.json()  # Assuming microservice returns user data
            user, _ = User.objects.get_or_create(username=username)  # Create user locally if not exists
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
