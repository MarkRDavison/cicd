import argparse
import ruamel.yaml

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
'''
Replaces a value in a yaml file
''')
    parser.add_argument('-f', '--file', help='The yaml file to modify', required=True)
    parser.add_argument('-n', '--name', help='The name of the value to set', required=True)
    parser.add_argument('-v', '--value', help='The value to set', required=True)

    args = parser.parse_args()    

    yaml = ruamel.yaml.YAML()

    with open(args.file, "r") as stream:
        try:
            yaml.indent(mapping=2, sequence=2, offset=2)
            yaml.preserve_quotes = True
            yaml.compact(seq_seq=False, seq_map=False)
            data = yaml.load(stream)
            
            y = data

            nameElements = args.name.split('.')
            for el in nameElements[:-1]:
                y = y[el]

            y[nameElements[-1]] = args.value
        except:
            exit(1)

    with open(args.file, "w") as stream:
        yaml.dump(data, stream)
    
    exit(0)