import os
import sys
import time
import shutil

# Create the module file..
filename = str(input('File-Name (mymod.py, name.py, myModule.py, ext.): '))

if '.py' in filename:

	print(' ')
else:
	print('adding .py extension..')
	filename = str(filename+'.py')

# Build the module code..
xfile = open(filename, 'w')
xfile.write('import os'+'\n')
xfile.write('import sys'+'\n')
xfile.write('\n')
xfile.write('def sayHello():'+'\n')
xfile.write('	print("Hello World!")'+'\n')
xfile.close()

# Format the module without the .py extension, for importing..
modname = str(filename.replace('.py',''))

# Render the module usable for importing within the script..
# You can rename 'moddata' to whatever you want the module to be..
moddata = __import__(modname)

# Use the module..
moddata.sayHello()

time.sleep(5)

# Auto-Remove all __pycache__ data..
shutil.rmtree('__pycache__')


