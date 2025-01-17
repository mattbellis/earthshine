import pyhepmc

import numpy as np

import sys

from scipy.spatial.transform import Rotation as R


################################################################################

def rotation_matrix_from_vectors(vec1, vec2):
    """Find the rotation matrix that aligns vec1 to vec2."""

    # Normalize the vectors
    vec1 = vec1 / np.linalg.norm(vec1)
    vec2 = vec2 / np.linalg.norm(vec2)

    # Find the axis of rotation
    axis = np.cross(vec1, vec2)
    axis_norm = np.linalg.norm(axis)

    # If the vectors are parallel, no rotation is necessary
    if axis_norm == 0:
        return np.eye(3)

    # Find the angle of rotation
    angle = np.arccos(np.dot(vec1, vec2))

    # Construct the rotation matrix
    rot = R.from_rotvec(angle * axis / axis_norm)
    return rot.as_matrix()

# Example usage:
#v1 = np.array([1, 0, 0])
#v2 = np.array([0, 1, 0])
#R = rotation_matrix_from_vectors(v1, v2)
#print(R)
#print(np.matmul(R,v1))
################################################################################


################################################################################

CMS_origin = np.array([0,0,0])
smearing_length = 0.5 # Meter

# The input file is expected to be a .ascii file from the NuHEPMC format
infile_name = sys.argv[1]
outfile_name = None

verbose = False
#verbose = True
DO_ROTATION = True

#MAX_EVENTS = 10
MAX_EVENTS = None

# Define the nominal coordinates. We might smear these later.
interaction_vertex_org = [0, -10, 0]
interaction_vertex_cmd_line = sys.argv[2]
if interaction_vertex_cmd_line is None:
    interaction_vertex_org = [0, -10, 0]
else:
    vals = interaction_vertex_cmd_line.split(',')
    interaction_vertex_org = [float(vals[0]), float(vals[1]), float(vals[2])]
interaction_vertex_org  = np.array(interaction_vertex_org)

print(f"Interaction vertex will be {interaction_vertex_org}\n")

# Do rotation?
rot_mat = None
if DO_ROTATION:
    up = np.array([0, 1, 0])
    new_vec = CMS_origin-interaction_vertex_org
    rot_mat = rotation_matrix_from_vectors(up, new_vec)
    print(f"up:      {up}\n")
    print(f"new vec: {new_vec}\n")
    print(f"rot_mat: {rot_mat}\n")

################################################################################

print(f"Reading in {infile_name}")

if infile_name[-6:] != '.ascii':
    print("Expecting input file to end in .ascii\n")
    print(infile_name)
    print("\nExiting\n")
    exit()

else:
    x,y,z = interaction_vertex_org
    outfile_name = f"{infile_name.split('.ascii')[0]}_vtx_{x}_{y}_{z}.hepmc2"
    outfile_name = f"{outfile_name.replace('hepmc3.','')}"
    print(f"Will write output to {outfile_name}")
    #exit()


# Open the files for input and output
fin =   pyhepmc.open(infile_name)
print("Opened the input file...\n")
fout =  pyhepmc.open(outfile_name, "w", format="hepmc2", precision=6)
print("Opened the output file...\n")


for idx,event in enumerate(fin):
    # Move the vertices of the files
    if idx%1000==0:
        print(f"Processing event {idx}")
    if verbose:
        print(idx)
    # Vertices
    nvertices = len(event.vertices)
    for i,v in enumerate(event.vertices):
        # Smear the points by 1 meter
        dx = interaction_vertex_org[0] + smearing_length*np.random.random()
        dy = interaction_vertex_org[1] + smearing_length*np.random.random()
        dz = interaction_vertex_org[2] + smearing_length*np.random.random()

        # The first and last vertex seem to be "special"? 
        # Don't fully understand
        if i==0 or i==nvertices-1:
            v.position[0] = dx
            v.position[1] = dy
            v.position[2] = dz
        else:
            v.position[0] += dx
            v.position[1] += dy
            v.position[2] += dz
    
        if verbose:
            print(i,v)
    if verbose:
        print("event.vertices: ",event.vertices)
    
    # For now, just swap out the y and z momenta of the particles
    # to represent them traveling upward.
    for i,p in enumerate(event.particles):
        z = p.momentum[2]
        y = p.momentum[1]
    
        p.momentum[1] = z
        p.momentum[2] = y

        pmag = np.linalg.norm(np.array([p.momentum[0], p.momentum[1], p.momentum[2]]))
        if verbose:
            print(f"NO ROTATION: {i} {p} {pmag}")

        if DO_ROTATION:
            x = p.momentum[0]
            y = p.momentum[1]
            z = p.momentum[2]
            v1 = np.array([x,y,z])
            newv1 = np.matmul(rot_mat,v1)
            #print(np.matmul(rot_mat,v1))
            p.momentum[0] = newv1[0]
            p.momentum[1] = newv1[1]
            p.momentum[2] = newv1[2]
            pmag = np.linalg.norm(np.array([p.momentum[0], p.momentum[1], p.momentum[2]]))
        if verbose:
            print(f"   ROTATION: {i} {p} {pmag}")
    if verbose:
        print(event.particles)
    
    fout.write(event)
    
    if MAX_EVENTS is not None and idx>=MAX_EVENTS:
        break

  #print(event)

fout.close()
fin.close()

print("Finished writing")
print("Closed input and output files.")

