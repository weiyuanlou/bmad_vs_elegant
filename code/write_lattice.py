def write_bmad_lattice(ele_type, dict_bmad, root_dir):
    
    out1 = f"""parameter[particle] = electron
no_digested

beginning[beta_a] = 10
beginning[alpha_a] = 1
beginning[beta_b] = 10
beginning[alpha_b] = 1

parameter[geometry] = open
parameter[p0c] = 10e6

ele1: {ele_type}"""
    
    out2 = ""
    for key, value in dict_bmad.items():
        out2 += f",\n{key} = {value}"
    
    out3 = """\n
lat: line = (ele1)

use, lat
    """
    
    f = open(root_dir+"/bmad/one_ele.bmad", "wt")
    f.write(out1)
    f.write(out2)
    f.write(out3)
    f.close()
    
    return None
    


def write_elegant_lattice(ele_type, dict_elegant, root_dir):
    
    out1=f"""C: CHARGE,TOTAL= 13E-12
    
ELE1: {ele_type}"""

    out2 =""
    for key, value in dict_elegant.items():
        out2 += f", &\n{key} = {value}"

    out3 = """\n
BPM_END: WATCH,FILENAME="BPM_END.out"

MYLINE: LINE = (C, ELE1, BPM_END)
    """
    
    f = open(root_dir+"/elegant/one_ele.lte", "wt")
    f.write(out1)
    f.write(out2)
    f.write(out3)
    f.close()        

    return None


