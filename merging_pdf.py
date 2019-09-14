import PyPDF2
import os



merge = PyPDF2.PdfFileMerger()
filenames = os.listdir('w_m') #把想要合併的檔案放在「w_m」這個資料夾
filenames.sort()
print(filenames)
for file in filenames:
    print(file)
    if file.endswith('.pdf'):
        merge.append(PyPDF2.PdfFileReader(os.path.join('w_m', file)))
merge.write(os.path.join('result', 'be_merged.pdf'))



# import os
# path = "/Users/victorchiang/OneDrive/python/coding/pdf_project/w_m" #待讀取的資料夾
# path_list = os.listdir(path)
# path_list.sort() #對讀取的路徑進行排序
# for filename in path_list:
#     print(os.path.join(path, filename))

# 以上是讓PDF按照順序讀取的方法