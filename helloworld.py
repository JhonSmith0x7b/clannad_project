#-*- coding:utf-8 -*-
from flask import Flask, url_for, render_template, g, request, send_from_directory, current_app
import sys;reload(sys);sys.setdefaultencoding('utf-8')
from clannad_novel import clannad_novel
from tieba_search import tieba_search
from get_sen.index import get_sen
import os
app = Flask(__name__)
app.debug = True
app.register_blueprint(get_sen)



@app.route('/favicon.ico', methods = ['get'])
def icon():
	return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/clannadnovel', methods = ['get', 'post'])
@app.route('/', methods = ['get', 'post'])
def hello():
	return clannad_novel.hello()


@app.route('/tiebasearch')
def tiebasearch():
	return tieba_search.tieba_search()

@app.route('/tiebasearch/query', methods = ['post'])
def tieba_search_query():
	return tieba_search.query()

@app.route('/tiebasearch/r', methods=['post'])
def r():
	return tieba_search.r()

if __name__ == '__main__':
	app.run(host = '0.0.0.0', threaded=False, port = 12300)