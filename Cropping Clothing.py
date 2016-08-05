import urllib.request
import json
import urllib
from io import StringIO
from urllib import request
import io
from PIL import Image, ImageTk
import sys


	
class Solution(object):




	def readUrlToImage(self,url):
		#convert url to image
		outputName = url[-36:]
		fd = urllib.request.urlretrieve(url, outputName)
		#save image to desktop
		localImage = Image.open(outputName) 
		return outputName
		
		
		
	def leftTopAreaColor(self,localImage):
		'''
		input an image, return the left top area's main color in RGB value
		
		'''
		#a dict to track the major color
		maximum = 0
		major1,major2,major3 = 0,0,0
		RGBCount = dict()
		im = Image.open(localImage)
		#convert image to RGB value
		rgb_im = im.convert('RGB')
		#get the image size as tuple
		#1st is width
		#2nd is length
		imageScale = im.size
		for i in range(0,int(imageScale[0]/10)):
			for j in range(0,int(imageScale[1]/10)):
				(r, g, b) = rgb_im.getpixel((i, j))
				if (r,g,b) in RGBCount:
					RGBCount[r,g,b] += 1
					if RGBCount[r,g,b] > (i*j/2):
						return r,g,b
				else:
					RGBCount[r,g,b] = 1
					
		for key in RGBCount.keys():
			maximum = max(maximum,RGBCount[key])
			if maximum == RGBCount[key]:
				major1,major2,major3 = key
		return major1,major2,major3
		
		
		
		
	
	#find clean images objects' edges, and crop it
	def findEdges(self,localImage):
		
		leftX,leftY  = sys.maxsize,sys.maxsize
		rightX,rightY = -sys.maxsize ,-sys.maxsize
		topX,topY = sys.maxsize,sys.maxsize
		bottomX,bottomY = -sys.maxsize,-sys.maxsize 
		
		bgcol1,bgcol2,bgcol3 = self.leftTopAreaColor(localImage)
			
		img = Image.open(localImage)
		rgb_im = img.convert('RGB')
		imageScale = img.size
		
		for i in range(0,imageScale[0]):
			for j in range(0,imageScale[1]):
				(r, g, b) = rgb_im.getpixel((i, j))
				#if (r != bgcol1 and g != bgcol2) or (b != bgcol3 and r != bgcol1) or (b != bgcol3 and g != bgcol2):	

				if r not in range(bgcol1-15,bgcol1+15)  and g not in range(bgcol2-15,bgcol2+15) and b not in range(bgcol3-15,bgcol3+15):
					leftX = min(leftX,i)
					#leftY = min(leftY,j)
					rightX = max(rightX,i)
					#rightY = max(rightY,j)
					#topX = min(topX,i)
					topY = min(topY,j)
					#bottomX = max(bottomX,i)
					bottomY = max(bottomY,j)
		print("leftX: %d",leftX)
		print("topY: %d",topY)
		print("rightX: %d",rightX)
		print("bottomY: %d",bottomY)		
		cropedImage = img.crop((leftX,topY,rightX,bottomY))
		path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'Cropped.jpg'
		cropedImage.save(path,'JPEG')
		#cropedImage.show()
		return cropedImage		
		
		
	
	
	
	
	
	
#originalURL = "https://test.flaunt.peekabuy.com/api/board/get_jc_product_images_batch/?page=0"
#response = urllib.request.urlopen(originalURL)
#content = response.read()
#data = json.loads(content.decode("utf8"))
#
#for clothingInfo in range(0,len(data["images"])):
#	waitingEditing = readUrlToImage(clothingInfo[0])	
		
	
url = "https://peekabuy.s3.amazonaws.com/products/image/f435b4317bf4a5c7c13e249c9dca1571.jpg"
test = Solution() 
localImage = test.readUrlToImage(url)
major1,major2,major3 = test.leftTopAreaColor(localImage)
print(major1,major2,major3)
print()	
test.findEdges(localImage)
	
	
	
	
	
	
	
	
	