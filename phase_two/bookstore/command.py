import sys 
from app import sort_names_list, names_encoder


def main():     
    arguments = sys.argv[1:]  # Skip the first element (script name)         print("Command-line arguments:")     for arg in arguments:         print(arg)
    print(names_encoder(sort_names_list(names_decoder(arguments))))

def names_decoder(names_list):
    names_no_spaces = [name.strip() for name in names_list]
    return names_no_spaces

if __name__ == '__main__':     
    main()
