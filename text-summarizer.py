import requests

def summarize_text(text):
    """
    Summarize the provided text using OpenAI's API.

    Parameters:
    text (str): The text to summarize.

    Returns:
    str: The summarized text.
    """
    api_url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer OpenAI-API-key"  # Replace YOUR_API_KEY with your actual OpenAI API key
    }
    data = {
        "model": "gpt-3.5-turbo-instruct",  # You can change the model based on your specific needs and availability
        "prompt": "Summarize the following paragraph:\n\n" + text,
        "max_tokens": 150  # Adjust max_tokens as needed for the length of the summary
    }

    response = requests.post(api_url, json=data, headers=headers)
    response_data = response.json()
    return response_data["choices"][0]["text"]

# Example usage:``
paragraph = input("Submit you text to summarize: ")
summary = summarize_text(paragraph)
print("Summary:", summary)
