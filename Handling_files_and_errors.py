from pathlib import Path  
nowfile_directory = Path(__file__).resolve().parent
text_file_path = nowfile_directory / "forevercrush.txt"

File = open('forevercrush.txt', 'w')
File.write('I love chisom')
File.close( )

with open('forevercrush.txt', 'r') as File:
    data = File.read( )
    
modified_data = data.upper( )

with open('my_painful_wish.txt', 'w') as File:
    File.write(modified_data)

try:
    File = open('my_painful_wish.txt', 'r')
    data = File.read( )
    print(data)
except FileNotFoundError:
    print('File not found')
finally:
    File.close( )