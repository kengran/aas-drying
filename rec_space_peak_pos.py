import sys
sys.path.append('/Users/hty/Google Drive/python_modules')
import getData as gd
from numpy import *
from matplotlib.pyplot import *
sys.path.append('/Users/hty/Google Drive/research/APS exp/py_files')
import peak_assign as pn
# import target file
import noNano_rh0 as target


data_file = target.read_reciprocal_space_files('.sq')[1]

xy = gd.curve(data_file,141)

close("all")

# remember to update the range of the label****
[plot(xy[i][0],xy[i][1],label='%s h'%(target.read_reciprocal_space_files('.sq')[3] [i])) for i in range (shape(xy)[0])]
legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
xlabel(r'r ($\AA^{-1}$)')
ylabel('S(Q)')

show()

local_max = pn.find_local_max(xy)[0]

peak_pos = [xy[i][0][local_max[i][0]] for i in range(shape(xy)[0])]
