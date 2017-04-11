# import os
# import subprocess


# def image_to_string(img, cleanup=True, plus='-l num1 -psm 7'):

#     subprocess.check_call('tesseract ' + img + ' ' +
#                           img + ' ' + plus, shell=True)
#     text = ''
#     with open(img + '.txt', 'r') as f:
#         text = f.read().strip()
#     if cleanup:
#         os.remove(img + '.txt')
#     return text
