import os,Image
def divide(path):
	file_name = 1
	for pic in os.listdir(path):
	    if pic.endswith(".gif"):
	        img = Image.open(path+pic)
	        for code_index in range(4): 
	            x = 11 + code_index * 9
	            y = 5
	            img.crop((x, y, x+9, y+11)).save("bina/%d.gif" % file_name) 
	            print "file_name=",file_name
	            file_name += 1

if __name__=='__main__':
    divide('./pic/')