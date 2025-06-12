from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/termos')
def termos():
    return send_from_directory('.', 'termos.html')

@app.route('/privacidade')
def privacidade():
    return send_from_directory('.', 'privacidade.html')

@app.route('/logo.png')
def logo():
    return send_from_directory('.', 'logo.png')

if __name__ == '__main__':
    app.run()
