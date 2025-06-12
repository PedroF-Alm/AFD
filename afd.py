def getMachine():
    machine = {'(': 'LParenteses', 
               ')': 'RParenteses', 
               '{': 'LChave',  
               '}': 'RChave',
               '[': 'LColchete',
               ']': 'RColchete',
               '=': {'=': 'EQ', '$': 'Atribuicao'},
               '>': {'=': 'GEQ', '$': 'GT'},
               '<': {'=': 'LEQ', '$': 'LT'},
               '!': {'$':'NEG'},
               ',': 'Virgula',
               ';': 'PVirgula',
               'i': {'f': {' ': 'IF'}, 'n': {'t': {' ': 'INTDEF'}}},               
               '+': 'SUM',
               '-': 'SUB',
               '*': 'MULT',
               '/': 'DIV',
               '%': 'RESTO',
               'f': {'l': {'o': {'a': {'t': {' ': 'FLOATDEF'}}}}},
               '&': {'&': 'AND'},
               '|': {'|': 'OR'},                                
               '.': {},
               'c': {'h': {'a': {'r': {' ': 'CHAR_TYPE'}}}},       
               'b': {'o': {'o': {'l': {' ': 'BOOL_TYPE'}}}},       
               'r': {'e': {'t': {'u': {'r': {'n': {' ': 'RETURN'}}}}}},       
               'v': {'a': {'r': {' ': lambda : Exception}}},       
               }
    
    for i in range(0, 10):
        machine[str(i)] = {'$': 'NUM_INT', '.': {}}
        machine['.'][str(i)] = {'$': 'NUM_FLOAT'}

    aux = [chr(j) for j in range(ord('a'), ord('z') + 1)]
    aux.extend([chr(j) for j in range(ord('A'), ord('Z') + 1)])

    for i in aux:
        machine['v']['a']['r'][i] = {'$': 'VAR'}

    for i in aux:
        for j in aux:
            machine['v']['a']['r'][i][j] = machine['v']['a']['r'][i]

    for i in range(0, 10):
        for j in range(0, 10):
            machine[str(i)][str(j)] = machine[str(i)]            
            machine[str(i)]['.'][str(j)] = {'$': 'NUM_FLOAT'}              
            machine['.'][str(i)][str(j)] = machine['.'][str(i)]     
            for k in range(0, 10):
                machine[str(i)]['.'][str(j)][str(k)] = machine[str(k)]['.']  
  
    return machine

def processFile(file):     
    machine = getMachine()
    line = file.readline()
    line_number = 1
    output = ''
    while line != '':
        machine = getMachine()
        i = 0
        while i < len(line):
            symbol = line[i]
            try:
                if symbol in machine.keys() and (type(machine[symbol]) == str):
                    print(machine[symbol], end=' ')
                    output += machine[symbol]
                    machine = getMachine()
                elif symbol in machine.keys():
                    machine = machine[symbol] 
                elif '$' in machine.keys():
                    print(machine['$'], end=' ')
                    output += machine['$']
                    machine = getMachine()
                    i -= 1
                else:
                    machine = getMachine()
                    i += 1
                    raise Exception
                i += 1
            except:     
                if (symbol != '\n' and symbol != ' '):
                    print(f"\nFalhou em {line_number}:{i}")
                    return None   
        line = file.readline()
        line_number += 1
        print()    
        output += '\n'
    return output