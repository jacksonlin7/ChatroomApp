from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html', ip=request.remote_addr)

@app.route('/fetch')
def fetch():
    return messages

@app.route('/send', methods=["POST"])
def send():
    msg = request.form.get('msg')
    msg = msg if len(msg) < 50 else None
    if msg:
        messages.append(f"{request.remote_addr}: {msg}")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run("172.16.172.218", 3000, debug=True)