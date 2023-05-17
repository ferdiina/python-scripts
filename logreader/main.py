from flask import Flask, render_template, request

app = Flask(__name__)

SOURCE_FILES = [
    {
        'name': 'Tomcat-8080',
        'path': '/opt/tomcat/8080/logs/catalina.out',
    },
    {
        'name': 'Elasticsearch',
        'path': '/data/elasticsearch/logs/elasticsearch.log',
    },
    # Add more source files here
]

PAGE_SIZE = 1000


def read_file_lines(file_path, start_line, end_line):
    lines = []
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= start_line and i < end_line:
                lines.append(line.rstrip())
            elif i >= end_line:
                break
    return lines


@app.route('/', methods=['GET', 'POST'])
def display_log():
    selected_file = request.form.get('file')
    if selected_file is None:
        selected_file = SOURCE_FILES[0]['path']

    lines = read_file_lines(selected_file, 0, PAGE_SIZE)
    total_lines = sum(1 for _ in open(selected_file))

    return render_template('log.html', lines=lines, total_lines=total_lines, source_files=SOURCE_FILES, selected_file=selected_file)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
