#-*- coding:utf-8 -*-
from flask import Flask, request, render_template, send_from_directory, Blueprint, current_app
import sqlite3,json, os

get_sen =  Blueprint('get_sen' , __name__)

@get_sen.route('/get_sen', methods=['post', 'get'])
def hello():
	main = False
	try:
		main = get_random_sentence()
	except Exception, e:
		print str(e)
		pass
	if not main:
		main = {
		'content': '如果想认识某人的话，就要先知道那人反感什么.',
		'author': '富坚义博',
		'anime': '全职猎人'
		}
	html = """
	<!DOCTYPE html>
<html>
<head>
	<title>SEN PROJECT</title>
	<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
</head>
<body>
	<div id="content">
		
	</div>
</body>
</html>
<script type="text/javascript">
	window.onload = function(){
		data = JSON.parse('""" + json.dumps(main).replace('\\r', '\\\\r\\\\n') + """')
		content = '<p class="content">' + data.content + '</p><br>'
		+ '<p class="author">-- ' + data.author + '</p><br>'
		+ '<p class="anime">「' + data.anime + '」</p><br>'
		$('#content').html(content)
	}
</script>
<style type="text/css">
	@font-face {
		font-family: 'me_font';
	    src: url('get_sen/font/fzbiaoysk_ccpc-webfont.woff2') format('woff2'),
	         url('get_sen/font/fzbiaoysk_ccpc-webfont.woff') format('woff');
	    font-weight: normal;
	    font-style: normal;
	}
	body{
		font-size: 18px;
		font-family: 'me_font';
	}
	#content{
		text-align: center;
		margin-top: 100px;
	}
	.content{

	}
	.content:before{
		content: open-quote;
		font-size: 24pt;
		text-align: center;
		line-height: 42px;
		color: #fff;
		background: #ddd;
		top: 30px;
		border-radius: 25px;

		/** define it as a block element **/
		height: 25px;
		width: 25px;
	}
	.content:after{
		content: close-quote;
		font-size: 24pt;
		text-align: center;
		line-height: 42px;
		color: #fff;
		background: #ddd;
		bottom: 40px;
		border-radius: 25px;

		/** define it as a block element **/
		height: 25px;
		width: 25px;
	}
	.author{
		text-align: right;
		margin-right: 30%;
	}
</style>
	"""
	return html, 
	200, {'Content-Type': 'text/html;charset=utf-8'}

@get_sen.route('/get_sen/font/<path:path>')
def send_font(path):
	return send_from_directory('get_sen/font', path)

def get_random_sentence():
	db = sqlite3.connect(os.path.join(current_app.root_path, 'get_sen/static/juzimi_db.db'))
	sql = """
	select * from juzimi_table order by random() limit 1
	"""
	cursor = db.cursor()
	result = cursor.execute(sql).fetchall()
	main = {}
	if result[0] != '':
		main['content'] = result[0][0]
		main['author'] = result[0][1]
		main['anime'] = result[0][3]
	return main
	pass

