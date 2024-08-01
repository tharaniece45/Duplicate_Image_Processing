import os
import filecmp
 
Original_path = '/Cosmos/MyLearning/Duplicate_Image_Processing/Original'
print("Number of originals:",len(os.listdir(Original_path)))
list_of_images  = set()
for filename_i in os.listdir(Original_path):
    isFirstMatch = False
    file_i = os.path.join(Original_path, filename_i)
    print("+++++file_i+++++:",filename_i)
    if (filename_i.endswith('.png') or filename_i.endswith('.jpg')):
        for filename_j in os.listdir(Original_path):
            file_j = os.path.join(Original_path, filename_j)
            print("file_j:",filename_j)
            if (filename_j.endswith('.png') or filename_j.endswith('.jpg')):
                try:
                    if filecmp.cmp(file_i, file_j, shallow=False):
                        if isFirstMatch == False:
                            isFirstMatch = True
                        else:
                            print("{0} and {1} files are matching".format(filename_i,filename_j))
                            os.remove(file_j)
                            break
                         
                except:
                    print("Other error")

print("Final number of originals:",len(os.listdir(Original_path)))