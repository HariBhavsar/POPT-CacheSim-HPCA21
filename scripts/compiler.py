import os

def findFile(app, graph, policy, version):
    searchStr = 'out_' + app + '_' + graph + '_' + policy + '_' + version + '.dat'
    for i in os.listdir(os.getcwd() + '/../raw_data'):
        if searchStr in i:
            return './../raw_data/' + i

def getLLCMisses(app, graph, policy, version):
    "Return LLC Demand misses"
    fname = findFile(app, graph, policy, version)
    f     = open(fname, 'r')
    lines = f.readlines()
    f.close()
    
    miss = 0
    for lnum in range(len(lines)):
        if '[LLC-STAT] Total Misses' in lines[lnum]:
            temp = lines[lnum].strip('\n')
            line = temp.split(' ')
            miss += float(line[len(line)-1])
    return miss
            
def getInstructions(app, graph, policy, version):
    "Return LLC Demand misses"
    fname = findFile(app, graph, policy, version)
    f     = open(fname, 'r')
    lines = f.readlines()
    f.close()
    
    miss = 0
    for lnum in range(len(lines)):
        if '[PINTOOL] No. of Instructions(unique)' in lines[lnum]:
            temp = lines[lnum].strip('\n')
            line = temp.split(' ')
            miss += float(line[len(line)-1])
    return miss

def getMPKI(app, graph, policy, version):
    "Return LLC Demand misses"
    fname = findFile(app, graph, policy, version)
    f     = open(fname, 'r')
    lines = f.readlines()
    f.close()
    
    miss = 0
    ins = 0
    for lnum in range(len(lines)):
        if '[PINTOOL] No. of Instructions' in lines[lnum]:
            temp = lines[lnum].strip('\n')
            line = temp.split(' ')
            ins += float(line[len(line)-1])
        if '[LLC-STAT] Total Misses' in lines[lnum]:
            temp = lines[lnum].strip('\n')
            line = temp.split(' ')
            miss += float(line[len(line)-1])
    return ((miss * 1000)/ins)