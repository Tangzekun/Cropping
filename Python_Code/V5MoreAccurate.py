import urllib.request
import json
import urllib
from io import StringIO
from urllib import request
import io
from PIL import Image, ImageTk,ImageDraw
import os,sys
import mysql.connector
import base64


	
class Solution(object):
	
	
	db = mysql.connector.connect(user='', password='',
	host='',
	port = ,
	database ='')
	
	def readUrlToImage(self,url):
		#convert url to image
		outputName = url[-36:]
		fd = urllib.request.urlretrieve(url, outputName)
		#save image to desktop
		localImage = Image.open(outputName) 
		return outputName
		
		
		
		
	def leftTopAreaColor(self,localImage):

		#input an image, return the left top area's main color in RGB value

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
	def findEdges(self,imageName):
		
		leftX  = sys.maxsize
		rightX = -sys.maxsize 
		topY = sys.maxsize
		bottomY = -sys.maxsize 
		
		bgcol1,bgcol2,bgcol3 = self.leftTopAreaColor(localImage)
			
		img = Image.open("/Users/tangzekun/Desktop/Cropped/"+imageName)
		rgb_im = img.convert('RGB')
		imageScale = img.size
		
		for i in range(0,imageScale[0]):
			for j in range(0,imageScale[1]):
				(r, g, b) = rgb_im.getpixel((i, j))
				if r not in range(bgcol1-15,bgcol1+15)  and g not in range(bgcol2-15,bgcol2+15) and b not in range(bgcol3-15,bgcol3+15):
					
					leftX = min(leftX,i)
					rightX = max(rightX,i)
					topY = min(topY,j)
					bottomY = max(bottomY,j)
							
		#croppedImage = img.crop((leftX,topY,rightX,bottomY))
		
		edgedImage = ImageDraw.Draw(img)
		edgedImage.line((leftX,topY,rightX,topY),fill=128,width = 1)
		edgedImage.line((leftX,topY,leftX, bottomY),fill=128,width = 1)
		edgedImage.line((rightX,topY,rightX,bottomY),fill=128,width = 1)
		edgedImage.line((leftX,bottomY,rightX,bottomY),fill=128,width = 1)
		del edgedImage 
		#path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'Cropped.jpg'
		edgedpath = '/Users/tangzekun/Desktop/Cropped/'+localImage
		#croppedImage.save(path,'JPEG',quality = 95)
		img.save(edgedpath,'JPEG',quality = 95)
		#img.show()
		#return edgedpath	
		return edgedpath
		
		
		
	def cropEdges(self,localImage):
		
		leftX  = sys.maxsize
		rightX = -sys.maxsize 
		topY = sys.maxsize
		bottomY = -sys.maxsize 
		
		bgcol1,bgcol2,bgcol3 = self.leftTopAreaColor(localImage)
		
		zoomoutImage = self.zoomOut(localImage)	
		img = zoomoutImage
		rgb_im = img.convert('RGB')
		imageScale = img.size
		
		for i in range(0,imageScale[0]):
			for j in range(0,imageScale[1]):
				(r, g, b) = rgb_im.getpixel((i, j))
				if r not in range(bgcol1-15,bgcol1+15)  and g not in range(bgcol2-15,bgcol2+15) and b not in range(bgcol3-15,bgcol3+15):
					leftX = min(leftX,i)
					rightX = max(rightX,i)
					topY = min(topY,j)
					bottomY = max(bottomY,j)		
		croppedImage = img.crop((leftX,topY,rightX,bottomY))
		path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'Cropped.jpg'
		croppedImage.save(path,'JPEG',quality = 95)
		return path	
		
		
		
	def relateSample(self, croppedImage):
		
		
		model = Image.open(croppedImage)
		scale = model.size
		
		left = 0
		top = 0
		right = 0
		bottom = 0
		
		colorData = set()
		
		if scale[0] > 150 and scale[1]>150:
			left = scale[0]/2-15
			top = scale[1]/2-15
			right = scale[0]/2+15
			bottom = scale[1]/2+15
			
			
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
					
		return colorData


		
	def detectRelation(self, localImageName,croppedImage):
		
		model = Image.open("/Users/tangzekun/Desktop/Cropped/"+localImageName) # this is original image
		rgb_im = model.convert('RGB')
		scale = model.size
		sampleColorInfo = self.relateSample(croppedImage)
		os.remove(croppedImage)		
		
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
					
		linedImage = ImageDraw.Draw(model)
					
		#completely = model.crop((leftX,topY,rightX,bottomY))
		if (bottomY-topY) > int(scale[1]*0.90):
			topY += 80
			bottomY -= 50
			linedImage.line((leftX,topY,rightX,topY),fill=128,width = 1)
			linedImage.line((leftX,topY,leftX, bottomY),fill=128,width = 1)
			linedImage.line((rightX,topY,rightX,bottomY),fill=128,width = 1)
			linedImage.line((leftX,bottomY,rightX,bottomY),fill=128,width = 1)
		else:
			linedImage.line((leftX,topY,rightX,topY),fill=128,width = 1)
			linedImage.line((leftX,topY,leftX, bottomY),fill=128,width = 1)
			linedImage.line((rightX,topY,rightX,bottomY),fill=128,width = 1)
			linedImage.line((leftX,bottomY,rightX,bottomY),fill=128,width = 1)
			
		del linedImage
									
		#path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+"deep.jpg"
		path = '/Users/tangzekun/Desktop/Cropped/'+localImageName
		model.save(path,'JPEG',quality = 95)
		return path # change to this when want to run all code
		#return model
		
		
		
		
	def uploadToDB(self,linedImagePath):
		
		encoded_string= open(linedImagePath, 'rb')
		blob_value = base64.b64encode(encoded_string.read())
		sql = 'INSERT INTO Clothing(Picture_Storage) VALUES(%s)'
		args = (blob_value,)
		cursor=db.cursor()
		cursor.execute(sql,args)
		db.commit()
		#db.close()

	
