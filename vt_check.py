#!/usr/bin/python3
import requests as req
import sys,re
template = 'https://www.virustotal.com/ui/search?query='
headers= {
"Host": "www.virustotal.com",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
"Accept": "application/json",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Referer": "https://www.virustotal.com/",
"content-type": "application/json",
"X-Tool": "vt-ui-main",
"x-app-version": "20200916t174337",
"Connection": "close",
"Cookie": "_ga=GA1.2.280690693.1600524091; _gid=GA1.2.191579739.1600524091; _gat=1"}
gui_link="https://www.virustotal.com/gui/search/"

print("\nStarting...")

try:
    if sys.argv[1] == "-f":
        with open(sys.argv[2]) as file_in:
            domains = [line.rstrip() for line in file_in]
            for i in domains:
                url = template+i
                r = req.get(url, headers=headers)
                response=r.text
            
                if r.status_code != 200:
                    print("Something went wrong\n")
                    print("Dump of JSON:\n\n {}".format(r.text))
                    sys.exit()
        
                #clean search
                pattern = r'category.*harmless'
                clean=re.findall(pattern,response)
                clean=len(clean)
                
                #malicious  search
                pattern = r'category.*malicious'
                malicious=re.findall(pattern,response)
                malicious=len(malicious)

                #suspicious search
                pattern = r'category.*suspicious'
                suspicious=re.findall(pattern,response)
                suspicious=len(suspicious)
            
                #undetected search
                pattern = r'category.*undetected'
                undetected=re.findall(pattern,response)
                undetected=len(undetected)
            
                #timeout search
                pattern = r'category.*timeout'
                timeout=re.findall(pattern,response)
                timeout=len(timeout)
            
                print("\n\033[1;37;40mResults for {}".format(i))
                print("-" * 12)
                print('\033[1;32;420mclean {}\n\033[1;31;40mmalicious {}\n\033[1;33;40msuspicious {}\n\033[0;37;40mundetected {}\n\033[0;35;40mtimeout {}'.format(clean,malicious,suspicious,undetected,timeout))
                if "http://" in i:
                    i=i.replace("http://","")
                if "https://" in i:
                    i=i.replace("https://","") 
                print("\n\033[1;37;40mreference at: \033[1;34;40m{}".format(str(gui_link+i)))
                print("\n")
        file_in.close()
        sys.exit()

    elif sys.argv[1] == "-i":
        for i in sys.argv[2:]:
            url = template+i
            r = req.get(url, headers=headers)
            response=r.text
            
            if r.status_code != 200:
                print("Something went wrong\n")
                print("Dump of JSON:\n\n {}".format(r.text))
                sys.exit()
        
            #clean search
            pattern = r'category.*harmless'
            clean=re.findall(pattern,response)
            clean=len(clean)
            
            #malicious  search
            pattern = r'category.*malicious'
            malicious=re.findall(pattern,response)
            malicious=len(malicious)
            
            #suspicious search
            pattern = r'category.*suspicious'
            suspicious=re.findall(pattern,response)
            suspicious=len(suspicious)
            
            #undetected search
            pattern = r'category.*undetected'
            undetected=re.findall(pattern,response)
            undetected=len(undetected)
            
            #timeout search
            pattern = r'category.*timeout'
            timeout=re.findall(pattern,response)
            timeout=len(timeout)
            
            print("\n\033[1;37;40mResults for {}".format(i))
            print("-" * 12)
            print('\033[1;32;420mclean {}\n\033[1;31;40mmalicious {}\n\033[1;33;40msuspicious {}\n\033[0;37;40mundetected {}\n\033[0;35;40mtimeout {}'.format(clean,malicious,suspicious,undetected,timeout))
            if "http://" in i:
                i=i.replace("http://","")
            if "https://" in i:
                i=i.replace("https://","")
            print("\n\033[1;37;40mreference at: \033[1;34;40m{}".format(str(gui_link+i)))
            print("\n")
        sys.exit()

    elif sys.argv[1] == "-h":
        print("\nVirusTotal Checker 1.0\n\nUsage: ./vt_check.py [mode] [input_type]")
        print("MODES:\n\t-h <no argument>: Displays help menu (this screen)\n\t-f <inputFilename>: Input domains/ip address from a text file\n\t-i <cmdline>: domains/ip address provided through cmdline seperated by space(s)")
        print("EXAMPLES:\n\t./vt_check.py -f domains.txt\n\t./vt_check.py -i domain1.com domain2.com\n")
        sys.exit()

except IndexError as err:
    print("\nERROR: {}".format(err))
    print("\nVirusTotal Checker 1.0\n\nUsage: ./vt_check.py [mode] [input_type]")
    print("MODES:\n\t-h <no argument>: Displays help menu (this screen)\n\t-f <inputFilename>: Input domains/ip address from a text file\n\t-i <cmdline>: domains/ip address provided through cmdline seperated by space(s)")
    print("EXAMPLES:\n\t./vt_check.py -f domains.txt\n\t./vt_check.py -i domain1.com domain2.com\n")

except Exception as err:
    print(err)
