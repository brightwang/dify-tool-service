from flask import Flask, request, send_from_directory, jsonify

import os
import markdown
import time
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)

# 配置文件夹路径
UPLOAD_FOLDER = './markdown-quiz-files'
OUTPUT_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

# 确保文件夹存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/upload_markdown', methods=['POST'])
def upload_markdown():
    content = request.get_data(as_text=True)
    print(content)
    if content is None:
        return jsonify({"error": "Invalid input"}), 400
    """Render quiz in Markdown format to HTML."""
    extensions = [
        "tables", "app.extensions.checkbox", "app.extensions.radio",
        "app.extensions.textbox"
    ]
    html = markdown.markdown(content,
                             extensions=extensions,
                             output_format="html5")
    env = Environment(loader=PackageLoader('app', 'static'),
                      autoescape=select_autoescape(['html', 'xml']))
    javascript = env.get_template('app.js').render()
    test_html = env.get_template('base.html').render(content=html,
                                                     javascript=javascript)
    test_html = env.get_template('wrapper.html').render(content=test_html)
    filename = str(int(time.time()))
    with open(os.path.join(OUTPUT_FOLDER, f"{filename}.html"),
              "w+",
              encoding='utf-8') as f:  # create final file
        f.write(test_html)

    return jsonify(
        {"message":
         f"保存成功\n查看链接http://127.0.0.1:5006/get_html/{filename}"}), 200


@app.route('/get_html/<filename>', methods=['GET'])
def get_html(filename):
    if not filename.endswith('.html'):
        filename += '.html'

    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True, port=5006, host='0.0.0.0')
