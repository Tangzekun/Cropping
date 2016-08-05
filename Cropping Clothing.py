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
		
	
	def zoomOut(self,localImage):
		basewidth = 100
		img = Image.open(localImage)
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
		return img
		
		
		
	
	#find clean images objects' edges, and crop it
	def findEdges(self,zoomOutImage):
		
		leftX  = sys.maxsize
		rightX = -sys.maxsize 
		topY = sys.maxsize
		bottomY = -sys.maxsize 
		
		bgcol1,bgcol2,bgcol3 = self.leftTopAreaColor(localImage)
			
		img = zoomOutImage
		#img = Image.open(localImage)
		rgb_im = img.convert('RGB')
		imageScale = img.size
		
		for i in range(0,imageScale[0]):
			for j in range(0,imageScale[1]):
				(r, g, b) = rgb_im.getpixel((i, j))
				if r not in range(bgcol1-15,bgcol1+15)  and g not in range(bgcol2-15,bgcol2+15) and b not in range(bgcol3-15,bgcol3+15):
					leftX = min(leftX,i)
					#leftY = min(leftY,j)
					rightX = max(rightX,i)
					#rightY = max(rightY,j)
					#topX = min(topX,i)
					topY = min(topY,j)
					#bottomX = max(bottomX,i)
					bottomY = max(bottomY,j)
#		print("leftX: %d",leftX)
#		print("topY: %d",topY)
#		print("rightX: %d",rightX)
#		print("bottomY: %d",bottomY)		
		croppedImage = img.crop((leftX,topY,rightX,bottomY))
		path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'Cropped.jpg'
		croppedImage.save(path,'JPEG',quality = 95)
		return path		
		

	
	def zoomIn(self,croppedImage):
		img = Image.open(croppedImage)
		basewidth = 400
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
		path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'Cropped.jpg'
		img.save(path,'JPEG',quality = 95)
		return img
		
	
	
originalURL = "https://test.flaunt.peekabuy.com/api/board/get_jc_product_images_batch/?page=3"
response = urllib.request.urlopen(originalURL)
content = response.read()
data = json.loads(content.decode("utf8"))
for clothingInfo in range(0,len(data["images"])):
	if data["images"][clothingInfo][2] == 2:
		test = Solution() 
		localImage = test.readUrlToImage(data["images"][clothingInfo][0])
		zoomOutImage = test.zoomOut(localImage)
		croppedImage = test.findEdges(zoomOutImage)
		test.zoomIn(croppedImage)
		
	
#url = "https://peekabuy.s3.amazonaws.com/products/image/7b8e4beb6b6591e4f69e02cb38235569.jpg"
#url = "https://peekabuy.s3.amazonaws.com/products/image/8281cb2e07b34c2692249671de811508.jpg"
#url = "https://peekabuy.s3.amazonaws.com/products/image/69993f3a85c113bece40344b33f9a3de.jpg"
#url = "https://peekabuy.s3.amazonaws.com/products/image/ec71d52091c29b3f60241c42ea0f4d52.jpg"
#url = "https://peekabuy.s3.amazonaws.com/products/image/e8304e33f415f09dfc8dd4c65c0e4a65.jpg"



#test = Solution() 
#localImage = test.readUrlToImage(url)
#zoomOutImage = test.zoomOut(localImage)
#major1,major2,major3 = test.leftTopAreaColor(localImage)	
#croppedImage = test.findEdges(zoomOutImage)
#test.zoomIn(croppedImage)
	
	
	
	
	
	
	
	
	