import os
import sys

os.system('echo '+sys.argv[1]+' | hfst-lookup -q chvfinal.hfst | python3 l545_final_stress.py')