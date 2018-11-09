from flask import Flask, request, render_template
app = Flask(__name__, static_url_path='')

@app.route('/upload')
def hello_world():
   return 'Hello World'

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/upload', methods = ['POST'])
def upload_file():
	f = request.files['file']
	


if __name__ == '__main__':
   app.run()
