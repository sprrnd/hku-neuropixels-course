

#%%
# ********************************************************************************************************************************************************
# IBL_quick_start.py
# ********************************************************************************************************************************************************


'''''''''''''''''''''''''''''''''''''''''
import modules
'''''''''''''''''''''''''''''''''''''''''
import numpy as np
import matplotlib.pyplot as plt

'''''''''''''''''''''''''''''''''''''''''
import IBL modules
'''''''''''''''''''''''''''''''''''''''''
from brainbox.io.one import SpikeSortingLoader
from one.api import ONE


'''''''''''''''''''''''''''''''''''''''''
Define directories
'''''''''''''''''''''''''''''''''''''''''
# define path for downloading IBL data
PATH_one = "/home/IBL/" # substitute for your own


'''''''''''''''''''''''''''''''''''''''''
setup ONE api - connect to IBL database
    !!! make sure to have setup ONE first e.g. run IBL_setup_one.py script
'''''''''''''''''''''''''''''''''''''''''
# openalyx is the datasharing platform for publicly released IBL data
one = ONE(base_url="https://openalyx.internationalbrainlab.org", mode='remote', cache_dir=PATH_one)

'''''''''''''''''''''''''''''''''''''''''
searching/loading data with ONE
'''''''''''''''''''''''''''''''''''''''''
# can access data search and loading functions through ONE-api
print(one.search_terms())


'''''''''''''''''''''''''''''''''''''''''
filter insertions which pass through particular regions
'''''''''''''''''''''''''''''''''''''''''
atlas_acronym = 'VTA'
_, insertions = one.search_insertions(atlas_acronym=atlas_acronym, query_type='remote', project='ibl_neuropixel_brainwide_01', details=True)

print(f'n{len(insertions)} probes passing through {atlas_acronym}:\n {insertions}')

'''''''''''''''''''''''''''''''''''''''''
extract probe IDs (pid) for relevant insertions
'''''''''''''''''''''''''''''''''''''''''
pids = [ins['id'] for ins in insertions]

'''''''''''''''''''''''''''''''''''''''''
extract session IDs (eid) for relevant insertions
'''''''''''''''''''''''''''''''''''''''''
eids = [ins['session'] for ins in insertions]


#%%
# ********************************************************************************************************************************************************
# DATA DOWNLOAD: single insertion example
# ********************************************************************************************************************************************************
'''''''''''''''''''''''''''''''''''''''''
Init data loader
'''''''''''''''''''''''''''''''''''''''''
# example insertion pid
pid = '50ebb677-e4a3-4421-b74f-1997a9cd1ad1'
ssl = SpikeSortingLoader(pid=pid, one=one)

'''''''''''''''''''''''''''''''''''''''''
Spikesorted data
'''''''''''''''''''''''''''''''''''''''''
# run spikesorted data download
ssl.download_spike_sorting(collection=f'alf/{ssl.pname}/pykilosort')


'''''''''''''''''''''''''''''''''''''''''
OPTIONAL - Raw data
    !!! the raw data size for each insertion is between 50-100GB so it takes time and space to download
    Can do most analysis on spikesorted data directly
'''''''''''''''''''''''''''''''''''''''''
# ssl.download_raw_electrophysiology(band='ap') # ap and lfp available

#%%
# ********************************************************************************************************************************************************
# SPIKESORTED DATA LOADING: single insertion example
# ********************************************************************************************************************************************************

'''''''''''''''''''''''''''''''''''''''''
load spikesorted data
'''''''''''''''''''''''''''''''''''''''''
# Via IBL spikesorting loader 
spikes, clusters, channels = ssl.load_spike_sorting(revision = '2024-05-06')
clusters = ssl.merge_clusters(spikes, clusters, channels)
path_spikesorted = ssl.spike_sorting_path

# can check downloaded data under
path_spikesorted= ssl.spike_sorting_path
print(f'spikesorted data downloaded at {path_spikesorted}')

# each neuron is assigned a cluster_id and corresponding Allen Atlas region acronym
cluster_ids = clusters['cluster_id']
cluster_regions = clusters['acronym']

# each ephys spike time corresponding to a neuron cluster id contained in spike_clusters
spike_times = spikes['times']
spike_clusters = spikes['clusters']

