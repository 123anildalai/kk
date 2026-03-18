from flask import Flask, request, jsonify
import sys
import os

# Add parent directories to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
# text_emotion is 4 levels up (backend/backend folder)
sys.path.insert(0, os.path.normpath(os.path.join(current_dir, '../../../../')))
# recommender is 2 levels up (data/backend folder)
sys.path.insert(0, os.path.normpath(os.path.join(current_dir, '../../')))

from text_emotion import detect_text_emotion
from recommender import recommend_songs

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json.get("text")
    emotion = detect_text_emotion(text)
    songs = recommend_songs(emotion).to_dict(orient='records')
    
    return jsonify({"emotion": emotion, "songs": songs})

if __name__ == "__main__":
    app.run(debug=True)