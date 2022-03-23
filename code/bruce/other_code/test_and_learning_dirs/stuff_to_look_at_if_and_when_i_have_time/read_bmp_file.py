# ******************************* #
#   Try to read raw bitmap file   #
#          raster fileIO          #
#           Version: 0.0          #
#       Author: Bruce Stull       #
#            2022-01-18           #
# ******************************* #


def open_file_return_contents(file = r'.\two_circles.bmp', mode = 'r'):
    '''Accepts arguments of filename of file and file opening mode. Returns whole_text and lines (list).'''
    '''We don't necessarily need the whole text in one file, but I'm returning it in case it's needed.'''
    with open(file, mode) as file:
        # Retrieves the whole file-string.
        whole_text_of_file = file.read()
    return whole_text_of_file

# raster_string = open_file_return_contents()

# print(raster_string)


# https://discourse.mcneel.com/t/write-a-bitmap-pixel-by-pixel-in-python/81116/2
# import System.Drawing as sd

# csvData = []
# with open(r'.\two_circles.bmp','r') as file:
#     for line in file.readlines():
#         l = line.strip().split(';')
#         csvData.append(l)

# print(csvData)

# import System.Drawing 
# import math

# bmp = System.Drawing.Bitmap(Width,Height)

# for x in xrange(Height*Width):
#     #index = i + j*Width
#     j = int(math.floor(x/Width)) 
#     i = int(math.floor(x-(j*Width)))
#     col = Color[x]
#     bmp.SetPixel(i,j,col)
#     bmp.Save(PathWrite,System.Drawing.Imaging.ImageFormat.Bmp)