import argparse
import Tkinter as tk
from tkFileDialog import askopenfilename, asksaveasfilename

import sys

READ_MODE = "r"

def fix_wrongly_encoded_data(data):
    """
        This method receive wrongly encoded data and fix it to be
        appeared as Hebrew.

    :param data: (string) The data to fix.
    :return: (string) The fixed data.
             (bool) False is returned if the function failed.
    """

    # Trying to fix the encoding of the Gibbrish data.
    try:
        return data.decode("cp1255").encode("utf8")

    # If did not succeed, printing errors and returning False.
    except Exception as e:
        print "[-] Could not fix encoded subtitles."
        print "[-] Exception: %s", data
        return False

def write_to_file(path, data, mode="w+"):
    """
        This method receiving a path of a file and a data to write to the file.
        It can also receive the mode to write with, default is "w+".

    :param path: (string) The path of the file we are writing to.
    :param data: (string) The data we are writing to the file.
    :param mode: (string) The mode we are writing with. Default is "w+".
    :return: (bool) True if succeed, False if failed.
    """
    # Checking if it contains a mode that allows writing/appending.
    if "a" not in mode and "w" not in mode:
        print "[-] The mode {0} is not valid.".format(mode)
        return False

    print "[+] Got valid mode {0}".format(mode)

    # Trying to open the file and write the data into it.
    try:
        with open(path, mode) as f:
            f.write(data)

    # If not succeed, printing errors and return False.
    except Exception as e:
        print "[-] Could not open file {0} in mode {1}".format(path, mode)
        print "[-] Exception: {0}".format(e)
        return False

    return True

def read_file(path, binary=False):
    """
        This method receive a file and returns its content. If binary is Trus
        the file is being read in binary mode.

    :param path: (string) The path to the file to read.
    :param binary: (bool) True to read the file in binary mode, False to not.
    :return: (bool) False is returned if a failure accures.
             (string) The data is returned on success.
    """

    # Trying to open the file and read it into data.
    try:
        print "[+] Trying openning file %s", path
        with open(path, READ_MODE if not binary else READ_MODE + 'b') as f:
            data = f.read()

    # If not succeed, printing errors and returning False.
    except Exception as e:
        print "[-] Could not open path %s", path
        print "[-] Exception: %s", e
        return False

    # Returning the data read from file.
    print "[+} Opened file %s successfully", path
    return data

def get_path_from_user(input):
    """
        This method gets a path from the user using Tkinter windows and returns it.
        It chooses the window type to pop according to the input variable - True for
        askopenfilename(), False for asksaveasfilename().

    :param input: (bool) True for using askopenfilename(), False for using asksaveasfilename()
    :return: (string) The path we received from the user.
    """

    # Initialization of a Tkinter instance.
    root = tk.Tk()

    # Show askopenfilename dialog without the Tkinter window
    root.withdraw()

    # Get existing path if input=True, else get non existing path.
    file_name = askopenfilename() if input else asksaveasfilename()

    return file_name

def main(argc, argv):
    parser = argparse.ArgumentParser(description="This script fixes wrong encoded subtitles.")
    parser.add_argument("-i", "--input", help="Input file (wrong encoded).", required=False)
    parser.add_argument("-o", "--output", help="Output file path. The path of the new subtitles file.", required=False)
    args = parser.parse_args()

    # If got no parameters, use Tkinter to get the paths from the user.
    input_path = args.input if args.input else get_path_from_user(True)
    output_path = args.output if args.output else get_path_from_user(False)

    # If one of the paths are empty, exit the program.
    if not input_path or not output_path:
        print "[-] Missing a input/output path. Exiting..."
        return 1

    # Read the data to fix and make sure the function succeed. Else, exit the program.
    data_to_fix = read_file(input_path)
    if not data_to_fix:
        print "[-] data_to_fix was not read successfully."
        return 1

    print "[+] Successfully read the broken data from file %s. Len: %d", input_path, len(data_to_fix)

    # Fix the data and make sure the fixing method succeed, else exit the program.
    fixed_data = fix_wrongly_encoded_data(data_to_fix)
    if not fixed_data:
        print "[-] Data could not be fixed successfully."
        return 1

    print "[+] Sucessfully fixed data. Len: %d", len(fixed_data)

    # Writing the fixed data to the output path, making sure the function succeed, else exiting.
    if not write_to_file(output_path, fixed_data):
        print "[-] Could not write fixed data to file successfully."
        return 1

    print "[+] Successfully wrote the fixed data to file %s. Len: %d", output_path, len(fixed_data)
    return 0

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)