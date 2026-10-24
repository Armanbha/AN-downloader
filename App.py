
from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "Backend is running!"

@app.route('/api/download', methods=['POST', 'GET'])
def get_video_info():
    data = request.get_json(silent=True) or {}
    url = data.get('url') or request.args.get('url')

    if not url:
        return jsonify({'error': 'Link missing'}), 400

    try:
        ydl_opts = {'format': 'best', 'quiet': True, 'no_warnings': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({
                'status': 'success',
                'title': info.get('title'),
                'thumbnail': info.get('thumbnail'),
                'download_url': info.get('url'),
                'url': info.get('url')
            })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


।
