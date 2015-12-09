import sys
import openbabel as ob
import pybel as pb
import euler
import graphics

def main(args):
    assert len(args) ==1
    mol_file = args[0]
    assert mol_file.split(".")[-1] == 'xyz'
    molecule = pb.readfile("xyz", mol_file).next()
    print("You inputted the molecule"+ mol_file.split(".")[0] +"\n")
    print("The structure looks like\n")
    eulerian_cycle= euler.find_euler(molecule)
    assert(list != None)
    for atom in eulerian_cycle:
		print(atom.GetIdx())
    graphics.set_background_color(1,1,1)
    graphics.display_atoms(molecule)
    print('done')
    graphics.display_bonds(molecule)
    graphics.animate(eulerian_cycle)






if __name__ == '__main__':
	main(sys.argv[1:])