import csv
import argparse 
import math
def Kiran():
  args = parser.parse_args()
  Ainst,Binst,xi,count = [],[],[],0
  file=args.data
  with open(file,'r') as csvfile:
    my_reader = csv.reader(csvfile, delimiter=',')
    for row in my_reader:
      xi.append(row)
      if (row[0]=='A'):
            Ainst.append(row)
      if (row[0]=='B'):
            Binst.append(row)      
    nca=len(Ainst)
    ncb=len(Binst)
    def summ(x,y,z):
      sum=0
      for i in range(0,x,1):
        sum=sum+float(y[i][z])
      return sum
    mu_1_c_a=(1/nca)*summ(nca,Ainst,1)#attribute 1 class a
    mu_2_c_a=(1/nca)*summ(nca,Ainst,2)#attribute 2 class a
    mu_1_c_b=(1/ncb)*summ(ncb,Binst,1)#attribute 1 class b
    mu_2_c_b=(1/ncb)*summ(ncb,Binst,2)#attribute 2 class b
    #print(mu_1_c_a,mu_2_c_a,mu_1_c_b,mu_2_c_b)
    def sigmasumm(x,y,z,w):
       sum=0
       for i in range(0,x,1):
         sum=sum+((float(y[i][z])-float(w))**2)
       return sum  
    sigma_1_c_a=(1/(nca-1))*sigmasumm(nca,Ainst,1,mu_1_c_a)
    sigma_2_c_a=(1/(nca-1))*sigmasumm(nca,Ainst,2,mu_2_c_a)
    sigma_1_c_b=(1/(ncb-1))*sigmasumm(ncb,Binst,1,mu_1_c_b)
    sigma_2_c_b=(1/(ncb-1))*sigmasumm(ncb,Binst,2,mu_2_c_b)
    #print(sigma_1_c_a,sigma_2_c_a,sigma_1_c_b,sigma_2_c_b)
    p_a=nca/(nca+ncb)
    p_b=ncb/(nca+ncb)
    #print(p_a,p_b)
    for i in range(0,len(xi),1): 
     pofx1abyc=(1/(2*(22/7)*sigma_1_c_a)**0.5)*math.exp(-(((float(xi[i][1])-mu_1_c_a)**2)/(2*sigma_1_c_a)))
     pofx2abyc=(1/(2*(22/7)*sigma_2_c_a)**0.5)*math.exp(-(((float(xi[i][2])-mu_2_c_a)**2)/(2*sigma_2_c_a))) 
     pofx1bbyc=(1/(2*(22/7)*sigma_1_c_b)**0.5)*math.exp(-(((float(xi[i][1])-mu_1_c_b)**2)/(2*sigma_1_c_b)))
     pofx2bbyc=(1/(2*(22/7)*sigma_2_c_b)**0.5)*math.exp(-(((float(xi[i][2])-mu_2_c_b)**2)/(2*sigma_2_c_b)))
     #print(pofx1abyc,pofx2abyc,pofx1bbyc,pofx2bbyc)
     prioriofa=pofx1abyc*pofx2abyc*p_a
     prioriofb=pofx1bbyc*pofx2bbyc*p_b     
     #print(prioriofa,prioriofb)
     if (prioriofa>prioriofb):
       if(xi[i][0]!='A'):
         count=count+1
     else:
       if(xi[i][0]!='B'):
         count=count+1 
    #print(mu_1_c_a,sigma_1_c_a,mu_2_c_a,sigma_2_c_a,p_a)
    line1=str(mu_1_c_a)+','+str(sigma_1_c_a)+','+str(mu_2_c_a)+','+str(sigma_2_c_a)+','+str(p_a)
    print(line1)
    #print(mu_1_c_b,sigma_1_c_b,mu_2_c_b,sigma_2_c_b,p_b)
    line2=str(mu_1_c_b)+','+str(sigma_1_c_b)+','+str(mu_2_c_b)+','+str(sigma_2_c_b)+','+str(p_b)
    print(line2)
    print(count)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Data File")
    Kiran()