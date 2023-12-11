from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
from openai import OpenAI


app = Flask(__name__, template_folder="template")
CORS(app)

config = dotenv_values(".env")

@app.route('/chat', methods=['POST'])
def chat():
  try:
  
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
      return jsonify({"reply": response.choices[0].message.content})
    else:
      return jsonify({"reply": "Sorry, No response found."})
  except Exception as e:
    return jsonify({"error": str(e)}), 500

    
if __name__ == '__main__':
    app.debug = True
    app.run()
    debug= True 


  
