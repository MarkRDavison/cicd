import argparse
import sys
import os
import xml.etree.ElementTree as ET
import extractProjectVersion

def writeProjectVersion(csproj, version, existingVersion):
    tree = ET.parse(csproj)

    for element in tree.findall('.//PackageVersion'):

        if (not element.text == existingVersion):
            continue

        element.text = version
        ET.indent(tree, space="\t", level=0)
        tree.write(csproj, encoding="utf-8")
        return True

    return False

def iterateCsproj(rootPath, version):
    for root, dirs, files in os.walk(rootPath):
        for name in files:
            file_path = os.path.join(root, name)
            filename, file_extension = os.path.splitext(name)
            if (not file_extension == ".csproj"):
                continue
            
            existingVersion = extractProjectVersion.getProjectVersion(file_path)
            if (not existingVersion):
                continue
            
            if writeProjectVersion(file_path, version, existingVersion):
                print('Updated %s.csproj to %s from %s' % (filename, version, existingVersion))
            else:
                print('Failed to update %s.csproj' % filename)
                exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
'''
Sets the project version in all projects recursively to the given version
''')

    parser.add_argument('--projectDir', help='The root path to the project files', required=True)
    parser.add_argument('--version', help='The path to the csproj', required=True)

    args = parser.parse_args()

    iterateCsproj(args.projectDir, args.version)