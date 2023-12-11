from flask import Flask, request, jsonify
from dotenv import dotenv_values
from openai import OpenAI

app = Flask(__name__)
config = dotenv_values(".env")

@app.route('/chat', methods=['POST'])
def chat():
  
  data = request.json
  user_input = data.get('message')
  
  
  client = OpenAI(api_key=config['OPENAI_API_KEY'])
  
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": user_input}
    ]
  )
  if response.choices:
    return jsonify({"reply": response.choices[0].message['content']})
  else:
    return jsonify({"reply": "Sorry, No response found."})
    



  
