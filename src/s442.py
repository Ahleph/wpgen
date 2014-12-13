from PIL import Image
import math
import time

def main():
  picture = Image.open("new.png")
  pic = picture.load()
  width, height = picture.size
  pic = HypReflect(picture, pic, width, height)
  BuildS442WallPaper(pic, width*2, height*2, 1600)

## Take top half triangle and copy it over the hypotenuse. gives one reflection:
## Specifically, the reflection of order 2
def HypReflect(picture, pic, width, height):
  for i in range(height):
    for j in range(width - i):
        pic[width-i-1, height-j-1] = pic[j,i]

  picture.save("new2.png")
  return Image.open("new2.png").load()


def BuildS442WallPaper(pic, width, height, maxdim):
  while (width < maxdim and height < maxdim):
      newim, width, height = DoubleWallpaperSize(pic, width, height)
  return

## Copies the fundamental region, reflecting it over itself twice:
## Once vertically, once horizontally. This doubles the size of the wallpaper
def DoubleWallpaperSize(pic, width, height):
## Multiply length and width by 2, then reflect horizontally and vertically
  newim = Image.new("RGB", (width, height), "white")
  newimg = newim.load()
  im = Image.open("new2.png")
  img = im.load()
  for i in range(int(height/2)):
    for j in range(int(width/2)):
      newimg[i,j] = img[i,j]
  newim = HorizontalReflect(newim, newimg, width, height)
  newimg = newim.load()
  newim = VerticalReflect(newim, newimg, width, height)
  return (newim, width * 2, height * 2)

def HorizontalReflect(picture, pic, width, height):
  for i in range(height - 1):
      for j in range(int(width/2 - 1)):
          pic[width - j - 1, i] = pic[j, i]
  picture.save("new2.png")
  return Image.open("new2.png")

def VerticalReflect(picture, pic, width, height):
  for i in range(int(height/2 - 1)):
      for j in range(width - 1):
          pic[j , height - i - 1] = pic[j, i]
  picture.save("new2.png")

  return Image.open("new2.png")

if __name__ == "__main__":
  main()
