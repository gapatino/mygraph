# mygraph
Python functions to format figures

Requires that matplotlib.pyplot had been imported from the program importing these functions
Both functions will require pyplot to be the first positional argument when called

**settingup_figs()** sets the default value for the figures. pyplot and seaborn must be passed as arguments.

**mygraph()** is used to format each figure being produced. pyplot is the first positional input and is the only required.
Other inputs are optional and include labels and limits for each axis, whether to display (default is yes) and location
of the legend, and title for the figure.
