
__author__ = "germanb"


import clr
clr.AddReference('System.Web.Extensions')
from System.Net import WebClient
from System.Text import Encoding
from System.Web.Script.Serialization import JavaScriptSerializer

def chat_with_gpt(prompt):
    # Your OpenAI API key


    # Set up the API URL (adjust the URL for the GPT-3.5 Turbo model)
    url = 'https://api.openai.com/v1/completions'

    # Prepare the request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {0}'.format(api_key)
    }

    # Prepare the data to be sent
    data = {
        "model": "text-davinci-003",
        'prompt': prompt,
        'max_tokens': 100,
        'temperature': 0.7,
        'top_p': 1
    }

    # Serialize the data to JSON
    serializer = JavaScriptSerializer()
    json_data = serializer.Serialize(data)

    # Create a WebClient instance
    client = WebClient()
    for key, value in headers.items():
        client.Headers.Add(key, value)

    # Send the request and receive the response
    response = client.UploadString(url, json_data)

    # Deserialize the response
    result = serializer.DeserializeObject(response)

    return result['choices'][0]['text']

# Example usage

response = chat_with_gpt(prompt)
print(response)
