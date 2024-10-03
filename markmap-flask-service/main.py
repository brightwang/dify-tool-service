from flask import Flask, request, send_from_directory
import time
import subprocess
import os

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_markdown():
    content = request.get_data(as_text=True)
    time_name = str(int(time.time()))
    file_name = time_name + ".md"
    html_name = time_name + ".html"
    with open(f"data/{file_name}", 'w', encoding='utf-8') as f:
        f.write(content)
    # 转换md为html
    result = subprocess.run(
        ['npx', 'markmap-cli', f'data/{file_name}', '--no-open'],
        capture_output=True,
        text=True)
    return f'Markdown 文件已保存\n预览链接: http://127.0.0.1:5003/html/{html_name}'


@app.route('/html/<filename>', methods=['GET'])
def get_html(filename):
    html_dir = 'data'
    return send_from_directory(html_dir, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
