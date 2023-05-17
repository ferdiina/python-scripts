from flask import Flask, render_template, request
app = Flask(__name__)
LOG_FILE_PATH = 'logfile.txt'

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def read_log_files():
    files = []
    with open(LOG_FILE_PATH, 'r') as file:
        for line in file:
            name, path = line.strip().split(',')
            files.append({
                'name': name,
                'path': path
            })
    return files

@app.route('/', methods=['GET', 'POST'])
def display_log():
    selected_file = request.args.get('file')
    if selected_file is None:
        selected_file = read_log_files()[0]['path']

    log_content = read_file_content(selected_file)
    source_files = read_log_files()

    return render_template('log.html', log_content=log_content, source_files=source_files, selected_file=selected_file)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
