
from matplotlib.pyplot import *
from matplotlib import gridspec

# #change font properties of the plots
# font = {'family' : 'serif',
#         'weight' : 'normal',
#         'size'   : 17}
# matplotlib.rc('font', **font)

# # set style of the plot
# style.use('classic')

close("all")
gs = gridspec.GridSpec(2, 2,
                       height_ratios=[2,1]
                       )
f = figure(figsize=(15,8))

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)


'''ctrl sample'''
import plot_PDF_ctrl_diff as ctrl
reload(ctrl)
ctrl.difference_plot(gs[1], gs[3], '(b) Control')

'''dry sample'''
import plot_PDF_dry_diff as dry
reload(dry)
system_name = dry.difference_plot(gs[0], gs[2], '(a) 0% RH')

f.show()


#f.savefig('/Users/hty/desktop/ pdf 2col %s.pdf'%(system_name),
#          transparent=True
##          ,dpi = 600
#          )
