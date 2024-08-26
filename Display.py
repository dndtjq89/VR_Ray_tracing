import numpy as np
from Ray import Rays

class Displays:
    def __init__(self, d_s, r_n, p_n):
        """
        -params d_s: size of displays
        -params r_n: number of Rays (should be odd to show center light ray)
        -params p_n: number of simulated point light source in displays
        """
        self.d_s = d_s
        self.r_n = r_n
        self.p_n = p_n
        self.ray_bundles = [None] * r_n * p_n
        try:
            if is_even(r_n):
                raise
        except:
            print("Number of Rays should be odd")
            quit()
        try:
            if is_even(p_n):
                raise
        except:
            print("Number of point source in display should be odd")
            quit()

    def run(self, l_s, d_l_dist):
        """
        -params l_s: first lens size(diameters)
        -params d_l_dist : display to lens distance
        """
        for idx_p in range(self.p_n):
            for idx_r in range(self.r_n):
                # parameters of point source at display position(z=0 plane)
                p_pitch = self.d_s / (self.p_n - 1) # pitch
                p_pos = p_pitch*idx_p - self.d_s/2  # position(y)
               
                # parameters of ray angle
                top_angle = np.arctan((l_s/2-p_pos)/d_l_dist) # in radian
                bottom_angle = np.arctan((-l_s/2-p_pos)/d_l_dist) # in radian
                angle_pitch = (top_angle - bottom_angle)/(self.r_n - 1)
                r_angle = angle_pitch * idx_r + bottom_angle

                # Create rays at each point source
                index = idx_p * self.r_n + idx_r
                self.ray_bundles[index] = Rays(p_pos, r_angle)

    def output(self):
        return self.ray_bundles

def is_even(integer):
    return integer % 2 == 0
    
    