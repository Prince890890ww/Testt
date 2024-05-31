from flask import Flask, request
import requests
import time

app = Flask(__name__)

headers_template = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_stickers():
    if request.method == 'POST':
        cookie = request.form.get('cookie')
        thread_id = request.form.get('threadId')
        time_interval = int(request.form.get('time'))

        headers = headers_template.copy()
        headers['Cookie'] = cookie

        api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/messages'

        sticker_urls = [
            "https://example.com/sticker1.png",  # Replace with actual sticker URLs
            "https://example.com/sticker2.png",
            "https://example.com/sticker3.png",
        ]

        while True:
            try:
                for sticker_url in sticker_urls:
                    # Send the sticker
                    sticker_parameters = {'sticker': sticker_url}
                    sticker_response = requests.post(api_url, data=sticker_parameters, headers=headers)
                    if sticker_response.status_code == 200:
                        print(f"Sticker sent: {sticker_url}")
                    else:
                        print(f"Failed to send sticker: {sticker_url}")

                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending sticker: {e}")
                time.sleep(30)

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Devil Brand</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
            }
            .container {
                max-width: 500px;
                background-color: #fff;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                margin: 0 auto;
                margin-top: 20px;
            }
            .header {
                text-align: center;
                padding-bottom: 20px;
            }
            .btn-submit {
                width: 100%;
                margin-top: 10px;
            }
            .footer {
                text-align: center;
                margin-top: 20px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <header class="header mt-4">
            <h1 class="mb-3">𝗥𝗢𝗛𝗜𝗧 𝐁𝐑𝐀𝐍𝐃</h1>
            <p>𝐎𝐅𝐅𝐋𝟏𝐍𝟑 𝐒𝟑𝐑𝐕𝟃𝐑 𝗕𝗬 𝗥𝗢𝗛𝗜𝗧</p>
            <h1 class="mt-3">𝐎𝐖𝐍𝟃𝐑 :: ʀᴏʜɪᴛ ᴀʟᴏɴᴇ</h1>
        </header>

        <div class="container">
            <form action="/" method="post">
                <div class="mb-3">
                    <label for="cookie">Enter Your Cookie:</label>
                    <input type="text" class="form-control" id="cookie" name="cookie" required>
                </div>
                <div class="mb-3">
                    <label for="threadId">Enter Convo/Inbox ID:</label>
                    <input type="text" class="form-control" id="threadId" name="threadId" required>
                </div>
                <div class="mb-3">
                    <label for="time">Speed in Seconds:</label>
                    <input type="number" class="form-control" id="time" name="time" required>
                </div>
                <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
            </form>
        </div>
        <footer class="footer">
            <p>&copy; 2024 ROHITXWD. All Rights Reserved.</p>
            <p>Convo/Inbox Loader Tool</p>
            <p>Made with 𝐑𝐎𝐇𝐈𝐓𝐗𝐖𝐃 by <a href="https://github.com/Rohitxwd">Rohitxwd</a></p>
        </footer>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
