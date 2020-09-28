# Problem Statement
I receive a plain text file for Adoption and Foster Care information. The file needs to be parsed into columns. Each column has its own width. Then the file needs to be saved as a CSV file with the header row. The Adoption File and Foster Care file have their own headers and column widths.

Once the file is parsed, then the text file is used in another two programs that were created a long time ago in C. These programs analyze the text file and produces an output. The programs need to be run once for the Adoption file and then again for the Foster Care file.

Currently the department uses Microsoft Access to parse the file and exports it as an Microsoft Excel file. Access sometimes would not work and it becomes time consuming to figure out why. Then the text file would have to manually be moved to another folder to run the other two programs because they would not always run properly if the text file is in another location. This whole process is tedious and unreliable.

# Solution
I created a Python program that parses the text file with the correct column widths and creates a CSV file for both the Adoption and Foster Care file. At the same time, the program moves the text files to the folder where the other programs are and runs the programs. It automatically types the file path and any information the program asks. The output files are then moved back to the folder where the text file originally was. The user only needs to put in the file location once. I used the pyinstaller module to make the program an executable for staff that do not have Python on their computers.

** See below for an example. I am not able to add actual examples to the github page because of the confidentiality of the information and the old programs only work in my work directory. 

1. Download text files.
![Text File](.\images\text_file.JPG)

2. Save text files.
![Save File](.\images\file_loc.JPG)

3. Run the Python program.
![Run Program](.\images\parser.JPG)

4. Enter the file locations.
![File Info](.\images\run.JPG)

5. The files will be parsed and analyzed.
![Output](.\images\output.JPG)

6. The new parsed file and reports can be used.
![New File](.\images\cout.JPG)
