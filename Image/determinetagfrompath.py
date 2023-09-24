import argparse
import hashlib
import sys
import os

def hash_directory(paths):
    digest = hashlib.sha1()

    for path in paths:
        for root, dirs, files in os.walk(path):
            for names in files:
                file_path = os.path.join(root, names)

                digest.update(hashlib.sha1(file_path[len(path):].encode()).digest())

                if os.path.isfile(file_path):
                    with open(file_path, 'rb') as f_obj:
                        while True:
                            buf = f_obj.read(1024 * 1024)
                            if not buf:
                                break
                            digest.update(buf)
        digest.update(hashlib.sha1(digest.hexdigest().encode()).digest())

    return digest.hexdigest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
'''
Determines a hash of a given directory
''')
    parser.add_argument('-m', '--modulepath', 
        action='append', 
        help='The module path to calculate a hash for', 
        required=True,
        )

    args = parser.parse_args()    

    hash = hash_directory(args.modulepath)

    sys.stdout.write(hash)
    
    exit(0)