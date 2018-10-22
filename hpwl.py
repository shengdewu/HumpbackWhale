from hpwl.ft_extract import ft_extract
from hpwl.predatap import predatap
import sys
import os

if '__main__' == __name__:
    print('start identify whale...' + sys.path.pop(0))
    pdp = predatap()
    pdp.parse_label('whale_image/train.csv')


    ft = ft_extract()

    for dir_path, dir_names, files in os.walk(top='./'):
        if -1 == dir_path.find('whale_image'):
            continue
        for file in files:
            if file.endswith('.jpg'):
                img_path = dir_path[2:] + '/' + file
                print(str('start process img {0}').format(img_path))
                ft.excetue(img_path)