import os
from PyPDF2 import PdfFileMerger

path_to_files = '/home/sabuj/projects/educative.io_courses/GCN' # root directory
files_arr = []
lo = 1 # place first file id
hi = 115 # place last file id

# traverse files
for root, dirs, file_names in os.walk(path_to_files):
    for file in file_names:
        if (file == "merge.py"): continue
        files_arr.append(file)

# sort the files_arr
files_arr.sort(key= lambda x: int(x.split('_')[0]))

#Create an instance of PdfFileMerger() class
merger = PdfFileMerger()

# merge files in order
for file in files_arr:
    print("Merging", file, ".............")
    merger.append(file)

#Write out the merged PDF file
merger.write("final.pdf")
merger.close()
