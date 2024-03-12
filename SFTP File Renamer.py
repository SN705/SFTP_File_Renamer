"""
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
"""
import paramiko

# Establish an SFTP connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("canfts02.dayforcehcm.com", username="brewsters", password="692VxaWmN9hCxJ")

# Open an SFTP session
sftp = ssh.open_sftp()

# Set the directory path
directory = "/Import/KPIImport"

# List the files in the directory
files = sftp.listdir(directory)

# Rename each .csv file in the directory
for file in files:
    if file.endswith(".csv"):
        source_path = directory + "/" + file
        destination_path = directory + "/" + file[:-4] + ".csv.ready"
        
        try:
            # Check if the source file exists
            sftp.stat(source_path)
        except FileNotFoundError:
            print(f"Error: File '{source_path}' does not exist. Skipping rename.")
            continue
        
        try:
            # Rename the file
            sftp.rename(source_path, destination_path)
            print(f"Renamed '{source_path}' to '{destination_path}'.")
        except Exception as e:
            print(f"Error renaming '{source_path}': {str(e)}")

# Close the SFTP session and SSH connection
sftp.close()
ssh.close()

print("Success. Script executed without error.")
