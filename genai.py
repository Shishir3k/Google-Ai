import google.generativeai as genai


def gemini(command):

    genai.configure(api_key="Your_Google_Genrative_AI_API_Key")

    generation_config = {
      "temperature": 0.9,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 30720,
    }

    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config,
                                  safety_settings=safety_settings)

    response = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["make an ai model using gemini 1.5 pro api"]
    },
    {
        "role": "model",
        "parts": ["## Creating an AI Model with Gemini 1.5 Pro API: A Guide\n\nWhile I can't directly build and deploy a full AI model for you, I can definitely guide you through the process of utilizing the Gemini 1.5 Pro API to achieve your goal.  \n\n**Here's a breakdown of the steps involved:**\n\n**1. Defining Your Goal:**\n\n*   **What kind of AI model are you building?** (e.g., text generation, translation, question answering, etc.)\n*   **What specific tasks should it perform?** \n*   **What kind of data will you use to train it?**\n\n**2. Accessing the Gemini 1.5 Pro API:**\n\n*   **Obtain API credentials** through the Google AI platform or relevant service.\n*   **Explore the API documentation** to understand available endpoints, parameters, and data formats.\n*   **Choose a programming language and library** compatible with the API (e.g., Python with the `google-api-python-client` library).\n\n**3. Data Preparation:**\n\n*   **Gather and clean your data** according to the model's needs and the API's requirements. \n*   **Preprocess the data** as necessary (e.g., tokenization, normalization).\n*   **Structure the data** in a format suitable for the API calls (e.g., JSON).\n\n**4. Model Training and Fine-tuning:**\n\n*   **Select the appropriate API endpoint** based on your model type and task. \n*   **Structure API calls** with your data and desired parameters.\n*   **Iteratively train and fine-tune your model** by analyzing results and adjusting parameters or data.\n\n**5. Integration and Deployment:**\n\n*   **Develop a method to integrate the trained model** into your application or system.\n*   **Consider deployment options** such as cloud-based solutions or local hosting.\n*   **Implement error handling and monitoring** for your model in production.\n\n**Additional Considerations:**\n\n*   **Security:** Ensure secure storage of API credentials and data.\n*   **Cost management:** Be mindful of API usage and associated costs.\n*   **Ethical implications:** Consider the potential bias and fairness of your model.\n\n**Tools and Resources:**\n\n*   **Google AI Platform:** https://cloud.google.com/ai-platform\n*   **Gemini API Documentation:** (Specific link unavailable as of Nov 2023, search for updated documentation)\n*   **Programming libraries:** `google-api-python-client`, other language-specific libraries\n\n**Remember:**  Building and deploying a successful AI model is an iterative process. Be prepared to experiment, learn, and adapt as you go."]
    },
    ])
    
    response.send_message(command)
    print("Gemini: ", response.last.text)

if __name__ == '__main__':
    while True:
        command = input("You: ")
        gemini(command)
        
        if command == "quit":
            break
