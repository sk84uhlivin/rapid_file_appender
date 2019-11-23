import configparser
import glob
import time

config = configparser.ConfigParser()

try:
    config.read_file(open('settings.ini'))

except FileNotFoundError:
    input('No settings file found. Press any key to quit.')

files_folder = config.get('paths', 'files_folder')
fileout = config.get('paths', 'fileout')
time_interval = config.getfloat('settings', 'time_interval')
separator = config.get('settings', 'separator').replace('"',"")  # Removes "s from string.


print("")
print("rapid_file_appender by sk84uhlivin v0.1")
print("")

while True:
    file_path_list = glob.glob(f"{files_folder}*.txt")
    file_name_list = glob.glob1(files_folder, "*.txt")
    open(fileout, 'w').close   # Wipes output file before appending files.
    with open(fileout, "a") as outfile:
        for file in file_path_list[0:-1]:
            index = file_path_list.index(file)
            print(f"Appending {file_name_list[index]}...")
            with open(file, "r") as infile:
                outfile.write(infile.read())
            if separator != 'none':  # Adds the separator if requested.
                outfile.write(separator)
        for file in file_path_list[-1:]:
            print(f"Appending {file_name_list[-1]}...")
            with open(file, "r") as infile:
                outfile.write(infile.read())
    print("")
    print("Files appended! Cooling down for", time_interval, "seconds.")
    print("")
    time.sleep(time_interval)  # Program sleeps per requested amount of seconds.
