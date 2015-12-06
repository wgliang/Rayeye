import binarization

def walk_picture(path):
    for root, dirs, files in os.walk(path):
        #files
        for c_file in files:
            # index = c_file.find('.gif')
            # index = int(c_file[:index])
            # if index >4000 or index < 2000:
            #     continue
            f_path =  root + '/' + c_file;
            binarization.binariza(path)

