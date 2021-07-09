fin = open('InputData3.txt', 'r')			
fout = open('OutputData3.txt', 'w')		
for i in fin:
	fout.write(i)

fin.close()					
fout.close()        
			              
               			
fin = open('OutputData3.txt' , 'r')			
print(fin.read())


fin.close()               	
