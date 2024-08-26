### Import modules
import numpy as np
import matplotlib.pyplot as plt

### Import my modules
from config import configs
from Ray import Rays
from Display import Displays
from Simulation import Simul

### Main folder path
root_path = '/home/woongseob/Pytorch_code/Ray_Tracing/'

### Load parameters
D_s, L_s_set, L_f_set, R_n, P_n, Dist_set = configs.load_params(root_path)

# Example usage
if __name__ == "__main__":
    my_display = Displays(D_s, R_n, P_n)
    my_display.run(L_s_set[0], Dist_set[0])

    ray_bundles = my_display.output()
    ray_trace = Simul(ray_bundles,Dist_set, L_s_set, L_f_set, R_n)
    ray_trace.run()
    
   
    