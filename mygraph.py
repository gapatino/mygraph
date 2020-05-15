''' Functions to format figures

Requires that matplotlib.pyplot has been imported
and passed as argument when both functions are called

Run settingup_figs() before making any figures
to set default values

Run mygraph() for each figure'''

def settingup_figs(plt):
    '''Set default values for figures
    Requires pyplot as input'''
    plt.rcParams['axes.labelsize']=18
    plt.rcParams['axes.labelweight']='bold'
    plt.rcParams['axes.titlesize']=22
    plt.rcParams['axes.titleweight']='bold'
    plt.rcParams['lines.linewidth']=2
    plt.rcParams['lines.markersize']=7
    plt.rcParams['xtick.labelsize']=14
    plt.rcParams['ytick.labelsize']=14
    plt.rcParams['legend.fontsize']=16
    plt.rcParams['figure.figsize']=(8,8)

def mygraph(plt,
            xlabel='X axis', xlim=None,
            ylabel='Y axis', ylim=None,
            legend=True, loc='best',
            title=None):
    '''Adds formatted labels, legend and title
    Requires pyplot as input'''
    import matplotlib.pyplot as plt
    plt.xlabel('\n'+xlabel)
    plt.ylabel(ylabel+'\n')
    plt.xticks(fontweight='normal')
    plt.yticks(fontweight='normal')
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    if legend:
        plt.legend(loc=loc)
    if title:
        plt.title(title)