#	def zoomIn(self,image):
#		img = Image.open(image)
#		basewidth = 400
#		wpercent = (basewidth/float(img.size[0]))
#		hsize = int((float(img.size[1])*float(wpercent)))
#		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
#		path = '/Users/tangzekun/Desktop/Cropped/'+localImage
#		img.save(path,'JPEG',quality = 95)
#		return img
		
	
db = mysql.connector.connect(user='', password='',
host='',
port = ,
database ='')





originalURL = "https://style.peekabuy.com/api/board/get_jc_product_images_batch/?page=3"
response = urllib.request.urlopen(originalURL)
content = response.read()
data = json.loads(content.decode("utf8"))


for clothingInfo in range(0,len(data["images"])):
	
	
	if data["images"][clothingInfo][2] == 2:
		test = Solution() 
		localImage = test.readUrlToImage(data["images"][clothingInfo][0])
		edgedImage = test.findEdges(localImage)
		test.uploadToDB(edgedImage)
	

	elif data["images"][clothingInfo][2] == 3:		
		test = Solution() 
		localImageName = test.readUrlToImage(data["images"][clothingInfo][0])
		croppedImage = test.cropEdges(localImageName)
		linedImage = test.detectRelation(localImageName,croppedImage)
		test.uploadToDB(linedImage)
db.close()
	


#test = Solution() 
#localImageName = test.readUrlToImage("https://peekabuy.s3.amazonaws.com/products/image/5cee7ef11c774396385a5030b5ef70b0.jpg")
#croppedImage = test.cropEdges(localImageName)
#linedImage = test.detectRelation(localImageName,croppedImage)



#test = Solution() 
#localImage = test.readUrlToImage("https://peekabuy.s3.amazonaws.com/products/image/22e68ff8fa654025d95c270b9dd1c42c.jpg")
#croppedImage = test.cropEdges(localImageName)
#linedImage = test.detectRelation(localImageName,croppedImage)












