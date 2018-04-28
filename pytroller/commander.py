import os
import subprocess

# ansys_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\ANSYS 16.0\\Mechanical APDL 16.0"
# control_file_path = "C:\\Users\\xuchi\\Desktop\\JiashaoBridge\\model\\control.mac"
# output = subprocess.check_output([ansys_path, "-i", control_file_path])

def RunAPDL():

    ansyspath = r'C:\Users\xuchi\Desktop\JiashaoBridge\test\apdl.exe'
    directory = r'C:\Users\xuchi\Desktop\JiashaoBridge\test'
    jobname = 'file'
    memory = '4096'
    reserve = '1024'
    inputfile = r'C:\Users\xuchi\Desktop\JiashaoBridge\test\ShellBucklingInput.inp'
    outputfile = r'C:\Users\xuchi\Desktop\JiashaoBridge\test\OutputFile.txt'
    resultsfile = r'C:\Users\xuchi\Desktop\JiashaoBridge\test\ShellBuckling.csv'


    # Write input file
    input_parameters = ('/NERR,200,10000,,OFF,0 \n'
                        '/CLEAR'
                        )
    with open(inputfile,'w') as f:
        f.write(input_parameters)

    # Call ANSYS
    callstring = ('\"{}\" -p aa_t_a -dir \"{}\" -j \"{}\" -s read'
                  ' -m {} -db {} -t -d win64 -b -i \"{}\" -o \"{}\"'
                  ).format(ansyspath,directory,jobname,memory,reserve,inputfile,outputfile)
    print('Invoking ANSYS with', callstring)
    proc = subprocess.Popen(callstring).wait()

    # Update pressure field for next analysis
    with open(resultsfile,'r') as f:
        lambdaS = float(list(csv.reader(f))[-1][16])
    p = 1.2*lambdaS*p
    print('Updated pressure is',p,' N/mm2.')

    print ("success")
    return(p) 

if __name__=="__main__":
    # RunAPDL()
    # subprocess.Popen(r'C:\Users\xuchi\Desktop\JiashaoBridge\test\apdl.exe', shell=False, close_fds=True)
    p = subprocess.Popen(r'apdl.exe',shell=True)
