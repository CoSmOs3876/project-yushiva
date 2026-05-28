import ollama

print("Testing connection to your local AI engine...")

try:
    response = ollama.chat(
        model='llama3', 
        messages=[
            {
                'role': 'user', 
                'content': 'Write a 1-sentence motivation for a computer engineering student.'
            }
        ]
    )
    print("\n🤖 AI Response:")
    print(response['message']['content'])
except Exception as e:
    print(f"\n❌ Error connecting: {e}")
    print("Make sure you ran 'ollama run llama3' in your main Command Prompt first!")