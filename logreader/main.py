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
def read_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


@app.route('/', methods=['GET', 'POST'])
def display_log():
    selected_file = request.args.get('file')
    if selected_file is None:
        selected_file = SOURCE_FILES[0]['path']

    log_content = read_file_content(selected_file)

    return render_template('log.html', log_content=log_content, source_files=SOURCE_FILES, selected_file=selected_file)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
