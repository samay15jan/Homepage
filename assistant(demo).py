import openai, os

openai.api_key = "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"

while True : 
    text = input(" You >> ")
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        temperature=0.5,
        max_tokens=100,
    )
    
    print(" Chatgpt >> ", completion.choices[0].message["content"])
