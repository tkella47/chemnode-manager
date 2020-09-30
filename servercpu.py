import json
import datetime
import sys
import getopt
class CpuMem:
    def __init__(self):
        self.scpu = {}
    def write_cpu_mem(self,cpu_dict):
        time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        file_obj = open("memtest.txt","w")
        json_obj = open("permcpu.json","w")
        file_obj.write(time)
        file_obj.write("\n")
        file_obj.write(json.dumps(cpu_dict))
        json_obj.write(json.dumps(cpu_dict))
        file_obj.close()
        json_obj.close()
    def read_cpu_mem(self):
        json_obj = open("permcpu.json")
        js_dict = json.load(json_obj)
        json_obj.close()
        print (js_dict)
        return js_dict
    def install_cpu_memory(self):
        cpu = {"16": "0"}
        self.write_cpu_mem(cpu)
def access(argv):
    opts, args = getopt.getopt(argv,'r:w:')
    for opt,arg in opts:
        if opt == '-r' and arg == "1":
            test = CpuMem()
            test.read_cpu_mem()
        elif opt == '-w' and arg == "1":
            test = CpuMem()
            test.write_cpu_mem(create_dict(args))
def create_dict(args):
    cpu_dict = {}
    for x in range(0,len(args)-1,2):
        cpu_dict[args[x]] = args[x+1]
    return cpu_dict
if __name__ == "__main__":
    access(sys.argv[1:])

    



