import numpy as np

import subprocess
import os


def parse_sdds_table(sddsfile, columns, sdds2plaindata_exe='sdds2plaindata'):
    """
    Get tabular data from SDDS file.
    
    Example:
        get_table('LCLS2scH.twi', ['s', 'betax', 'betay', 'etax'])
    """

    assert os.path.exists(sddsfile)

    outfile = sddsfile+'_table'
    cmd0 = [sdds2plaindata_exe, sddsfile, outfile, '-noRowCount', '-outputMode=ascii']

    cmd = cmd0 + [f'-col={c}' for c in columns] + ['-separator= ']

    output,error  = subprocess.Popen(
                    cmd, universal_newlines=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    assert os.path.exists(outfile), f'{outfile} does not exist'

    rdat = np.loadtxt(outfile)

    dat = {}
    for i, key in  enumerate(columns):
        dat[key] = rdat[:,i]

    os.remove(outfile)
    return dat

def get_twiss_elegant(elegant_twiss_file_name):

    d = parse_sdds_table(elegant_twiss_file_name, ['betax','alphax','betay','alphay','etax','etaxp','etay','etayp'])
    
    t1 =  d['betax'][-1]
    t2 =  d['alphax'][-1]
    t3 =  d['betay'][-1]
    t4 =  d['alphay'][-1]
    t5 =  d['etax'][-1]
    t6 =  d['etaxp'][-1]
    t7 =  d['etay'][-1]
    t8 =  d['etayp'][-1]
    
    return np.array([t1, t2, t3, t4, t5, t6, t7, t8])


def get_twiss_tao(tao, ele):
    t1 = tao.lat_list(ele, 'beta_a')[0]
    t2 = tao.lat_list(ele, 'alpha_a')[0]
    t3 = tao.lat_list(ele, 'beta_b')[0]
    t4 = tao.lat_list(ele, 'alpha_b')[0]
    t5 = tao.lat_list(ele, 'eta_x')[0]
    t6 = tao.lat_list(ele, 'etap_x')[0]
    t7 = tao.lat_list(ele, 'eta_y')[0]
    t8 = tao.lat_list(ele, 'etap_y')[0]
    return np.array([t1, t2, t3, t4, t5, t6, t7, t8])
