#!/usr/bin/env bash
# SET PATH OF EXECUTABLES
FREECONTACT='PATH/TO/FREECONTACT'
HHBLITS='PATH/TO/HHBLITS'
PHOBIUS='PATH/TO/PHOBIUS'

# SET PATH OF DIRECTORIES
DB='PATH/TO/HHBLITS/DB/'

while getopts ":n:c:i:" opt
do
    case $opt in
        n)
        ps=$OPTARG
        ;;
        c)
        pc=$OPTARG
        ;;
        i)
        in=$OPTARG
        ;;
        ?)
        echo "parameter errors, please see README of the software."
        exit 1;;
    esac
done

$PHOBIUS $in$ps$pc'.fasta' > $in$ps$pc'.jphobius'
$HHBLITS -i $in$ps$pc'.fasta' -maxfilt 100000 -realign_max 100000 -d $DB -all -B 100000 -Z 100000 -n 3 -e 0.001 -oa3m $in$ps$pc'.a3m'
egrep -v "^>" $in$ps$pc'.a3m' | sed 's/[a-zA-Z]//g' > $in$ps$pc'.aln'
egrep -v "^>" $in$ps$pc'.a3m' | sed 's/[a-z]//g' > $in$ps$pc'.faln'
$FREECONTACT < $in$ps$pc'.aln' > $in$ps$pc'.evfold'