# amplitude of recorded spikes
spike_amps= spikes['amps']
# depth along probe of recorded spikes
spike_depths = spikes['depths']

#%%
# ********************************************************************************************************************************************************
# SPIKESORTED DATA LOADING: single neuron example
# ********************************************************************************************************************************************************

'''''''''''''''''''''''''''''''''''''''''
filter clusters by region
'''''''''''''''''''''''''''''''''''''''''
# e.g. find cluster ids in specific region
filter_region = 'VTA'
cids_in_region = cluster_ids[np.where(cluster_regions==filter_region)]
print(f'n{len(cids_in_region)} clusters in {filter_region} recorded on probe {pid}\n cluster IDs: {cids_in_region}')

assert len(cids_in_region)>0, print(f'no good clusters recorded in {filter_region} on probe {pid}')

'''''''''''''''''''''''''''''''''''''''''
spike data for single neuron cluster (cid)
'''''''''''''''''''''''''''''''''''''''''
# load spike times for neurons in filter_region
cid = cids_in_region[0]
cid_region = cluster_regions[cid]
print(f'loading spike times for cluster {cid}')
cid_spike_times = spike_times[np.where(spike_clusters == cid)]
cid_spike_amplitudes = spike_amps[np.where(spike_clusters == cid)]
print(f'n{len(cid_spike_times)} spikes for cluster {cid}')


'''''''''''''''''''''''''''''''''''''''''
plot spike times vs amplitude
'''''''''''''''''''''''''''''''''''''''''
# e.g. plot spike times in 10s interval
Dt = 10
time_interval = (cid_spike_times>=Dt) & (cid_spike_times<Dt)

spikes_in_interval = cid_spike_times[time_interval]
amps_in_interval = cid_spike_amplitudes[time_interval]

plt.scatter(spikes_in_interval, amps_in_interval, marker='.', color='black')
plt.xlabel('Time (s)')
plt.ylabel('Spike Amplitude')
plt.show()


#%%
# ********************************************************************************************************************************************************
# TRIAL DATA LOADING: single session example
# ********************************************************************************************************************************************************

'''''''''''''''''''''''''''''''''''''''''
load session trials data
'''''''''''''''''''''''''''''''''''''''''
# find session eid corresponding to insertion pid
eid = one.pid2eid(pid)[0]

# load trial data
trials = one.load_object(eid, 'trials')
print(trials.keys())

# key trial times
stimon_times = trials.stimOn_times
firstmove_times = trials.firstMovement_times
feedback_times = trials.feedback_times
stimoff_times = trials.stimOff_times


'''''''''''''''''''''''''''''''''''''''''
trial-aligned firing rates
'''''''''''''''''''''''''''''''''''''''''
# e.g. align to feedback time +/- 500ms
dt = 0.5 # s, trial interval
starts = trials.feedback_times - dt
ends = trials.feedback_times + dt

trial_aligned_st = [cid_spike_times[(cid_spike_times >= start) & (cid_spike_times < end)] - start for start, end in zip(starts, ends)]
print(f'number of trials = {len(trial_aligned_st)}')

'''''''''''''''''''''''''''''''''''''''''
bin spikes
'''''''''''''''''''''''''''''''''''''''''
bin_size = 0.01 # s
trial_duration = ends[0] - starts[0]
all_aligned_spikes = np.concatenate(trial_aligned_st)

bins = np.arange(0, trial_duration + bin_size, bin_size)
counts, _ = np.histogram(all_aligned_spikes, bins=bins)

# convert to firing rate
n_trials = len(starts)
firing_rate = counts / (n_trials * bin_size)

bin_centers = bins[:-1] + bin_size / 2 - dt

'''''''''''''''''''''''''''''''''''''''''
plot PSTH
'''''''''''''''''''''''''''''''''''''''''
plt.figure()
plt.bar(bin_centers, firing_rate, width=bin_size, align='center', color='lightgrey')
plt.xlabel("Time from feedback (s)")
plt.ylabel("Firing rate (Hz)")
plt.axvline(0, color='black', linestyle='-', linewidth=1)
plt.title(f"PSTH\n probe insertion {pid}\n cluster {cid} in {cid_region}")
plt.show()


# %%
