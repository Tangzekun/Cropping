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
			
		im = Image.open(localImage)
		rgb_im = im.convert('RGB')
		imageScale = im.size
		
		for i in range(0,imageScale[0]):
			for j in range(0,imageScale[1]):
				(r, g, b) = rgb_im.getpixel((i, j))
				#if (r != bgcol1 and g != bgcol2) or (b != bgcol3 and r != bgcol1) or (b != bgcol3 and g != bgcol2):
				if r not in range(bgcol1-20,bgcol1+20)  and g not in range(bgcol2-20,bgcol2+20) and b not in range(bgcol3-20,bgcol3+20):
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
		cropedImage = im.crop((leftX,topY,rightX,bottomY))
		path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'Cropped.jpg'
		cropedImage.save(path,'JPEG')
		#cropedImage.show()
		return path		
		


	def relateSample(self, croppedImage):
		
		model = Image.open(croppedImage)
		scale = model.size
		
		left = 0
		top = 0
		right = 0
		bottom = 0
		
		colorData = set()
		
		if scale[0] > 200 and scale[1]>200:
			left = scale[0]/2-25
			top = scale[1]/2-25
			right = scale[0]/2+25
			bottom = scale[1]/2+25
			
			left2 = scale[0]/2-25
			top2 = scale[1]/2-100
			right2 = scale[0]/2+25
			bottom2 = scale[1]/2-50
			
			left3 = scale[0]/2-25
			top3 = scale[1]/2+75
			right3 = scale[0]/2+25
			bottom3 = scale[1]/2+100
			
			'''
			sample2 = model.crop((left2,top2,right2,bottom2))
			sampleSize2 = sample2.size
			rgb_sample2 = sample2.convert('RGB')
			
			for x in range(sampleSize2[0]):
				for y in range(sampleSize2[1]):
					(r,g,b) = rgb_sample2.getpixel((x, y))	
					colorData.add((r,g,b))				
					tempR = r
					tempG = g
					tempB = b
					for t in range(10):
						r += 1
						colorData.add((r,g,b))
					for z in range(10):
						r = tempR
						g += 1
						colorData.add((r,g,b))
					for k in range(10):
						r = tempR
						g = tempG
						b += 1
						colorData.add((r,g,b))
			
			
			
			sample3 = model.crop((left3,top3,right3,bottom3))
			sampleSize3 = sample3.size
			rgb_sample3 = sample3.convert('RGB')
			
			
			for x in range(sampleSize3[0]):
				for y in range(sampleSize3[1]):
					(r,g,b) = rgb_sample3.getpixel((x, y))
					colorData.add((r,g,b))
					tempR = r
					tempG = g
					tempB = b
					for t in range(10):
						r += 1
						colorData.add((r,g,b))
					for z in range(10):
						r = tempR
						g += 1
						colorData.add((r,g,b))
					for k in range(10):
						r = tempR
						g = tempG
						b += 1
						colorData.add((r,g,b))
		'''	
			
		else:
			left = scale[0]/2-10
			top = scale[1]/2-10
			right = scale[0]/2+10
			bottom = scale[1]/2+10
			
		sample = model.crop((left,top,right,bottom))
		sampleSize = sample.size
		rgb_sample = sample.convert('RGB')
		
		
		for x in range(sampleSize[0]):
			for y in range(sampleSize[1]):
				(r,g,b) = rgb_sample.getpixel((x, y))
				colorData.add((r,g,b))
				tempR = r
				tempG = g
				tempB = b
#				for t in range(10):
#					r += 1
#					colorData.add((r,g,b))
#				for z in range(10):
#					r = tempR
#					g += 1
#					colorData.add((r,g,b))
#				for k in range(10):
#					r = tempR
#					g = tempG
#					b += 1
#					colorData.add((r,g,b))
					
		return colorData


	
	def detectRelation(self, croppedImage):
		
		model = Image.open(croppedImage)
		rgb_im = model.convert('RGB')
		scale = model.size
		sampleColorInfo = self.relateSample(croppedImage)
				
		
		leftX  = sys.maxsize
		rightX = -sys.maxsize
		topY = sys.maxsize
		bottomY = -sys.maxsize
		
		
		for i in range(0,scale[0]):
			for j in range(0,scale[1]):
				color = rgb_im.getpixel((i, j))
				if color in sampleColorInfo:
					
					leftX = min(leftX,i)
					rightX = max(rightX,i)
					topY = min(topY,j)
					bottomY = max(bottomY,j)

		completely = model.crop((leftX,topY,rightX,bottomY))		
		path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'Cropped.jpg'
		completely.save(path,'JPEG')
		return path

				
				
				
				
			
	
		


#url = "https://peekabuy.s3.amazonaws.com/products/image/415af9b4ec984e929268c2c5288d9e4d.jpg"
#url = "https://peekabuy.s3.amazonaws.com/products/image/f435b4317bf4a5c7c13e249c9dca1571.jpg"
#url = "https://peekabuy.s3.amazonaws.com/products/image/e8304e33f415f09dfc8dd4c65c0e4a65.jpg"
url = "https://peekabuy.s3.amazonaws.com/products/image/5100ae9b5cb0e83efe089645dfc3c58c.jpg"
#url = "https://peekabuy.s3.amazonaws.com/products/image/059e3eb786abfdab670db39d3ff53925.jpg"
#url = "https://peekabuy.s3.amazonaws.com/products/image/d9a4d815d68325aee748a82856017a50.jpg"




test = Solution() 
localImage = test.readUrlToImage(url)
major1,major2,major3 = test.leftTopAreaColor(localImage)
print(major1,major2,major3)	
croppedImage = test.findEdges(localImage)
test.detectRelation(croppedImage)








