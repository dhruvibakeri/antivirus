import os, sys, os.path

def main():
        sigs = []
        ans = 0
        ansd = 0
        s = open(sys.argv[1], 'r')
        for line in s:
                sigs.append(line.strip())
        for f in sys.argv[2:]:
                if os.path.isdir(f):
                        for fn in os.listdir(f):
                                ansd = 0
                                fpath = os.path.join(f,fn)
                                fd = open(fpath).read()
                                for xd in sigs:
                                        ansd += fd.find(xd)
                                if (ansd == (len(sigs) * -1)):
                                        print fn + ": SAFE"
                                else:
                                        print fn + ": MALWARE"
                else:
                        ans = 0
                        ff = open(f).read()
                        for x in sigs:
                                ans += ff.find(x)
                        if (ans == (len(sigs) * -1)):
                                print f + ": SAFE"
                        else:
                                print f + ": MALWARE"

main()
