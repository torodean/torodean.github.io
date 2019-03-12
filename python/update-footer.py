##################################################################################
## Program: update-nav-bar.py
## Author: Antonius Torode
## Date: 3/11/2019
## Purpose: To update the navbar in multiple html documents based on a template.
##################################################################################



filenames = ['index', 'projects', 'MIA', 'blog', 'AHandbook', 'ACookbook', 'blog/blog-template', 'D3F']
templatefilename = 'footer'
templatefilenameblue = 'footer-blue'
print('...')
print('...Template File as {0}.html'.format(templatefilename))
print('...')

with open('{0}.html'.format(templatefilename), 'r') as templatefile:
	templatetext=templatefile.read()
	
with open('{0}.html'.format(templatefilenameblue), 'r') as templatefileblue:
	templatetextblue=templatefileblue.read()
	
print('...')
print('...Printing Template Text.')
print('...')
print(templatetext)

print('...')
print('...Printing Template Text - variant.')
print('...')
print(templatetext)

print('...')

for filename in filenames:
	p1 = True
	p2 = False
	p3 = False
	p4 = False
	print('...')
	print('...Processing file: {0}.html'.format(filename))
	print('...')
	file = open('../{0}.html'.format(filename),'r')
	filelines = file.readlines()
	file.close()
	file = open('../{0}.html'.format(filename),'w')
	for fileline in filelines:
		if p1:
			file.write(fileline)
		if p3:
			if '<!-- ============== END FOOTER - PYTHON ENCODED =============== -->' in fileline:
				p3 = False
				p4 = True
		if p2:
			if filename != 'projects':
				file.write(templatetext)
			else:
				file.write(templatetextblue)
			p2 = False
			p3 = True
		if p4:
			file.write(fileline)
		if '<!-- ============== BEGIN FOOTER - PYTHON ENCODED =============== -->' in fileline:
			p1 = False
			p2 = True	
	
print('...')
print('...Program Finished')