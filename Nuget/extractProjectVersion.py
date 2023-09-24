import argparse
import sys
import xml.etree.ElementTree as ET


def getProjectVersion(csproj):
    tree = ET.parse(csproj)

    for element in tree.findall('.//PackageVersion'):
        versionParts = element.text.split('.')

        if (len(versionParts) != 3):
            continue

        if (not versionParts[0].isdigit()):
            continue
        if (not versionParts[1].isdigit()):
            continue
        if (not versionParts[2].isdigit()):
            continue

        return element.text
    
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
'''
Retrieves the version from a csproj file
''')

    parser.add_argument('--csproj', help='The path to the csproj', required=True)

    args = parser.parse_args()
    version = getProjectVersion(args.csproj)
    if not version == None:
        sys.stdout.write(version)
        exit()

    exit(1)