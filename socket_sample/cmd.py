__author__ = 'Admin'

import subprocess
import sys
cmd= sys.argv[1]
p= subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
(output,err) = p.communicate()
p_status = p.wait()
print output
print p_status