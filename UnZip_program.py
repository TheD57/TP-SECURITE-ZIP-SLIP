import zipfile
import os
import sys

def unzip_file(zip_file, extract_to):
    zipfile.ZipFile(zip_file, 'r').extractall(extract_to)

unzip_file(sys.argv[1], './')