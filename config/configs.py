import json
import torch
def load_params(root_path):

    ### Load hardware parameters 
    with open(root_path + 'config/params.json', 'r') as f:
        params = json.load(f)

    D_s = params['display_size']
    L_s_set = params['lens_size_set']
    L_f_set = params['lens_focal_length_set']

    R_n = params['num_Rays']
    p_n = params['num_Point_sources']

    dist_set = params['propagation distance_set']

    return D_s, L_s_set, L_f_set, R_n, p_n, dist_set