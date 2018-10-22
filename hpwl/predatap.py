import pandas as pd
from collections import Counter
import os
import matplotlib.pyplot as plt

class predatap(object):

    def parse_label(self, path):
        abs_path = os.getcwd() + '/' + path
        labeles = pd.read_csv(filepath_or_buffer=abs_path)

        rand_rows = labeles.sample(frac=1.)[:20]

        num_cat = len(labeles['Id'].unique())
        print(f'Number of categories:{num_cat}')

        conut = labeles['Id'].value_counts().values
        size_buckets = Counter(conut)

        plt.figure(figsize=(10, 6))
        plt.bar(range(len(size_buckets)), list(size_buckets.values())[::-1])
        plt.xticks(range(len(size_buckets)), list(size_buckets.keys())[::-1])
        plt.show()

        return

    def agment_img(self):
        return