# Copyright 2023 Google LLC & Thunder Develops X Krish Panchani

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import functions_framework  # Import the functions_framework library for HTTP functions
import vertexai  # Import the vertexai library for AI model handling
from vertexai.language_models import ChatModel, InputOutputTextPair
import json  # Import the JSON library for working with JSON data

# Replace with your project ID !!!
PROJECT_ID = "YOUR-PROJECT-ID"  

# Define a function named "summarize" that takes a text input and generates a response
def gen_response(text: str):

    # print(text) #debugging purpose

    vertexai.init(project=PROJECT_ID, location="asia-southeast1")

    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 200,
        "temperature": 0.3,
        "top_p": 0.8,
        "top_k": 40,
    }

    # Initialize the Vertex AI project with the provided project ID
    vertexai.init(project=PROJECT_ID)

    # Load the pre-trained chat-bison model from Vertex AI"

    model = ChatModel.from_pretrained("chat-bison")

    # Start a chat session with the model
    chat = model.start_chat(
    context="""You are Support assistant of Thunder Develops Company.
Thunder Develops is providing service like minecraft hosting, discord bot hosting & web service.
Panel Link: https://panel.thunderdevelops.in
Webiste: https://www.thunderdevelops.in
client often ask you questions about minecaft server development.""",
    )

    PROMPT = """
    {text}
    """
    prompt = PROMPT.format(text=text)

    response = chat.send_message(prompt, **parameters)

    # Print the response from the model
    print(f"Response from Model: {response.text}")

    # Return the generated response as text
    return response.text

# Define an HTTP function using the functions_framework library
@functions_framework.http
def assistant_vertex(request):

    # Call the chatbot function with the message from the HTTP request
    model_response = gen_response(request.data)

    # Define headers for the HTTP response to allow cross-origin requests
    headers = {"Access-Control-Allow-Origin": "*"}

    # Return the model response, HTTP status code 200 (OK), and the headers
    return (model_response, 200, headers)

