def fileLength(file_name):
    try:        
        file = open(file_name)
        contents = file.read()
        file.close()
        print(len(contents))
    except FileNotFoundError:
        
        
        
        
        
        
        
        
        
        
        
        
                   print("File {} not found.".format(file_name))