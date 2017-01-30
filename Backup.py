#!/usr/bin/python

import os
import time

source = ['/opt/mk/']
dest_dir = '/home/bkup/'

today = dest_dir + time.strftime('%Y%m%d%H%M%S')
now = time.strftime('%Y%m%d%H%M%S')

if not os.path.exists(today):
        os.mkdir(today)
target = today + os.sep + now + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'backup done'
else:
    print 'backup not done'
