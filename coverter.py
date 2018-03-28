import argparse

READ_MODE = "r"

def fix_wrongly_encoded_data(data):
    try:
        return data.decode("cp1255").encode("utf8")

    except Exception as e:
        print "[-] Could not fix encoded subtitles."
        print "[-] Exception: %s", data
        return False

def write_to_file(path, data, mode="w+"):
    if "a" not in mode and "w" not in mode or "b" in mode:
        print "[-] The mode {0} is not valid.".format(mode)
        return False

    print "[+] Got valid mode {0}".format(mode)

    try:
        with open(path, mode) as f:
            f.write(data)

    except Exception as e:
        print "[-] Could not open file {0} in mode {1}".format(path, mode)
        print "[-] Exception: {0}".format(e)
        return False

    return True

def read_file(path):
    try:
        print "[+] Trying openning file %s", path
        with open(path, READ_MODE) as f:
            data = f.read()

    except Exception as e:
        print "[-] Could not open path %s", path
        print "[-] Exception: %s", e
        return False
    print "[+} Opened file %s successfully", path
    return data
