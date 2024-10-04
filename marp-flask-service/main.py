from flask import Flask, request
import time

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_markdown():
    content = request.get_data(as_text=True)
    file_name = str(int(time.time())) + ".md"
    with open(f"data/{file_name}", 'w', encoding='utf-8') as f:
        f.write(content)
    return f'Markdown 文件已保存\n预览链接: http://127.0.0.1:5005/{file_name} \n下载链接: http://127.0.0.1:5005/{file_name}?pptx'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
