import csv
import argparse 
def kiran():
  args = parser.parse_args()
  file, eta, threshold = args.data, float(args.eta), float(args.threshold)
  with open(file,'r') as csvfile:
   my_reader = csv.reader(csvfile, delimiter=',')
   xi=[]
   for row in my_reader:
    xi.append(row)
   w0,w1,w2,x0=0,0,0,1
   iteration=0
   n=len(xi)
   sumofs2error_old=0
   sumof9s2error_new=len(xi)
   while(sumofs2error_new > threshold): 
    sumofs2error_old=sumofs2error_new
    sumofs2error=0
    gradientsum=[0,0,0]
    for i in range(0,n,1):
     x1=float(xi[i][0])
     x2=float(xi[i][1])
     yi=float(xi[i][2])
     xibar=[x0,x1,x2]
     fofxibar=(w0*x0)+(w1*x1)+(w2*x2)
     error=yi-fofxibar
     s2error=error*error
     sumofs2error=sumofs2error+s2error
     for j in range(3): 
      gradientsum[j]=gradientsum[j]+(xibar[j]*error)
    sumofs2error_new=sumofs2error
    result=str(iteration)+','+str(round(w0,4))+','+str(round(w1,4))+','+str(round(w2,4))+','+str(round(sumofs2error,4))
    w0=w0+gradientsum[0]*eta
    w1=w1+gradientsum[1]*eta
    w2=w2+gradientsum[2]*eta
    print(result)
    iteration += 1
if __name__ == '__kiran__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Data File")
    parser.add_argument("-l", "--eta", help="Learning Rate")
    parser.add_argument("-t", "--threshold", help="Threshold")
    kiran()
