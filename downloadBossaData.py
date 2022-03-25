#import bibliotek python
import os
import wget
from zipfile import ZipFile


#adres http/https lokalizacji danych
url = 'https://info.bossa.pl/pub/omega/futures/omegafut.zip'
get_zip_file = (url.split("/")[-1:])
zip_file = (get_zip_file[0])

output_directory = "temp_download"

dir_path_file = os.path.dirname(os.path.realpath(__file__))
dir_path_directory = os.getcwd()

#zamiana \ na / problem z literowaniem folderów po systemem Windows
dir_path_directory = dir_path_directory.replace('\\', '/')

#Sprawdzenie czy folder pobierania danych istnieje, jeżeli nie to zostanie utworzony
output_directory_path = (f"{dir_path_directory}/{output_directory}")
output_directory_path_isExist = os.path.exists(output_directory_path)

if not output_directory_path_isExist:
    #Utworzenie katalogu jeżeli nie istnieje
    os.makedirs(output_directory_path)

#for file in os.listdir(dir_path_directory):
    #if file.endswith(".py"):
        #path = (os.path.join(dir_path_directory, file))
        #path = path.replace('\\', '/')
        #print(path)

file_name = output_directory_path + "/" + zip_file
print(file_name)
file_name_isExist = os.path.exists(file_name)
print(file_name_isExist)

#Czyszczenie folderu z poprzedniej wersji pobranego pliku
if output_directory_path_isExist:
    os.remove(file_name)

wget.download(url, out = output_directory)

#rozpakowanie i przegląd pliku FW20WS.txt
with ZipFile(file_name) as myzip:
    with myzip.open('FW20WS.txt') as myfile:
        print(myfile.read())