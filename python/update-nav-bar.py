##################################################################################
## Program: update-nav-bar.py
## Author: Antonius Torode
## Date: 3/11/2019
## Purpose: To update the navbar in multiple html documents based on a template.
##################################################################################



filenames = ['index', 'projects', 'MIA', 'blog', 'AHandbook', 'ACookbook', 'blog/blog-template', 'D3F', 'sermonettes']
templatefilename = 'main-nav-bar'
print('...')
print('...Template File as {0}.html'.format(templatefilename))
print('...')

with open('{0}.html'.format(templatefilename), 'r') as templatefile:
	templatetext=templatefile.read()
	
print('...')
print('...Printing Template Text.')
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
			if '<!-- End of main navigation bar - PYTHON ENCODED -->' in fileline:
				p3 = False
				p4 = True
		if p2:
			file.write(templatetext)
			p2 = False
			p3 = True
		if p4:
			file.write(fileline)
		if '<!-- Main navigation bar - PYTHON ENCODED -->' in fileline:
			p1 = False
			p2 = True	
	
print('...')
print('...Program Finished')
