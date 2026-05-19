#!/bin/bash

SES=$1
echo "Session: $SES"

for DIR in /Users/akashrathi/Documents/BD2_UCB_dicom_conversions/dicoms/uncompressed/*; do
    BASE_DIR=$(basename "$DIR")

    if [ ! -d "/Users/akashrathi/Documents/BD2_UCB_dicom_conversions/bids/sub-$BASE_DIR/$SES/anat" ]; then
        echo "Processing subject: $BASE_DIR"
        bash /Users/akashrathi/Documents/BD2_UCB_dicom_conversions/scripts/4_single_sub.sh "$BASE_DIR" "$SES"
    fi 
done
