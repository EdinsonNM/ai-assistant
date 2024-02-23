import os
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

audio_file=open("audio.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print("Audio Transcription: ", transcript.text)

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")