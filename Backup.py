
		def detectSkin(self, croppedImage): # RGB
				
			bgcol1,bgcol2,bgcol3 = self.leftTopAreaColor(localImage)
			model = Image.open(croppedImage)
			rgb_im = model.convert('RGB')
			imageScale = model.size
			skinArea = [[0]*imageScale[0]]*imageScale[1] # 0: not skin, 1:may skin, 2: skin
			
			for i in range(0,imageScale[1]):
				for j in range(0,imageScale[0]):
					(r, g, b) = rgb_im.getpixel((j, i))
					#if r > 95 and g > 40 and g < 100 and b > 20 and max([r, g, b]) - min([r, g, b]) > 15 and abs(r - g) > 15 and r > g and r > b:
					if r>95 and g>60 and b>30 and r>g and r>b and max(r,g,b)-min(r,g,b)>15 and abs(r-g)>15: 

						skinArea[i][j] = 1
						#self.checkArounSkin(skinArea,i,j) 
			
			for i in range(0,imageScale[1]):
				for j in range(0,imageScale[0]):
					#if skinArea[i][j]==2:
					if skinArea[i][j]==1:
						new_color = (bgcol1,bgcol2,bgcol3)
						model.putpixel((j,i), new_color)
			path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'CroppedCompletely.jpg'
			model.save(path,'JPEG')
			return model
				



		
		def detectSkin(self, croppedImage): #ycbcr
			
			bgcol1,bgcol2,bgcol3 = self.leftTopAreaColor(localImage)
			model = Image.open(croppedImage)
			ycc_im = model.convert('YCbCr')
			imageScale = model.size
			skinArea = [[0]*imageScale[0]]*imageScale[1] # 0: not skin, 1:may skin, 2: skin
			
			for i in range(0,imageScale[1]):
				for j in range(0,imageScale[0]):
					(y,cb,cr) = ycc_im.getpixel((j, i))
					if 80 <= cb <= 120 and 130 <= cr <= 170 and 80<y:
						skinArea[i][j] = 1
						#self.checkArounSkin(skinArea,i,j) 
						
			
			for i in range(0,imageScale[1]):
				for j in range(0,imageScale[0]):
					#if skinArea[i][j]==2:
					if skinArea[i][j] == 1:
						new_color = (bgcol1,bgcol2,bgcol3)
						model.putpixel((j,i), new_color)
			path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'CroppedCompletely.jpg'
			model.save(path,'JPEG')
			return model
		
		
		
		
		
		
		def checkArounSkin(self,matrix,i,j):
			
			count = 0
			if i>0 and j>0 and i< len(matrix)-1 and j < len(matrix[0])-1:
				if matrix[i-1][j-1] == 1 or matrix[i-1][j-1] == 2:
					count +=1 
				if matrix[i-1][j] == 1 or matrix[i-1][j] == 2:
					count += 1
				if matrix[i-1][j+1] == 1 or matrix[i-1][j+1] == 2:
					count += 1
				if matrix[i][j-1] == 1 or matrix[i][j-1] == 2:
					count += 1
			if count >= 3:
				matrix[i][j]=2
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				'''
				def relateSample(self, croppedImage):
					
					model = Image.open(croppedImage)
					scale = model.size
					
					left = 0
					top = 0
					right = 0
					bottom = 0
					
					if scale[0] > 100 and scale[1]>100:
						left = scale[0]/2-25
						top = scale[1]/2-25
						right = scale[0]/2+25
						bottom = scale[1]/2+25
					else:
						left = scale[0]/2-10
						top = scale[1]/2-10
						right = scale[0]/2+10
						bottom = scale[1]/2+10
						
					sample = model.crop((left,top,right,bottom))
					sampleSize = sample.size
					rgb_sample = sample.convert('RGB')
					colorData = set()
					
					for x in range(sampleSize[0]):
						for y in range(sampleSize[1]):
							color = rgb_sample.getpixel((x, y))
							colorData.add(color)
					return colorData


				
				def detectUnrelation(self, croppedImage):
					
					bgcol1,bgcol2,bgcol3 = self.leftTopAreaColor(localImage)
					model = Image.open(croppedImage)
					rgb_im = model.convert('RGB')
					scale = model.size
					sampleColorInfo = self.relateSample(croppedImage)
							
					
					for i in range(0,scale[0]):
						for j in range(0,scale[1]):
							color = rgb_im.getpixel((i, j))
							if color not in sampleColorInfo:
								new_color = (bgcol1,bgcol2,bgcol3)
								model.putpixel((i,j), new_color)
								
					path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'CroppedCompletely.jpg'
					model.save(path,'JPEG')
					return model
				'''
				
				
				
				
				
				
				
				
				
				
				
				
				'''
				
				
				
				
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
								
					return colorData


				
				def detectUnrelation(self, croppedImage):
					
					bgcol1,bgcol2,bgcol3 = self.leftTopAreaColor(localImage)
					model = Image.open(croppedImage)
					rgb_im = model.convert('RGB')
					scale = model.size
					sampleColorInfo = self.relateSample(croppedImage)
							
					
					for i in range(0,scale[0]):
						for j in range(0,scale[1]):
							color = rgb_im.getpixel((i, j))
							if color not in sampleColorInfo:
								new_color = (bgcol1,bgcol2,bgcol3)
								model.putpixel((i,j), new_color)
								
					path = '/Users/tangzekun/Desktop/Cropped/'+localImage[:-4]+'CroppedCompletely.jpg'
					model.save(path,'JPEG')
					return model
			'''
						