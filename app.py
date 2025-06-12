from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/termos')
def termos():
    return send_from_directory('.', 'termos.html')

@app.route('/privacidade')
def privacidade():
    return send_from_directory('.', 'privacidade.html')

@app.route('/logo.jpg')
def logo():
    return send_from_directory('.', 'logo.jpg')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run()

