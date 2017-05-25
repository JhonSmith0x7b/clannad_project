#-*- coding:utf-8 -*-
from flask import Flask, url_for, render_template, g, request, send_from_directory, current_app
import sys;reload(sys);sys.setdefaultencoding('utf-8')
from clannad_novel import clannad_novel
app = Flask(__name__)
app.debug = True



@app.route('/favicon.ico', methods = ['get'])
def icon():
	return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/clannadnovel', methods = ['get', 'post'])
@app.route('/', methods = ['get', 'post'])
def hello():
	return clannad_novel.hello()

if __name__ == '__main__':
	app.run(host = '0.0.0.0', threaded=False, port = 12300)