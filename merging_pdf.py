import PyPDF2
import os
import time
# from progressbar import ProgressBar
from tqdm import tqdm

merge = PyPDF2.PdfFileMerger()
filenames = os.listdir('w_m') #把想要合併的檔案放在「w_m」這個資料夾
filenames.sort()
print(filenames)
for file in tqdm(filenames):
    if file.endswith('.pdf'):
        merge.append(PyPDF2.PdfFileReader(os.path.join('w_m', file)))

merge.write(os.path.join('result', 'be_merged.pdf'))
# 以上這個方法，沒辦法顯示出真正的執行進度



# with progressbar.ProgressBar(max_value=100) as bar:
#     for i in range(100):
#         time.sleep(0.1)
#         bar.update(i)
