import numpy as np
import matplotlib.pyplot as plt

class Rays:
    def __init__(self, y, angle):
        self.y = y
        self.tan_angle = np.tan(angle)  # in radian
        self.origin = np.mat([[self.y],[self.tan_angle]])
        self.M = np.mat([[0, 0], [0, 0]])
        self.output = self.origin
        self.z = 0
        self.out_of_range = False
    # Free-space Propagation
    def propagate(self, dist):
        """
        dist: propagation distance (z)
        """
        start_y = self.y
        start_z = self.z

        self.z = self.z + dist
        self.M = np.mat([[1, dist], [0, 1]])
        self.output = self.M * self.output
        self.y = self.output[0].item()
        # return starting point of propagation
        return start_y, start_z

    # Refraction at a planar boundary
    def refract_plane_bound(self, n1, n2):
        """
        -params n1: refractive index of original media
        -params n2: refractive index of entering media
        """
        bottom_right  = n1 / n2
        self.M = np.mat([[1, 0], [0, bottom_right]])
        self.output = self.M * self.output

    # Refraction at a spherical boundary
    def refract_sph_bound(self, n1, n2, R):
        """
        -params n1: refractive index of original media
        -params n2: refractive index of entering media
        -params R: radius of spherical boundary
        """
        bottom_right = n1 / n2
        bottom_left = -(n2-n1)/(n2*R)
        self.M = np.mat([[1, 0], [bottom_left, bottom_right]])
        self.output = self.M * self.output

    # Transmission through a thin lens
    def lens(self, l_f, l_s):
        """
        -params l_f: focal length of thin lens
        -params l_s: size of thin lens(diameter)
        """
        bottom_left  = -1/l_f
        self.M = np.mat([[1, 0], [bottom_left, 1]])
        
        if abs(self.output[0]) <= l_s/2 + 1:
            self.output = self.M * self.output
        else:       
            self.out_of_range = True
    
    # Return original position and angle
    def origin_pos_angle(self):
        return self.origin
    
    # Return current position and angle
    def pos_angle(self):
        return self.output

