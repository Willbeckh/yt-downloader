from flask import Flask, render_template, request, url_for
from pytube import YouTube
from pytube.extract import video_id

app = Flask(__name__)
app.config['SECRET_KEY'] = "12345678abcd"

def download(url):
  """downloads the video as of the link provided"""
  
  video = url.streams.first()
  video.download()

@app.route("/", methods=['POST', 'GET'])
def home():
  if request.method == 'POST':
    url = YouTube(request.form.get('url'))
    download(url)
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)