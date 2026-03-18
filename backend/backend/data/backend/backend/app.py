from flask import Flask, request, jsonify
import sys
import os

# Add parent directories to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
# text_emotion is 3 levels up
sys.path.insert(0, os.path.normpath(os.path.join(current_dir, '../../../')))
# recommender is 1 level up
sys.path.insert(0, os.path.normpath(os.path.join(current_dir, '../')))

from text_emotion import detect_text_emotion
from recommender import recommend_songs
from emotion_detector import detect_face_emotion

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    mode = request.json.get("mode")
    
    if mode == "face":
        emotion = detect_face_emotion()
    else:
        text = request.json.get("text")
        emotion = detect_text_emotion(text)
    
    songs = recommend_songs(emotion).to_dict(orient='records')
    
    return jsonify({"emotion": emotion, "songs": songs})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
}