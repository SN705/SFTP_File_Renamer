# SFTP_File_Renamer
For each file with a ".csv" extension, this script renames the file by replacing the extension with ".csv.ready".

SFTP File Renamer
By: Simon Nadeau

The following Python script achieves the following:

1. Establish an SFTP connection to the remote server.
2. Set the directory path.
3. List the files in the directory.
4. For each file with a ".csv" extension:
     - Rename the file by replacing the extension with ".csv.ready".
     - Print a success message for the rename operation.
5. Close the SFTP connection.
6. Print a success message indicating the script executed without errors.

If reading this as a plain text file, save as .py to execute.
Application (File Zilla, WinSCP et al.) need not to run at execution.
