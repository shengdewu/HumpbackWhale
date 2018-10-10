from hpwl.ft_extract import ft_extract
import sys

if '__main__' == __name__:
    print('start identify whale...' + sys.path.pop(0))

    ft = ft_extract()

    ft.excetue('whale_image/train/0a0b2a01.jpg')