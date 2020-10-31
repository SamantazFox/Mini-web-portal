#!/usr/bin/python

import os, shutil, json


#
# Functions for HTML segments
#

def genHeader(title):
	return (
		'<!DOCTYPE html>\n'
		'<html>\n'
		'\t<head>\n'
		'\t\t<title>{0}</title>\n'
		'\t\t<link rel="stylesheet" type="text/css" href="/static/css/normalize_v8.0.1.css">\n'
		'\t\t<link rel="stylesheet" type="text/css" href="/static/css/style.css">\n'
		'\t</head>\n'
		.format(title)
	)

def genFooter():
	return (
		'\t</body>\n'
		'</html>\n'
	)


def beginTable(welcome_text):
	return (
		'\t<body>\n'
		'\t\t<div class="content-container">\n'
		'\t\t\t<h1>{0}</h1>\n'
		'\t\t\t<table>\n'
		.format(welcome_text)
	)

def endTable():
	return (
		'\t\t\t</table>\n'
		'\t\t</div>\n'
	)


def beginCategory(name):
	return (
		'\t\t\t\t<tr><td><fieldset>\n'
		'\t\t\t\t\t<legend>{}</legend>\n'
		'\t\t\t\t\t<div class="button-container">\n'
		.format(name)
	)

def endCategory():
	return (
		'\t\t\t\t\t\t</div>\n'
		'\t\t\t\t</fieldset></td></tr>\n'
	)


#
# Main routine - Generate index.html
#

# Load JSON config
jsonImport = json.load(open('config.json', 'r'))

# Beginning of page
strbuffer  =  genHeader(jsonImport['Title'] )
strbuffer += beginTable(jsonImport['Banner'])

# Generate HTML for each category
for category in jsonImport['Categories']:

	name    = category['Name']
	content = category['Content']

	strbuffer += beginCategory(name)

	for item in content:

		if item['Image'] == "" or item['Image'] == None:
			image = 'no-image.png'
		else:
			image = item['Image']

		strbuffer += (
			'{tabs}<div class="button">\n'
			'{tabs}\t<a target="_blank" rel="noreferrer" href="{link}" title="{title}">\n'
			'{tabs}\t\t<div class="button-content">\n'
			'{tabs}\t\t\t<img class="button-image" src="/static/img/{img}" />\n'
			'{tabs}\t\t\t<p>{name}</p>\n'
			'{tabs}\t\t</div>\n'
			'{tabs}\t</a>\n'
			'{tabs}</div>\n'
			.format(
				tabs  = '\t\t\t\t\t\t',
				link  = item['Url'],
				title = item['Comment'],
				name  = item['Name'],
				img   = image
			)
		)

	strbuffer += endCategory()

# End of HTML
strbuffer += endTable()
strbuffer += genFooter()

# (Re)create output dir if needed
if os.path.exists('_build'): shutil.rmtree('_build')
os.mkdir('_build')

# Write HTML
with open("_build/index.html", 'w') as fd:
	fd.write(strbuffer)


#
# Main routine - Manage assets
#

# Create _build/static and subdirectories
os.mkdir('_build/static')
os.mkdir('_build/static/css')

# Copy CSS stylesheets
shutil.copy('style.css', '_build/static/css')
shutil.copy('normalize_v8.0.1.css', '_build/static/css')

# Copy icons directory
shutil.copytree('icons', '_build/static/img/')
