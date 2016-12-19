
import sys
sys.path.append('/Users/hty/Google Drive/research/APS exp/chi_files')
import noNano_ctrl as nnc
import nano_ctrl as nc
from matplotlib.pyplot import *
from numpy import *

close("all")
f, ax = subplots()

# ax.plot(array(nnc.x_value())+24,nnc.CaSi(),'o-', label='no nano')
# ax.plot(array(nc.x_value())+24,nc.CaSi(),'o-', label='nano')

ax.plot(array(nnc.x_value())+24,nnc.peak_casi(),'o-', label='no nano')
ax.plot(array(nc.x_value())+24,nc.peak_casi(),'o-', label='nano')

legend(loc = 0)
xlabel('time, hour')
ylabel('Ca-Si/T-O')
f.show()

#   f.savefig('/Users/hty/desktop/%s.pdf'%('ca-si ctrl compare'))
