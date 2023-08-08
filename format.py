#=============================================================================
#=============================================================================
#                        File organizer program
#=============================================================================
#=============================================================================


import os

# List creation
File_format  = []
File_split = []
Dir_name= []



# Ask the directory path
#------------------------
Dir_path = input("Enter the path where unorganized files are : ")
# C:\Users\guill\OneDrive\Bureau\PYTHON\File organizer program\First



# Find all file format
#------------------------

# Put all file names in a list
All_file = os.listdir(path=Dir_path)

# Find file format
for file in All_file:
    # select files and not other directories
    if len( file.split('.') ) > 1 and file.split('.')[-1] not in File_format  :
        File_format.append(file.split('.')[-1])
 

  

    
# Create a directory for each format
#------------------------------------

Dic_format = {'docx' : 'Microsoft Word document',
              'png'  : 'Portable Network Graphics',
              'pptx' : 'Microsoft PowerPoint presentation',
              'txt'  : 'Text',
              'xlsx' : 'Microsoft Excel workbook',
              'mp3'  : 'Mp3',
              'mp4'  : 'Mp4',
              'jpg'  : 'Jpg'
              }

for i in range(len(File_format)):
    try:
        dir_name = Dic_format[File_format[i]]
        # Create new directory
        os.mkdir(Dir_path + '/' + dir_name + ' files')
        # Save the directory name in a list
        Dir_name.append(dir_name + ' files')
    except FileExistsError:
        print('The directory already exist')
        # Save the directory name in a list
        Dir_name.append(dir_name + ' files')





# Move files in directories
#------------------------------------

for file in All_file:
    # select files and not other directories
    if len( file.split('.') ) > 1 :
        try:
            # Rename path
            os.rename(Dir_path + '/' + file, Dir_path + '/' + Dic_format[file.split('.')[-1]] + ' files/' + file)
        except FileExistsError:
            print('This file already exist on that directory')
            




# Create a Read me text file
#------------------------------------

f = open('./first/' + 'Read_Me.txt', 'w')
f.write("Moved files and their directory\n")
f.write("===============================\n\n")


for directory in Dir_name:      
    f.write(directory + '\n')    
    for file in All_file:
        if len( file.split('.') ) > 1 and directory  == Dic_format[file.split('.')[-1]] + ' files':
            f.write('     ' + file + '\n')           
    f.write('\n\n') 
 
      
f.close()

    





