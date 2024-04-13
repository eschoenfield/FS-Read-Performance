# FS-Read-Performance
This research aims to provide insight for what file system performs the best for reading small files on Linux by comparing the performance of the ext2, ext4, XFS, ZFS, and FAT32 file systems. 

## Usage
RAW output test values stored in .csv files named "myout-***.csv" where "***" is the file system name.

python script usage:
$python3 ddDataCollectionScript.py

R-Studio: 
If you'd like to replicate the graphs and tables for average times you'll need to update the path to the "myout-***.csv" files
