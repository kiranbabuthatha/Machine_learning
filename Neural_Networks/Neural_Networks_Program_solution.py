import csv
import argparse 
import math
def kiran():
  args = parser.parse_args()
  xi=[]
  file, eta, iterations = args.data, float(args.eta), float(args.iterations)
  with open(file,'r') as csvfile:
    my_reader = csv.reader(csvfile, delimiter=',')
    for row in my_reader:
     xi.append(row)
    def sigma(x):
     return (1/(1+math.exp(-x)))
    w_bias_h1,w_a_h1,w_b_h1,w_bias_h2,w_a_h2,w_b_h2,w_bias_h3,w_a_h3,w_b_h3,w_bias_o,w_h1_o,w_h2_o,w_h3_o=0.2,-0.3,0.4,-0.5,-0.1,-0.4,0.3,0.2,0.1,-0.1,0.1,0.3,-0.4
    print('a,b,h1,h2,h3,o,t,delta_h1,delta_h2,delta_h3,delta_o,w_bias_h1,w_a_h1,w_b_h1,w_bias_h2,w_a_h2,w_b_h2,w_bias_h3,w_a_h3,w_b_h3,w_bias_o,w_h1_o,w_h2_o,w_h3_o')
    print('-,-,-,-,-,-,-,-,-,-,-,0.20000,-0.30000,0.40000,-0.50000,-0.10000,-0.40000,0.30000,0.20000,0.10000,-0.10000,0.10000,0.30000,-0.40000')  
    while(iterations>0):
     iterations=iterations-1
     for i in range(0,len(xi),1): 
      a=float(xi[i][0]) 
      b=float(xi[i][1])
      t=float(xi[i][2])
      h1=(a*w_a_h1)+(1*w_bias_h1)+(b*w_b_h1)
      sigma_h1=float(sigma(h1))
      h2=(a*w_a_h2)+(1*w_bias_h2)+(b*w_b_h2)
      sigma_h2=float(sigma(h2))
      h3=(a*w_a_h3)+(1*w_bias_h3)+(b*w_b_h3)
      sigma_h3=float(sigma(h3))
      O=(sigma_h1*w_h1_o)+(sigma_h2*w_h2_o)+(sigma_h3*w_h3_o)+w_bias_o
      sigma_O=sigma(O) 
      delta_O=sigma_O*(1-sigma_O)*(t-sigma_O)
      delta_h1=float(sigma_h1*(1-sigma_h1)*(delta_O*w_h1_o))
      delta_h2=float(sigma_h2*(1-sigma_h2)*(delta_O*w_h2_o))
      delta_h3=float(sigma_h3*(1-sigma_h3)*(delta_O*w_h3_o))
      w_h1_o=w_h1_o+(eta*delta_O*sigma_h1)
      w_h2_o=w_h2_o+(eta*delta_O*sigma_h2)
      w_h3_o=w_h3_o+(eta*delta_O*sigma_h3)  
      w_bias_o=w_bias_o+(eta*delta_O*1)
      w_a_h1=w_a_h1+(eta*delta_h1*a)
      w_bias_h1=w_bias_h1+(eta*delta_h1*1)
      w_b_h1=w_b_h1+(eta*delta_h1*b)
      w_a_h2=w_a_h2+(eta*delta_h2*a)
      w_bias_h2=w_bias_h2+(eta*delta_h2*1)
      w_b_h2=w_b_h2+(eta*delta_h2*b)
      w_a_h3=w_a_h3+(eta*delta_h3*a)
      w_bias_h3=w_bias_h3+(eta*delta_h3*1)
      w_b_h3=w_b_h3+(eta*delta_h3*b)
      result=str("%.5f" % (a))+','+str("%.5f" % (b))+','+str("%.5f" % (sigma_h1))+','+str("%.5f" % (sigma_h2))+','+str("%.5f" % (sigma_h3))+','+str("%.5f" % (sigma_O))+','+str("%.5f" % (t))+','+str("%.5f" % (delta_h1))+','+str("%.5f" % (delta_h2))+','+str("%.5f" % (delta_h3))+','+str("%.5f" % (delta_O))+','+str("%.5f" % (w_bias_h1))+','+str("%.5f" % (w_a_h1))+','+str("%.5f" % (w_b_h1))+','+str("%.5f" % (w_bias_h2))+','+str("%.5f" % (w_a_h2))+','+str("%.5f" % (w_b_h2))+','+str("%.5f" % (w_bias_h3))+','+str("%.5f" % (w_a_h3))+','+str("%.5f" % (w_b_h3))+','+str("%.5f" % (w_bias_o))+','+str("%.5f" % (w_h1_o))+','+str("%.5f" % (w_h2_o))+','+str("%.5f" % (w_h3_o))
      print(result)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Data File")
    parser.add_argument("-l", "--eta", help="Learning Rate")
    parser.add_argument("-i", "--iterations", help="iterations")
    kiran()