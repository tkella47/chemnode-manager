import json
import datetime
import sys
import getopt
#reads the current memory, merges new keys/values,overwrites the old file
#server_assignments stored as file_name:[node#,PID,recovery_path]
def write_server_assign(server_assign_dict):
    json_obj = open("permsersign.json")
    js_dict = json.load(json_obj)
    json_obj.close()
    for tup in server_assign_dict.items():
        if tup[0] not in js_dict:
            js_dict[tup[0]] = tup[1]
    json_obj = open("permsersign.json","w")
    json_obj.write(json.dumps(js_dict))
    json_obj.close()
#removes any number of keys/values from server_memory, then  recommits to memory
def remove_server_assign(remove_list):
    json_obj = open("permsersign.json")
    js_dict = json.load(json_obj)
    json_obj.close()
    for item in remove_list:
        del js_dict[item]
    json_obj = open("permsersign.json","w")
    json_obj.write(json.dumps(js_dict))
    json_obj.close()
#reads server memory, then prints to command line (info is then processed client side)
def read_server_assign():
    json_obj = open("permsersign.json")
    try: 
        js_dict = json.load(json_obj)
    except Exception:
        js_dict ={}
    finally:
        json_obj.close()
        if len(js_dict) == 0:
            print("EMPTY")
        else:
            print (js_dict)
    return js_dict
#easily installs the memory file along with dummy parameter 
def install_server_assign():
    json_obj = open("permsersign.json","w")
    json_obj.write(json.dumps({"install": ["23","9999999","/home/student/pyDone"]}))
    json_obj.close()
#clears assignment memory from server_side memory (may not be used in the end)
def clear_server_assign():
    json_obj = open("permsersign.json", "w")
    json_obj.close()
#access portal (with arguments coming from command line)
#can read (r), write(w), clear(c), remove(x) and install (all opts passed as 0)
#parameters, -r(0|1) -w(0|1 see for args) -c(0|1) -x(0|1 see for args)
#only one option can be passed at a time
# -w 1 requires additional arguments in the form "file_name node_number PID path" per file_name desired to be written
# default path is "/home/student/pyDone", and is passed in as 0
# -x 1 requires additional arguments in the form "file_name" per file_name desired to be removed (separate with spaces)

def access(argv):
    opts, args = getopt.getopt(argv,'r:w:c:x:')
    install = True
    for opt,arg in opts:
        if opt == "-r" and arg == "1":
            read_server_assign()
            install = False
            break
        if opt == "-c" and arg == "1":
            clear_server_assign()
            install = False
            break
        if opt == "-w" and arg == "1":
            write_server_assign(pre_write(args))
            install = False
            break
        if opt == "-x" and arg == "1":
            remove_server_assign(pre_remove(args))
            install = False
            break
    if install:
        install_server_assign()
    return
#takes input from command line and parses into a dictionary
def pre_write(args):
    server_dict = {}
    for x in range(0,len(args)-3,4):
        if args[x+3] == "0":
            server_dict[args[x]] = [args[x+1],args[x+2],"/home/student/pyDone"]
        else:
            server_dict[args[x]] = [args[x+1],args[x+2],args[x+3]]
    return server_dict
#takes input from command line and parses into a list
def pre_remove(args):
    remove_list = []
    for node in args:
        remove_list.append(node)
    return remove_list
if __name__ == "__main__":
    access(sys.argv[1:])





