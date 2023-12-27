import functions_framework  # Import the functions_framework library for HTTP functions
import vertexai  # Import the vertexai library for AI model handling
from vertexai.language_models import ChatModel, InputOutputTextPair
import json  # Import the JSON library for working with JSON data

# Replace with your project ID !!!
PROJECT_ID = "YOUR-PROJECT-ID"  

# Define a function named "summarize" that takes a text input and generates a response
def gen_response(text: str):
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 200,
        "temperature": 0.3,
        "top_p": 0.8,
        "top_k": 40,
    }

    # Initialize the Vertex AI project with the provided project ID
    vertexai.init(project=PROJECT_ID)

    # Load the pre-trained TextGenerationModel named "text-bison@001"
    model = ChatModel.from_pretrained("chat-bison")

    # Generate a response by providing the input text and model parameters
    chat = model.start_chat(
    context="""You are Support assistant of Thunder Develops Company""",
)

    response = chat.send_message("{text}", **parameters)
    # Print the response from the model
    print(f"Response from Model: {response.text}")

    # Return the generated response as text
    return response.text

# Define an HTTP function using the functions_framework library
@functions_framework.http
def assistant_vertex(request):
    # Process and clean the input data received from the HTTP request
    parsed_data = (str(request.data)).replace('"', "").replace("'", "").replace(",", "").replace("\n", "")

    # Call the "summarize" function with the cleaned input data to generate a model response
    model_response = gen_response(parsed_data)

    # Define headers for the HTTP response to allow cross-origin requests
    headers = {"Access-Control-Allow-Origin": "*"}

    # Return the model response, HTTP status code 200 (OK), and the headers
    return (model_response, 200, headers)