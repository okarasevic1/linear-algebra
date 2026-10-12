import numpy as np

# Proj_u_k(v_n) = (dot(u_k, v_n) / power(norm(u_k), 2)) * u_k
# Another way: Proj_u_k(v_n) = (dot(u_k, v_n) / dot(u_k, u_k)) * u_k
def vector_projection(u, v):
    u_dot_v = np.dot(u, v)
    u_dot_u = np.dot(u, u)
    scalar = u_dot_v / u_dot_u
    proj = scalar * u

    return proj