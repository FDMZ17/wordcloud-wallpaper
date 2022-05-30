#!/usr/bin/env python3

import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)

mydir = "out"
check_folder = os.path.isdir(mydir)

inputFile=input("[?] Enter the words file path: ")
inputImage=input("[?] Enter the image file path: ")
outputImage=input("[?] Enter the output image file path: ")
f = open(inputFile, "r")
lines = f.read()

mask = np.array(Image.open(inputImage))
wordcloud = WordCloud(width=1920,height=1080,mask=mask,stopwords=stopwords,max_font_size=4000,max_words=10000,collocations=True).generate(lines)
f = plt.figure(figsize=(19.2,10.8))
f.subplots_adjust(0,0,1,1)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

if not check_folder:
    os.makedirs(mydir)
    print("Created folder: ", mydir)
    f.savefig("out/" + outputImage)

else:
    print("Saving to out folder...")
    f.savefig("out/" + outputImage)
