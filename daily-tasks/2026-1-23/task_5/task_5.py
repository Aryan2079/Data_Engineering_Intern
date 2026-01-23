# task 5: Write a program to copy the contents of one file to another.

def copy_contents(source_file_path, destination_file_path):
    with open(source_file_path, 'r', encoding='utf-8') as sf:
        with open(destination_file_path, 'w', encoding='utf-8') as df:
            df.write(sf.read())

copy_contents('source.txt', 'destination.txt')