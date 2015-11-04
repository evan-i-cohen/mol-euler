
'''
First argument is name of file ( in xyz format)
e.g. python main benzene.xyz
'''
import openbabel as ob
main(args):
	mol_file = args[0]
	assert mol_file.split(".")[-1] is "xyz"
	molecule = ob.readFile("xyz", mol_file)
	print("You inputted the molecule"+ mol_file[:".xyz"] +"\n")
	print("The structure looks like\n")
	#ob.draw(molecule)
	find_eulerian()








if __name__ == '__main__':
	main(sys.argv[1:])
