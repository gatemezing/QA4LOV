#!flask/bin/python
import sys
import subprocess
from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

# list in JSON
vocabs = [
    {
        'uri': 'http://www.w3c.org/ns/dcat',
        'title': u'DCAT',
        'description': u'DCAT vocabulary', 
        'namespace': 'http://www.w3c.org/ns/dcat#'
    },
    {
        'uri': 'http://purl.org/vocommons/voaf',
        'title': u'VOAF',
        'description': u'VOAF vocabulary', 
        'namespace': 'http://purl.org/vocommons/voaf#'
    }
]

@app.route('/test/api/v1.0/vocabs', methods=['GET'])
def get_vocabs():
    return jsonify({'vocabs': vocabs})

@app.route('/')
def form():
    #return 'index page!'
    return render_template('form_submit.html')


@app.route('/qa4lov', methods=['POST'])
def qa4lov():
    #print("I got it!")
    query = request.form['query']
    #sys.argv = ['/Users/gatemezing/Documents/lov/main.py','query']
    #result = execfile('/Users/gatemezing/Documents/lov/main.py')
    
    try:
        #result = subprocess.call("python main.py query", shell=True)
        #arg_param = ['query']
        lov_cmd = 'python main.py' + ' '+query
        result = subprocess.check_output(lov_cmd, shell=True)
        #print query
        print result
    
    except subprocess.CalledProcessError as e:
        return_code = e.returncode

    #print result
    return render_template('form_action.html', query=query, result=result)
    
    #res = subprocess.check_output(lcmd, stderr=subprocess.STDOUT)

# Use a list of args instead of a string
#input_files = ['file1', 'file2', 'file3']
#my_cmd = ['cat'] + input_files
#with open('myfile', "w") as outfile:
#    subprocess.call(my_cmd, stdout=outfile)

if __name__ == '__main__':
    app.run(debug=True)