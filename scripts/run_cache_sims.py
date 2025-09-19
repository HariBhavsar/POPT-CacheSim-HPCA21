import os, subprocess
import launcher

## Compile all simulators & applications
origDir = os.getcwd()
os.chdir(origDir + '/../applications')
subprocess.call('python compile_all.py', shell=True)

os.chdir(origDir + '/../simulators')
subprocess.call('python compile_all.py', shell=True)
os.chdir(origDir)
subprocess.call('mkdir -p ../raw_data', shell=True)

print('****************************')
print('[COMPILED. STARTING SIMS...]')
print('****************************')

## Launch simulations
apps        = ['pr']
simulators  = ['popt-8b']
versions    = ['popt']
graphs      = ['GAP-kron','GAP-urand']

for app in apps:
    for s in range(len(simulators)):
        simulator = simulators[s]
        version   = versions[s]
        for graph in graphs:
            cmd = launcher.launchSim(app, graph, simulator, version)
            subprocess.call(cmd, shell=True)


print('****************************')
print('[CACHE SIMS FINISHED]')
print('****************************')
