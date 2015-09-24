import openbabel as ob

def exists_eulerian (molecule):
    for atom in molecule.atoms:
        if atom.atomicnum ==1:
            continue
        num_non_H_bonds = atom.heavyvalence
        if heavyvalence % 2 != True:
            return False;  # Eulerian path doesn't exist
    return True; 
def find_eulerian(molecule):
    if not exists_eulerian(molecule):
    	print "No eulerian path exists for that"
     


