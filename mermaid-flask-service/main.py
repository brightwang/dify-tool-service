from flask import Flask, request, send_from_directory
import time
import subprocess

app = Flask(__name__)


# 上传接口
@app.route('/upload', methods=['POST'])
def upload_markdown():
    content = request.get_data(as_text=True)
    time_name = str(int(time.time()))
    file_name = time_name + ".md"
    # 防止格式不对
    if '```mermaid' not in content:
        content = '```mermaid\n' + content + '\n```'
    with open(f"data/{file_name}", 'w', encoding='utf-8') as f:
        f.write(content)
    result = subprocess.run([
        'mmdc', '-p', 'puppeteer-config.json', '-c', 'config.json', '-i',
        f'./data/{file_name}'
    ])
    print(result.stdout)
    return f'Markdown 文件已保存\n预览链接: http://127.0.0.1:5002/svg/{file_name}-1.svg'


# 获取svg接口
@app.route('/svg/<filename>', methods=['GET'])
def get_svg(filename):
    return send_from_directory("/app/data", filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
