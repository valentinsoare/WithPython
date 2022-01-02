#!/usr/bin/python

def main():
    list_of_names = [('Valentin', 'Soare'), ('Maria', 'Jones'), ('Eric', 'Clapton'), ('Carlos', 'Jones'), ('Queen', 'Jones')]
    list_of_jones = list(filter(lambda j: (j[0] == 'Jones' or j[1] == 'Jones'), list_of_names))

    print(f"{list_of_jones}")

main()