#!/usr/bin/env python

# Script to analyze revenue in various auctions

import subprocess
import numpy as np

data = np.empty((0,2), float)

for r in range(0,210,10):
    cmd = ('python auction.py --perms=1 --seed=2 --iters=20 --reserve='+str(r)+' Klczbb,4 Truthful,1').split()
    out, err = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()
    rev = map(float,(out.split()[-2:-1]))
    row = np.array([.1 * r] + rev) # get reserve, std-dev
    data = np.vstack((data, row))
    print data



#f = open("gsp.csv", 'a')
#np.savetxt(f, np.array([ns, avg_degrees, avg_time]))
#f.close()
