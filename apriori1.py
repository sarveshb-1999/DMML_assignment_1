import time
import linecache
import collections
from collections import *

words=[]
def Apriori(K, F, filename):
	print("K = ", K , " F= ", F , ' name = ', filename)
	name = "docword." + filename + ".txt"
	name2 = "vocab." + filename + ".txt"
	t_no = int(linecache.getline(name , 3))
	word_no = int(linecache.getline(name , 2))
	doc_no = int(linecache.getline(name , 1))
	arr1=[]
	arr2={}
	arr3=[]
	cnts={}
	trans={}
	unions=set()
	for i in range(0 , word_no+1):
		arr1.append(0)
	for e in open(name2,"rb"):
		e = e.rstrip()
		words.append(e)
	for i in range(1,word_no+1):
		trans[i]=set()
	for i in range(1,doc_no+1):
		unions.add(i)
	for line in open(name,"rb"):
		curword=line.rstrip().decode().split( " ")
		curword=map(int, curword)
		curword=list(curword)
		if len(curword) > 1:
			trans[curword[1]].add(curword[0])
			arr1[curword[1]]+=curword[2]

		
	f1=[set([i]) for i in range(0,word_no+1) if arr1[i]>= F]
	arr3.append(f1)


	for k in range(1,K+1):
		if arr3[k-1]==[]:
			return []
		if k==K:
			print (len(arr3[k-1]))
			return arr3[k-1]
		arr2[k]=generate(arr3[k-1],k+1)


		if arr2[k]=={}:
			return []
		for c in arr2[k]: 
			uni=set(unions)
			for j in arr2[k][c]:
				uni=trans[j].intersection(uni)
			cnts[c]=len(uni)
		arr3.append(0)
		arr3[k]= freq_gen(arr2[k],F,cnts)  
	print (len(arr3[k]))
	return arr3[k]
	
	
def generate(F,k):
	l1=len(F)
	l=k-1
	Ck={}
	p=0
	print ("STARTING\n")
	ans1=set(tuple(sorted(list(a))) for a in F)
	for i in range(0,l1):
		for j in range(i+1,l1):
			m=max(F[i])
			n=max(F[j])
			p1=set(F[i])
			p2=set(F[j])
			p2.remove(n)
			p1.remove(m)
			if m==n or p2!= p1:
				break	
			union=F[i]|F[j]
			ans=set(ksz(list(union)))
			if ans.issubset(ans1):
				Ck[p]=union
				
				p=p+1
			
	print ("DONE\n")
	return Ck

def freq_gen(Ck,F,cnts):
	Fk=[]
	for c in Ck:
		if cnts[c]>=F:
			Fk.append(Ck[c])
	return Fk
	
def ksz(lis):
	l=len(lis)
	sub=[]
	for pos in range(1,l+1):
		if(pos==1):
			li=lis[1:]
		else:
			li=lis[:(pos-1)]+lis[pos:]
		sub.append(sorted(li))
	return [tuple(a) for a in sub]

			
start=time.clock()
			
abcd=Apriori(4,200, "kos")
print (time.clock()-start)
with open("kos_5_300.txt", "w") as output:
	for f in abcd:
		f=list(f)
		f=[words[a] for a in f]
		output.write(str(f))


