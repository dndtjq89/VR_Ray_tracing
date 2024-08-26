import matplotlib.pyplot as plt
import numpy as np
from Ray import Rays
from Display import Displays

class Simul:
    def __init__(self, ray_bundles, dist_set, lens_size_set, lens_focal_length_set, R_n):
        self.ray_bundles = ray_bundles
        self.dist_set = dist_set # propagation distance set
        self.L_s_set = lens_size_set
        self.L_f_set = lens_focal_length_set 
        self.R_n = R_n # number of rays from each point source
        
        try:
            if len(self.dist_set) != len(self.L_f_set) + 1:
                raise
        except:
            print("Number of propagation distance should be set to (number of lens + 1)")
            quit()
        try:
            if len(self.L_s_set) != len(self.L_f_set):
                raise
        except:
            print("Number of lens size set and focal length set must be equal")
            quit()

    def plot_rays(self, start_y, start_z, ray, plot_color):
        """
        Plot and visualize loss graph in real-time 

        -params start_y : propagation starting point(y)
        -params start_z : propagation starting point(z)
        """
        plt.plot([start_z, ray.z], [start_y, ray.y],  color = plot_color)

        plt.xlabel('Propagation axis(z)')
        plt.ylabel('Position(y)')
        plt.title('Ray Tracing result')
        plt.grid(True)
    
    def plot_components(self, z, min_y, max_y):
        plt.vlines(z, min_y, max_y, colors='black', linewidth=3)

    def run(self):
        idx = 0
        cmap = plt.get_cmap('viridis')
        for dist in self.dist_set:
            ray_idx = 0
            min_y = 0; max_y = 0;  z = 0
            for ray in self.ray_bundles:
                # color by point source
                plot_color = cmap(ray_idx//self.R_n * 40)
                ray_idx = ray_idx + 1

                # starting point at each propagation
                start_y, start_z = ray.propagate(dist)
                
                # Plot rays only the rays propagate within the components
                if ray.out_of_range == False:
                    self.plot_rays(start_y, start_z, ray, plot_color)

                    # parameters to plot optical components
                    z = start_z
                    if start_y > max_y:
                        max_y = start_y
                    if start_y < min_y:
                        min_y = start_y

                # Multiply n-th lens matrix
                if idx < len(self.L_f_set):
                    ray.lens(self.L_f_set[idx], self.L_s_set[idx])

            # parameters in case of light rays is entering components partially
            if idx != 0:
                if max_y-min_y < self.L_s_set[idx - 1]:
                    print(len(self.L_s_set))
                    min_y = -self.L_s_set[idx - 1]/2 
                    max_y = self.L_s_set[idx - 1]/2

            # plot optical components
            self.plot_components(z, min_y, max_y)
            
            z = z + dist
            idx = idx + 1
        plt.show()
            
                


        

