def load_image(panda):
    image = {"type":"",
         "comment":"",
         "size":[],
         "pixels":[]}
    
    file=open(panda,"r+")
    koala=file.read()
    file_content=koala.split('\n')
    print(file_content)
    image["type"]=file_content.pop(0)
    print(image)
    print(file_content)
    size=file_content.pop(0)
    size=[int(size[0]),int(size[1])]
    image["size"]
    print(image)
    print(file_content)

    file.close()
    return(image)
    
    
def save_image(image,wombat):
    file=open(wombat,"w+")
    file.write(image["type"])
    file.write(image["size"][0])
    file.write(image["size"][1])
    #file.write(image["pixels"]
    file.close()
    



ax=load_image("pliczek.pgm")
save_image(ax,"raz.pgm")

print(ax)

#file=open("pliczek.pgm","w+")
#file.write(image["type"])
#file.write(image["size"][0])
#file.write(image["size"][1])
#file.write(image["pixels"][0][0,1,2])
#file.close()


