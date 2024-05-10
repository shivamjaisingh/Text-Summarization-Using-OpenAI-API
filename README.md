# Text Summarizer Using OpenAI API

This Python program uses the OpenAI API to summarize text. It sends a request to the OpenAI server, which processes the text and returns a concise summary. This can be useful for generating quick summaries of large texts or documents to capture the main points.

## Installation

Before you can run the program, you need to install the required Python library. Use the following command to install the `requests` library, if it's not already installed:

```bash
pip install requests
```

## Configuration
You need to obtain an API key from OpenAI to use their API. Once you have the API key, replace OpenAI-API-key in the headers dictionary with your actual API key:

```python
"Authorization": "Bearer YOUR_API_KEY"
```

