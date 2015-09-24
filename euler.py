import openbabel as ob
import pybel as pb

def exists_eulerian (molecule):
    for atom in molecule.atoms:
        if atom.atomicnum ==1:
            continue
        num_non_H_bonds = atom.heavyvalence
        if heavyvalence % 2 != True:
            return False;  # Eulerian path doesn't exist
    return True; 
def find_eulerian(mol):
	path = []
    if not exists_eulerian(mol):
    	print "No eulerian path exists for that"
   	else:
   		#Hierholtzer's ALGORITHM  for finding Eulerian path
   		mol_no_H = mol.removeh()
   		obmol = mol_no_H.OBMol
   		used_edges = set()
   		obAtom start_atom_ptr = obmol.index(1)
   		Bonds = start_atom_ptr.Bonds()
   		temp_path = []
   		final_path = []
   		visited_edges =set()
   		#while next_atom_ptr.idx != start_atom_ptr.idx:
   		for  obatom in openbabel.OBMolAtomIter(obmol):
   			if obatom in  visited_edges
   				continue
     


