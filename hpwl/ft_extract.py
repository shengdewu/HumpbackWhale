import cv2 as cv
import os

class ft_extract(object):

    def __init__(self):
        print('start feature extract ...')
        return

    def __imshow__(self, img_mat, name='name'):
        cv.namedWindow(name, cv.WINDOW_AUTOSIZE)
        cv.imshow(name, img_mat)
        cv.waitKey(0)
        return

    def excetue(self, path):
        '''
        :param path:  the relative path of image
        :return: the mat of feature
        '''
        abs_path = os.getcwd()[0:-4] + path
        img_mat = cv.imread(abs_path)

        self.__imshow__(img_mat, 'original')

        g_mat = cv.cvtColor(img_mat, cv.COLOR_BGR2GRAY)
        self.__imshow__(g_mat, 'gray img')

        b_mat = cv.threshold(g_mat, 0, 255, cv.THRESH_OTSU)
        self.__imshow__(b_mat, 'binary img')
        return
