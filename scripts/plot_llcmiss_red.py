import matplotlib
matplotlib.use('Agg')   # Use non-GUI backend
import matplotlib.pyplot as plt
import numpy as np
import compiler

app         = 'pr'
appNick     = 'PAGERANK'
policies    = ['lru', 'popt-8b', 'exclusive', 're-exclusive']
policyNicks = ['Non-Inclusive',  'P-OPT', 'Exclusive', 'Re-Exclusive']
versions    = ['baseline', 'popt', 'baseline', 'baseline']
graphs      = ['uk-2002', 'kron25-d4', 'urand25-d4', 'hugebubbles-00020', 'GAP-twitter']
graphNicks  = ['UK-02', 'KRON', 'URND', 'HBBL', 'Twitter']

# Define distinct colors for each policy
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

## Collect LLC Miss data
data_misses = {}
for graph in graphs:
    data_misses[graph] = {}
    for p in range(len(policies)):
        policy  = policies[p]
        version = versions[p]
        data_misses[graph][policy] = compiler.getLLCMisses(app, graph, policy, version)

## Collect Instructions data
data_instrs = {}
for graph in graphs:
    data_instrs[graph] = {}
    for p in range(len(policies)):
        policy  = policies[p]
        version = versions[p]
        data_instrs[graph][policy] = compiler.getMPKI(app, graph, policy, version)

## Plot results
fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=False)  # separate y scales

bwidth = 1 / (1.25 + len(policies))

def plot_bar(ax, data, ylabel, title_suffix):
    maxVal = 0
    vals_per_policy = []
    for p in range(len(policies)):
        policy = policies[p]
        vals   = [data[graph][policy] for graph in graphs]
        vals_per_policy.append(vals)
        maxVal = max(maxVal, max(vals))
    ind = np.arange(len(graphs))
    
    for p, vals in enumerate(vals_per_policy):
        ax.bar(ind + p * bwidth, vals, width=bwidth,
               label=policyNicks[p], color=colors[p])
    
    ax.set_title(f'App - {appNick} ({title_suffix})', fontweight='bold')
    ax.set_xlabel('Input Graphs', fontweight='bold')
    ax.set_ylabel(ylabel, fontweight='bold')
    ax.set_xticks(np.arange(len(graphs)) + 1.5 * bwidth)
    ax.set_xticklabels(graphNicks)
    ax.set_yticks(np.arange(0, 1.1 * maxVal, maxVal/5))
    ax.grid(alpha=0.64, axis='y', linestyle='--')
    # ax.axhline(y=1, linestyle='--', color='k')

# Left: LLC Misses
plot_bar(axes[0], data_misses, ylabel="LLC Misses", title_suffix="LLC Misses")

# Right: Instructions
plot_bar(axes[1], data_instrs, ylabel="Instructions", title_suffix="Instructions")

# Put legend once above both plots
fig.legend(
    loc='lower center',
    bbox_to_anchor=(0.5, 1.02),  # centered above figure
    framealpha=1.0,
    ncol=2
)

plt.tight_layout(rect=[0,0,1,0.95])  # leave room for legend
plt.savefig('llcmiss-vs-instr.pdf')

print('*********************************')
print('[OUTPUT SAVED TO llcmiss-vs-instr.pdf]')
print('*********************************')
