#%%
# ********************************************************************************************************************************************************
# IBL_setup_one.py
# ********************************************************************************************************************************************************

'''''''''''''''''''''''''''''''''''''''''
setup ONE-api
'''''''''''''''''''''''''''''''''''''''''

# run this once to setup the ONE environment
# can check here for more instructions and debugging: https://int-brain-lab.github.io/ONE/one_installation.html


from one.api import ONE
ONE.setup(base_url='https://openalyx.internationalbrainlab.org', silent=True)
one = ONE(password='international')
