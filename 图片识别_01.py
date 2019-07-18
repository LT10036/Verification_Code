
#-------------------------------------------------------------------------------------------------------------------------
#
# 修 改  pytesseract  文 件 中 的 tesseract_cmd 地 址 为：c://Program Files (x86)//Tesseract-OCR//tesseract.exe
# 初 级 版 本 识 别 数字 验 证 码
# 发 现 0 o 不 分 ，9 g 不 分 ，不 分 清 楚 能 个 别 数 字 和 字 母
#
# ------------------------------------------------------------------------------------------------------------------------


from PIL import Image
import pytesseract


# 设置语言包目录 必须加上这句，暂时没解决根本起因
tessdata_dir_config = '--tessdata-dir "c://Program Files (x86)//Tesseract-OCR//tessdata"'

# 空白列表接收单个字符
a=[]

# 打开图片，并解析
l=Image.open('D://Documents//Downloads//123.bmp')
# 识别汉字
# text = pytesseract.image_to_string(l,lang='chi_sim',config=tessdata_dir_config)
# 识别英文
text = pytesseract.image_to_string(l,lang='eng',config=tessdata_dir_config)

# 解析出来的文本有空格字符，需要解析下
for i in text:
    if i !=" ":
        a.append(i)
print(a)
