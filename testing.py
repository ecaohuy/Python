import openai

openai.api_key = "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"

def generate_text(prompt, model="gpt-3.5-turbo", tokens=100, temperature=0.5):
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}]
    
    response = openai.ChatCompletion.create(
        engine=model,
        messages=messages,
        max_tokens=tokens,
        n=1,
        stop=None,
        temperature=temperature,
        top_p=1
    )
    return response.choices[0].message['content']

prompt = "Write a brief summary of the advantages and disadvantages of renewable energy."
output = generate_text(prompt)
print(output)
