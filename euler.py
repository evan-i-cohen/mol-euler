import openbabel as ob
import pybel as pb

def exists_eulerian (molecule):
    for atom in molecule.atoms:
        num_bonds = atom.valence
        if num_bonds % 2 != 0:
            return False;  # Eulerian path doesn't exist
    return True; 
def find_euler(mol):
    path = []
    mol.removeh()
    if not exists_eulerian(mol):
        print "No eulerian path exists for that"
        return_val = [];
    else:
        #Hierholtzer's ALGORITHM  for finding Eulerian path
        obmol = mol.OBMol
        visited_bonds =set()
        start_atom = obmol.GetFirstAtom()
        return_val =find_eulerian(obmol, start_atom, visited_bonds)
    mol.addh()
    return return_val;
             

def find_eulerian(mol, starting_atom, visited_bonds):
    current_path = []
    atoms_with_unused_edges = []
    current_atom = starting_atom
    is_first_run = True
    while  current_atom != None and  (is_first_run  or current_atom.GetIdx() != starting_atom.GetIdx()): 
        current_path.append(current_atom)
        is_first_run = False
        current_atom = pick_next_atom(current_atom, visited_bonds, atoms_with_unused_edges)     
    if current_atom is None:  # we reached beginning
        return current_path 
    else:
        start_atom = atoms_with_unused_edges[0]
        return current_path + find_eulerian(mol,start_atom, visited_bonds)
def pick_next_atom(current_atom, visited_bonds, atoms_with_unused_edges):
    picked_next_atom = False
    bonds_connected_to_atom = ob.OBAtomBondIter(current_atom)
    next_atom = None
    for bond in bonds_connected_to_atom:
            if bond.GetIdx() in visited_bonds:
               continue
            else:
                if not picked_next_atom:
                    visited_bonds.add(bond.GetIdx())
                    next_atom = bond.GetNbrAtom(current_atom)
                    picked_next_atom = True
                else:
                    atoms_with_unused_edges.append(current_atom)
                    break
    return next_atom

            
     

