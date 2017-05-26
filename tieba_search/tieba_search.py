#-*- coding:utf-8 -*-
from flask import Flask, url_for, render_template, g, request, current_app
import sqlite3, json
def tieba_search():
	return render_template('tieba_search/tiebasearch.htm'), 200, 
	{'Content-Type': 'text/html;charset=utf-8'}
	pass

def query():
	if(request.form['date'] == 'all'):
		cur = get_tieba_db().cursor().execute('select * from tiebadata_table where author = ?', (str(request.form['author']).encode('gbk'),))
	else:
		cur = get_tieba_db().cursor().execute('select * from tiebadata_table where author = ? and datetime(date) > ? and datetime(date) < ?', (str(request.form['author']).encode('gbk'), request.form['date'], str(int(request.form['date']) + 1)))
	result = cur.fetchall()
	return json.dumps(result, ensure_ascii = False), 200, {'Content-Type':'text/json;charset=gbk'}
	pass

def get_tieba_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect('%s/static/db/tiebadata_db.db' %current_app.root_path)
		db.text_factory = str
	return db