from __future__ import division
import openbabel as ob
from visual import *
mol_frame= frame()
def set_background_color(r, g, b):
	display.get_selected().background =(r,g,b)
def get_color(atom):
	atomic_num = atom.GetAtomicNum()
	if atomic_num == 1:
		return color.red
	elif atomic_num ==6:
		return color.green
	elif atomic_num == 7:
		return color.green
	elif atomic_num == 8:
		return color.blue
	else:
		return color.purple

def display_atoms(mol):
	ob_mol = mol.OBMol
	for atom in ob.OBMolAtomIter(ob_mol):
		atom_pos = get_coords(atom)
		atom_color = get_atom_color(atom)
		atom_radius = 0.5*ob.OBElementTable().GetCovalentRad(atom.GetAtomicNum())
		sphere(frame = mol_frame, pos = atom_pos, radius =atom_radius, color = atom_color);
def get_atom_color(atom):
	return ob.OBElementTable().GetRGB(atom.GetAtomicNum())

def get_coords(atom):
	return vector(atom.GetX(), atom.GetY(), atom.GetZ())
def get_bond_color(atom1, atom2):
    atom1_color = map(float,get_atom_color(atom1))
    atom2_color = map(float,get_atom_color(atom2))
    bond_color = map(int, atom1_color+atom2_color)
    weighted_sum = (0.5* (col1 + col2) for col1, col2 in zip(atom1_color,atom2_color))
    return tuple ( map (int, weighted_sum))
def display_bond (atom1, atom2, bond_color = None):
        atom1Coords = get_coords(atom1)
        atom2Coords = get_coords(atom2)
        bondVector = atom2Coords - atom1Coords
        if bond_color == None:
        	bond_color = get_bond_color(atom1, atom2)
    	cylinder(frame = mol_frame, pos=atom1Coords, axis=bondVector, radius=0.05, color = bond_color)
def display_bonds(mol):
		 ob_mol = mol.OBMol
		 for bond in ob.OBMolBondIter(ob_mol):
		     print(bond.GetId())
		     atom1 = bond.GetBeginAtom()
		     atom2 = bond.GetEndAtom()
		     display_bond(atom1, atom2, (1,1,1))
def animate(cycle):
	sleep(20)
	for atom1, atom2 in zip( cycle[:len(cycle)], cycle[1:]):
		sleep(1)
		bond_color = get_bond_color(atom1, atom2)
		inverse_color = (1,1,0)
		display_bond(atom1, atom2, (inverse_color))
		rotate_mol_animate(pi, 20, 100)

def rotate_mol_animate(tot_rotation, time_per_step, num_steps):
	for a in range(num_steps):
		rate(time_per_step)
		angle_per_step = tot_rotation/num_steps
		mol_frame.rotate(angle=angle_per_step, axis=mol_frame.axis, pos = mol_frame.pos)



