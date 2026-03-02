import os
import glob
import sys

#Setting input arguments as variables
sub = sys.argv[1]
ses = sys.argv[2]



# Make anatomical, functional, dwi, and fieldmap folders in bids folder
def make_bids_dirs(sub,ses,bids_dir):
    anat_dir = bids_dir+'/'+'sub-'+sub+'/'+ses+'/'+'anat/'
    os.makedirs(anat_dir, exist_ok=True)

    func_dir = bids_dir+'/'+'sub-'+sub+'/'+ses+'/'+'func/'
    os.makedirs(func_dir, exist_ok=True)

    fmap_dir = bids_dir+'/'+'sub-'+sub+'/'+ses+'/'+'fmap/'
    os.makedirs(fmap_dir, exist_ok=True)
   
    fmap_dir = bids_dir+'/'+'sub-'+sub+'/'+ses+'/'+'dwi/'
    os.makedirs(fmap_dir, exist_ok=True)

# Rename each filename to BIDS format
def rename_partic(sub, ses, bids_dir): 
    print(sub + " " + bids_dir)
    print("in rename partic")
    directory = bids_dir+'/sub-'+sub+'/'+ses+'/'
    print(directory)

    


    # AP_REV indicates a fieldmap in the reverse direction; we denote this as 'PA' (posterior to anterior) in BIDS format
    files = sorted(glob.glob(directory + "*--SpinEchoFieldmap_MID_AP_REV--*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-01_dir-PA_epi." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    #Same process as PA, except we are looking at AP (forward direction fieldmap)

    files = sorted(glob.glob(directory + "*--SpinEchoFieldmap_MID_AP--*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-01_dir-AP_epi." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name)
        

    # MID run-1
    files = glob.glob(directory + "*MID_run-1--*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-01_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    #MID run-2
    files = glob.glob(directory + "*MID_run-2--*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-02_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    #T1w image
    counter = 0
    files = glob.glob(directory + "*t1_mpg_sag*")
    for file in files:
        if counter < 2:
            print(file)
            parts = file.split(".", 2)
            new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_run-1_T1w." + parts[2])
            print(directory + new_name)
            os.rename(file, new_name)
            counter +=1
        else: 
            print(file)
            parts = file.split(".", 2)
            new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_run-2_T1w." + parts[2])
            print(directory + new_name)
            os.rename(file, new_name)
            counter +=1

    #RL run-1
    files = glob.glob(directory + "*task-RLCAT_run-01*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-RL_run-01_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name)
    
    #RL run-2
    files = glob.glob(directory + "*task-RLCAT_run-02*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-RL_run-02_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name)
    
    #RL run-3
    files = glob.glob(directory + "*task-RLCAT_run-03*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-RL_run-03_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name)

    #DWI AP
    files = glob.glob(directory + "*DTI_AP*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_run-1_dir-AP_dwi." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name)

    #DWI PA
    files = glob.glob(directory + "*DTI_PA*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_run-1_dir-PA_dwi." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e1.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-1_part-mag_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e2.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-2_part-mag_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e3.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-3_part-mag_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e4.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-4_part-mag_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e5.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-5_part-mag_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e6.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-6_part-mag_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e7.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-7_part-mag_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e8.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-8_part-mag_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e1_ph.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-1_part-phase_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e2_ph.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-2_part-phase_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e3_ph.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-3_part-phase_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e4_ph.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-4_part-phase_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e5_ph.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-5_part-phase_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e6_ph.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-6_part-phase_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e7_ph.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-7_part-phase_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

    #Tissue Iron Mapping
    files = glob.glob(directory + "*QSM_8echo*e8_ph.*")
    for file in files:
        print(file)
        parts = file.split(".", 2)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-echo_flip-16_echo-8_part-phase_bold." + parts[2])
        print(directory + new_name)
        os.rename(file, new_name)

def main(sub, ses, bids_dir='/Users/akashrathi/Documents/Github/BD2_dicom_conversions/bids'):
    make_bids_dirs(sub,ses,bids_dir)
    rename_partic(sub,ses,bids_dir)

main(sub, ses)
