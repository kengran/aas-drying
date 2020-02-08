
import sys
sys.path.append('/Users/hty/Google Drive/research/APS exp/chi_files')
import noNano_ctrl as nnc
import nano_ctrl as nc
from matplotlib.pyplot import *
from numpy import *

reload(nnc)
reload(nc)

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

close("all")

f, ax = subplots()

which_peak = 'Ca-T'

# not normalized
# ax.semilogx(
#     array(nnc.x_value(nnc.read_file_with_low_angle_info)),
#     nnc.CaSi(),
#     'o-', label='No nano')
# ax.semilogx(
#     array(nc.x_value(nc.read_file_with_low_angle_info)),
#     nc.CaSi(),
#     '^-', label='Nano-ZrO$_2$')

# normalized
ax.semilogx(
    array(nnc.x_value(nnc.read_file_with_low_angle_info)),
    nnc.norm_peak(which_peak, nnc.read_file_with_low_angle_info),
    'o-', label='No nano')
ax.semilogx(
    array(nc.x_value(nc.read_file_with_low_angle_info)),
    nc.norm_peak(which_peak, nc.read_file_with_low_angle_info),
    '^-', label='Nano-ZrO$_2$')


legend(loc = 4, fontsize ='small')
xlabel('Time (hours)')
ylabel('%s/T-O'%(which_peak))
# xlim(10,500)
subplots_adjust(bottom=0.13)
f.show()

#   f.savefig('/Users/hty/desktop/Ca-T ctrl comp %s %s.pdf'%(nnc.__name__, nc.__name__))
