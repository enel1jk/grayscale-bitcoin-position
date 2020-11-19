#%%
import os, re
import easyocr

def find_box(date):
    """
    不同样式的图片，目标文字的位置不同。
    样式乱七八糟的，艹。
    """
    return [(440, 510, 150, 165)] if 20181211<=date<=20181218 else\
        [(440, 510, 130, 145)] if 20191028<=date<=20191119 else\
        [(750, 870, 220, 245)] if date==20191017 else\
        \
        [(890, 1065, 105, 140)] if date<=20180329 else\
        [(925, 1080, 325, 360)] if date<=20190116 else \
        [(925, 1080, 310, 340)] if date<=20190208 else \
        [(925, 1080, 285, 315)] if date<=20190625 else \
        [(775, 900, 230, 255)] if date<=20191213 else \
        [(410, 530, 270, 300)]

reader = easyocr.Reader(['en'])
with open("aum.csv", 'a') as f:
    for entry in os.scandir('images'):
        date = entry.name.split('.')[0]
        box = find_box(int(date))
        result = reader.recognize(entry.path, box, [], detail=0, allowlist=set("0123456789.,$M"))
        aum = result[0].strip()
        # 修正部分识别错误
        aum = re.findall(r"\$(.+?)M", aum)[0]
        aum = aum.replace('.', '')
        aum = aum.replace(',', '')
        p_index = len(aum) - 1
        aum = aum[:p_index]+'.'+aum[p_index:]

        row = f"{date}\t{aum}" 
        f.write(row+"\n")
        print(f"{row}\t{box}")