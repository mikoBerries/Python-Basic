import zipfile


f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()

f = open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()

# zipping file similar like write and read in file
# there are many copression type online we can choose
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# grab path zipped file with only read permission
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")


# using shutil to zipping entire folder and file inside it
import shutil
import os 

directory_to_zip=os.getcwd()+"\\extracted_content"
output_filename = 'example'
# zipping
shutil.make_archive(output_filename,'zip',directory_to_zip)

dir_for_extract_result=os.getcwd()+"\\extracted_content"
# unzipping
shutil.unpack_archive(output_filename+'zip',dir_for_extract_result,'zip')