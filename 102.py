import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx
#trocar a barras "\" para assim "/"
from_dir = "C:/Users/rafa/Downloads"  #pasta de origem         
to_dir = "C:/Users/rafa/Downloads"   #pasta de destino

list_of_files = os.listdir(from_dir)
print(list_of_files)


for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in ['.docx', '.txt']:

        path1 = from_dir + '/' + file_name      # Exemplo path1 : Downloads/nomeImagem1.jpg        
        path2 = to_dir + '/' + "Documentos"     # Exemplo path2 : D:/Meus Arquivos/Arquivos_Imagem      
        path3 = to_dir + '/' + "Documentos" + '/' + file_name # Exemplo path3 : D:/Meus Arquivos/Arquivos_Imagem/nomeImagem1.jpg
        print("path1 " , path1)
        print("path3 ", path3)

       
        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")

      
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
