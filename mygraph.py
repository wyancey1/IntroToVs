import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,100)
plt.plot(x, np.sin(x))
plt.show()

# A virtual file creates a folder environment that keeps libraries form interfering with each other.

# Three step process
# 1: Create a virtual environment (aka folder) by typing "py -3 -m venv introvenv" into the terminal
# 2: Activate the virtual environment ".\introvenv\Scripts\activate"
# 3: Install 3rd party libraries " pip3 install (library X)"

# Source control is specific code (python)
# Version code can include things like pictures and videos
