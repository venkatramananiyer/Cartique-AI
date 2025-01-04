from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Initialize Riva Client (Assuming Riva is set up with necessary services like ASR and NLP)
RIVA_SERVER = 'http://your-riva-server-url'
RIVA_ASR_ENDPOINT = '/riva/api/asr'
RIVA_NLP_ENDPOINT = '/riva/api/nlp'

@app.route('/')
def home():
    return "Welcome to Viteefe's Personalized Shopping Assistant!"

@app.route('/process_audio', methods=['POST'])
def process_audio():
    # Get the audio file sent from the frontend
    audio_file = request.files['audio']
    
    # Send to NVIDIA Riva's ASR Service for Speech Recognition
    audio_data = audio_file.read()
    response = requests.post(f'{RIVA_SERVER}{RIVA_ASR_ENDPOINT}', data=audio_data)

    if response.status_code == 200:
        # Assuming Riva returns the transcribed text
        transcribed_text = response.json().get('transcription')

        # Now process this text using NVIDIA Riva's NLP for product recommendations
        nlp_data = {
            'query': transcribed_text
        }
        nlp_response = requests.post(f'{RIVA_SERVER}{RIVA_NLP_ENDPOINT}', json=nlp_data)

        if nlp_response.status_code == 200:
            # Assuming Riva NLP returns product recommendations
            recommendations = nlp_response.json().get('recommendations')
            return jsonify({'status': 'success', 'recommendations': recommendations})

        else:
            return jsonify({'status': 'error', 'message': 'NLP service failed'})

    else:
        return jsonify({'status': 'error', 'message': 'ASR service failed'})

if __name__ == '__main__':
    app.run(debug=True)
