import os , sys

def main():
        s = open(sys.argv[3], 'w')
        for m in os.listdir(sys.argv[2]):
                mpath = os.path.join(sys.argv[2], m)
                strm = open(mpath).read()
                sig = strm[0:89]
                s.write(sig)
                s.write("\n")
        s.close()

main()
