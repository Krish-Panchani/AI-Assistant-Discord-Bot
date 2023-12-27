import requests
import json
# ... (server setup and authentication code, if applicable)
PUBLIC_FUNCTION_URL = "YOUR CLOUD FUNCTION URL"

def handle_request(user_input):
    data = {'input': user_input}  # Assuming the function expects 'input'
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(PUBLIC_FUNCTION_URL, json=data, timeout=10, headers=headers)  # Set a timeout
    print(response.text)  # Print the response (for debugging)

    if response.status_code == 200:
      return response.text
    else:
      print(f"Error: {response.status_code}")
      default_error = "Error: Something went wrong"
      return default_error
    # Handle error appropriately