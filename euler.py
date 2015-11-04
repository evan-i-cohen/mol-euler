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
    else:
        #Hierholtzer's ALGORITHM  for finding Eulerian path
        obmol = mol.OBMol
        visited_bonds =set()
        start_atom = mol.GetFirstAtom()
        return find_eulerian(obmol, start_atom, visited_bonds)
             

def find_eulerian(mol, starting_atom, visited_bonds):
    current_tour = []
    current_path.add(starting_atom)
    atoms_with_unused_edges = []
    picked_next_atom = False
    for bond in current_atom:
        if bond in visited_bonds:
           continue
        else:
            if not picked_next_atom:
                visited_bonds.append(bond)
                current_atom = bond.GetNbrAtom(current_atom)
                picked_next_atom = True
            else:
                atoms_with_unused_edges.append(current_atom)
                break
    if len(atoms_with_unused_edges) ==0:
        return current_path
    else:
        start_atom = atoms_with_unused_edges[0]
        return current_path + find_eulerian(mol,start_atom, visited_bonds)

 

            
     

