#! python3
# backuptozip essentially does tar, but worse
#Then the filename will increment

import zipfile, os

def backupToZip(folder):
# Backup contents of folder to ZIP file
	folder = os.path.abspath('/home/rosalux')
	number =1
	while True:
		zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFileName):
			break
		number = number + 1
	print ('Creating %s...' % (zipFileName))
	backupZip = zipfile.ZipFile(zipFileName, 'w')
	print ('Done.')
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files in %s...' % (foldername))
		# Add the current folder to the ZIP file.
		backupZip.write(foldername)
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue
			backupZip.write(os.path.join(foldername, filename))
	
	backupZip.close()
	print('Done.')

backupToZip('/home/rosalux/Pictures')

