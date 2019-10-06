import xlrd
import os
from bs4 import BeautifulSoup
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import pandas as pd

feedback = xlrd.open_workbook(r'withinStory.xlsx') # use the file name of your sheet
#print(feedback.sheet_names())

content1 = feedback.sheet_by_index(0)
result = content1.col_values(0)

allText = ""

for i in result:
    allText = allText + str(i)

words = jieba.cut(allText)
print("Full Mode: " + "/ ".join(words))

# set stopwords
stopwords = {}.fromkeys(["也","但","的","和","是","有"])

# need to add wordcloud function