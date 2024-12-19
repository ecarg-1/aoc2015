molecule = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
replacements, rev_repl = dict(), dict()
with open ('input.txt','r') as f:
    input_list = [line.strip('\n').split(' ') for line in f]
    f.close()
for element in input_list:
    if element[0] in replacements.keys(): replacements[element[0]].append(element[-1])
    else: replacements[element[0]] = [element[-1]]
    rev_repl[element[-1]] = element[0]
def make_list(molecule):
    molecule_list = []
    for i in range(len(molecule)):
        element_str = ''
        if molecule[i].isupper() or molecule[i]=='e': 
            element_str+=molecule[i]
            try:
                if molecule[i+1].islower():
                    element_str+=molecule[i+1]
            except:
                pass
            molecule_list.append(element_str)
    return molecule_list
molecule_list = make_list(molecule)
def repl(molecule_list):
    change_molecules = []
    for i in range(len(molecule_list)):
        try:
            for molecule in replacements[molecule_list[i]]:
                new_list = molecule_list.copy()
                new_list[i]=molecule
                change_molecules.append(''.join(new_list))
        except:
            pass
    return change_molecules
change_molecules = repl(molecule_list)
print(len(set(change_molecules))) #part 1

from random import shuffle
import re
def idk(m):
    count = 0
    keys = list(rev_repl.keys())
    while(m != 'e'):
        for key in keys:
            count += m.count(key)
            m = re.sub(key, rev_repl[key], m)
    return count
print(idk(molecule)) #Part 2

