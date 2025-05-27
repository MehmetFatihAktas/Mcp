from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_word_definition', methods=['POST'])
def get_word_definition():
    data = request.json
    word = data.get('word')
    if not word:
        return jsonify({'error': 'word is required'}), 400

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return jsonify({'error': 'Word not found or API error'}), 404

    data = resp.json()
    result = {
        'word': data[0].get('word'),
        'phonetic': data[0].get('phonetic'),
        'origin': data[0].get('origin'),
        'meanings': [
            {
                'partOfSpeech': m.get('partOfSpeech'),
                'definitions': [
                    {
                        'definition': d.get('definition'),
                        'example': d.get('example')
                    } for d in m.get('definitions', [])
                ]
            } for m in data[0].get('meanings', [])
        ]
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081) 