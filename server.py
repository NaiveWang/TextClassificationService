from flask import Flask, request, render_template
import client
import json
import ast
app = Flask(__name__)
@app.route('/headless', methods=['POST'])
def infer_json():
    return client.infer(json.dumps(request.json, ensure_ascii=False))
@app.route('/', methods=['GET'])
def root():
    # show the main page
    return render_template('root.html', results=[], text='')

@app.route('/', methods=['POST'])
def infer():
    # return a result list
    if 'squash' in request.form:
        raw=request.form['raw'].replace('\n', '').replace('\r', '')
        return render_template('root.html', results=[], text=raw)
    
    elif 'infer' in request.form:
        raw = request.form['raw']
        rawl=raw.split('\n')
        jtext=''
        for line in rawl:
            jtext+=json.dumps({
                    'doc_token': list(line)
                'doc_token': list(line),
                'doc_keyword': [],
                'doc_topic': []
            }, ensure_ascii=False)
            jtext+='\n'
        #print(jtext)
        results = client.infer(jtext[:-1])
        #print(results)
        return render_template('root.html', results=ast.literal_eval(results), text=raw)
if __name__ == "__main__":
    app.run(debug=False)
