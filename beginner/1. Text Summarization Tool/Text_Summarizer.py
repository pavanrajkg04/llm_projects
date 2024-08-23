import openai


openai.api_key =  ""

def summarize_text(text):
    # Use the GPT model for summarization
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Updated to use a newer model
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        max_tokens=150,  # Adjust based on the length of expected summaries
        temperature=0.7,  # Lower temperature for more focused output
    )
    
    # Extract the summary from the response
    summary = response['choices'][0]['message']['content'].strip()
    return summary


short_paragraph = "The sun rises in the east and sets in the west. This daily phenomenon is due to the Earth's rotation on its axis. It takes approximately 24 hours for the Earth to complete one full rotation, resulting in day and night."

summary = summarize_text(short_paragraph)
print("Summary:", summary)