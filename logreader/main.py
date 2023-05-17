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


def read_file_generator(file_path, start_line, end_line):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= start_line and i < end_line:
                yield line.rstrip()
            elif i >= end_line:
                break


@app.route('/', methods=['GET', 'POST'])
def display_log():
    selected_file = request.form.get('file')
    if selected_file is None:
        selected_file = SOURCE_FILES[0]['path']

    if request.method == 'POST':
        page = int(request.form.get('page', 1))
        start_line = (page - 1) * PAGE_SIZE
        end_line = start_line + PAGE_SIZE
    else:
        page = 1
        start_line = 0
        end_line = PAGE_SIZE

    lines = read_file_generator(selected_file, start_line, end_line)
    total_lines = sum(1 for _ in open(selected_file))

    return render_template('log.html', lines=lines, page=page, total_lines=total_lines, source_files=SOURCE_FILES, selected_file=selected_file)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
