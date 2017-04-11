from PIL import Image
import os
import subprocess


def image_to_string(img, cleanup=True, plus='-l num1 -psm 7'):

    subprocess.check_call('tesseract ' + img + ' ' +
                          img + ' ' + plus, shell=True)
    text = ''
    with open(img + '.txt', 'r') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(img + '.txt')
    return text


def get_yzm(Firstpath):
    img = Image.open(Firstpath)
    img = img.convert('L')
    img = img.point(lambda x: 0 if x < 190 else 255)
    img_ads = Firstpath + ".threshold.jpg"
    img.save(img_ads)
    text = str(image_to_string(img_ads))
    text = text[-4:]
    return text


# for i in xrange(9, 100):
#     path = '/home/drafff/p/' + str(i) + '.jpg'
#     img = Image.open(path)
#     img.save('/home/drafff/p/p/' + str(i) + '.jpg')
#     img = img.convert('L')
#     img = img.point(lambda x: 0 if x < 190 else 255)
#     img.save('/home/drafff/p/p/' + str(i) + '.jpg')
#     img_ads = '/home/drafff/p/p/' + str(i) + '.jpg'
#     text = str(image_to_string(img_ads))
#     text = text[-4:]
#     print 'No.' + str(i) + ': ' + text
