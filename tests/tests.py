
#test 1 
import main
import openbabel as ob
import pybel as pb
mol = pb.readfile("xyz", "benzene.xyz").next()
main(mol) 
