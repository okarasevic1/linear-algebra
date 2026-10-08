import numpy as np

def gramm_schmidt_process(basis:np.array):
    
    otrhogonal_basis = []
    v_count = 0

    for vector in basis: 

        current_v = vector

        # append first vector unchanged (k_1)
        if v_count == 0:
            v_count += 1
            otrhogonal_basis.append(current_v)
            continue

        # calculate the projection of the vectors 
        projections = []

        for k_vector in otrhogonal_basis:
            projection = np.dot(current_v, k_vector) / np.dot(k_vector, k_vector)
            projection = projection * np.array(k_vector)
            projections.append(projection) 

        # find the k_vector
        for projection in projections:
            current_v = current_v - np.array(projection)
        
        otrhogonal_basis.append(current_v)
        v_count += 1
    
    otrhogonal_basis = np.array(otrhogonal_basis).T

    return otrhogonal_basis


def gramm_schmidt_orthonormal(orthogonal_b):
    orthonormal_basis = []

    for vector in orthogonal_b.T:
        current_vector = vector

        v_norm = np.linalg.norm(current_vector)
        current_vector = current_vector / v_norm
        orthonormal_basis.append(current_vector)

    orthonormal_basis = np.array(orthonormal_basis).T

    return orthonormal_basis


basis = np.array([[1, 1, 1], [1, 0, 1]])
otrhogonal_basis = gramm_schmidt_process(basis)
orthonormal_basis = gramm_schmidt_orthonormal(otrhogonal_basis)

print('Orthogonal Basis: \n', otrhogonal_basis)
print('Orthonormal Basis: \n', orthonormal_basis)
