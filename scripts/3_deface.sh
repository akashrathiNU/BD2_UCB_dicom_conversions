SUB=$1 #check if $ needed. 
echo $SUB
SES=$2 #check if $ needed. 
echo $SES

mv /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/*T1w.* /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/anat/
mv /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/*phase* /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/fmap/
mv /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/*mag* /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/fmap/
mv /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/*epi* /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/fmap/
mv /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/*dwi* /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/dwi/
pydeface --verbose /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/anat/sub-${SUB}_${SES}_run-1_T1w.nii.gz 
mv /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/anat/sub-${SUB}_${SES}_run-1_T1w_defaced.nii.gz \
/Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/anat/sub-${SUB}_${SES}_run-1_T1w.nii.gz
rm /Users/akashrathi/Documents/Github/BD2_UCB_dicom_conversions/bids/sub-$SUB/${SES}/${SUB}-*