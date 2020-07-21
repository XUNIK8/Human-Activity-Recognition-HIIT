
import scipy as sp
from scipy import signal
from scipy import stats
from scipy.stats import entropy
from scipy.stats import iqr as IQR
import json
import numpy as np




def mean(inArray):
    array=np.array(inArray)
    mean_value = float(array.mean())
    return mean_value

# std: standard deviation of mag column
def std(inArray):
    array=np.array(inArray)
    std_value = float(array.std()) # std value
    return std_value

# mad: median deviation
def mad(inArray):
    array=np.array(inArray)
    mad_value = float(sp.median(array))# median deviation value of mag_column
    return mad_value

# max
def max(inArray):
    array=np.array(inArray)
    max_value=float(array.max()) # max value
    return max_value
# min
def min(inArray):
    array=np.array(inArray)
    min_value= float(array.min()) # min value
    return min_value

# IQR
def IQR(inArray):
    array=np.array(inArray)
    IQR_value=float(IQR(array))# Q3(column)-Q1(column)
    return IQR_value

# Entropy
def entropy(inArray):
    array=np.array(inArray)
    entropy_value=float(entropy(array)) # entropy signal
    return entropy_value

def sma(inArray):
    array=np.array(inArray)
    sma_axial=float(abs(array).sum()) # sum of areas under each signal
    return sma_axial # return sma value

def energy(inArray):
    array=np.array(inArray)
    energy_vector=(array**2).sum() # energy value of each df column
    return energy_vector # return energy vector energy_X,energy_Y,energy_Z

def skew(inArray):
    array=np.array(inArray)
    skew_value=float(stats.skew(array)) # entropy signal
    return skew_value

def kurt(inArray):
    array=np.array(inArray)
    kurt_value=float(stats.kurtosis(array)) # entropy signal
    return kurt_value


def testA(infile,outfile):
    f1 = open(infile, 'r', encoding='utf-8')
    f2 = open(outfile, 'a', encoding='utf-8')
    ln = 0


    feature = []
    b, a = signal.butter(3, 0.1, 'lowpass')
    for line in f1.readlines():
        for i in range(15):
            start = 20 * i
            end = 20 * (i+2)

            ln += 1
            dic = json.loads(line)
            activity = dic['activity']

            accx = signal.filtfilt(b, a, dic['accx'])
            mean_x1 = mean(accx[start:end])
            std_x1 = std(accx[start:end])
            mad_x1 = mad(accx[start:end])
            max_x1 = max(accx[start:end])
            min_x1 = min(accx[start:end])

            sma_x1 = sma(accx[start:end])
            energy_x1 = energy(accx[start:end])
            skew_x1 = skew(accx[start:end])
            kurt_x1 = kurt(accx[start:end])
            # plt.plot(num, accx[0:1000])
            # plt.title('accx:')
        # python要用show展现出来图
            # plt.show()

            accy = signal.filtfilt(b, a, dic['accy'])
            mean_y1 = mean(accy[start:end])
            std_y1 = std(accy[start:end])
            mad_y1 = mad(accy[start:end])
            max_y1 = max(accy[start:end])
            min_y1 = min(accy[start:end])

            sma_y1 = sma(accy[start:end])
            energy_y1 = energy(accy[start:end])
            skew_y1 = skew(accy[start:end])
            kurt_y1 = kurt(accy[start:end])

         #   plt.plot(num, accy[0:1000])
          #  plt.title('accy:')
        # python要用show展现出来图
           # plt.show()

            accz = signal.filtfilt(b, a, dic['accz'])
            mean_z1 = mean(accz[start:end])
            std_z1 = std(accz[start:end])
            mad_z1 = mad(accz[start:end])
            max_z1 = max(accz[start:end])
            min_z1 = min(accz[start:end])

            sma_z1 = sma(accz[start:end])
            energy_z1 = energy(accz[start:end])
            skew_z1 = skew(accz[start:end])
            kurt_z1 = kurt(accz[start:end])
          #  plt.plot(num, accz[0:1000])
          #  plt.title('accz:')
        # python要用show展现出来图
           # plt.show()

            gryx = signal.filtfilt(b, a, dic['gryx'])
            mean_x2 = mean(gryx[start:end])
            std_x2 = std(gryx[start:end])
            mad_x2 = mad(gryx[start:end])
            max_x2 = max(gryx[start:end])
            min_x2 = min(gryx[start:end])

            sma_x2 = sma(gryx[start:end])
            energy_x2 = energy(gryx[start:end])
            skew_x2 = skew(gryx[start:end])
            kurt_x2 = kurt(gryx[start:end])
            #plt.plot(num, gryx[0:1000])
            #plt.title('gryx:')
        # python要用show展现出来图
            #plt.show()

            gryy = signal.filtfilt(b, a, dic['gryy'])
            mean_y2 = mean(gryy[start:end])
            std_y2 = std(gryy[start:end])
            mad_y2 = mad(gryy[start:end])
            max_y2 = max(gryy[start:end])
            min_y2 = min(gryy[start:end])

            sma_y2 = sma(gryy[start:end])
            energy_y2 = energy(gryy[start:end])
            skew_y2 = skew(gryy[start:end])
            kurt_y2 = kurt(gryy[start:end])
            #plt.plot(num, gryy[0:1000])
            #plt.title('gryy:',)
        # python要用show展现出来图
            #plt.show()

            gryz = signal.filtfilt(b, a, dic['gryz'])
            mean_z2 = mean(gryz[start:end])
            std_z2 = std(gryz[start:end])
            mad_z2 = mad(gryz[start:end])
            max_z2 = max(gryz[start:end])
            min_z2 = min(gryz[start:end])

            sma_z2 = sma(gryz[start:end])
            energy_z2 = energy(gryz[start:end])
            skew_z2 = skew(gryz[start:end])
            kurt_z2 = kurt(gryz[start:end])
            #plt.plot(num, gryz[0:1000])
            #plt.title('gryz:')
        # python要用show展现出来图
            #plt.show()

            feature.extend([mean_x1,std_x1,mad_x1,max_x1,min_x1,sma_x1,energy_x1,skew_x1,kurt_x1,
                            mean_y1,std_y1,mad_y1,max_y1,min_y1,sma_y1,energy_y1,skew_y1,kurt_y1,
                            mean_z1,std_z1,mad_z1,max_z1,min_z1,sma_z1,energy_z1,skew_z1,kurt_z1,
                            mean_x2,std_x2,mad_x2,max_x2,min_x2,sma_x2,energy_x2,skew_x2,kurt_x2,
                            mean_y2,std_y2,mad_y2,max_y2,min_y2,sma_y2,energy_y2,skew_y2,kurt_y2,
                            mean_z2,std_z2,mad_z2,max_z2,min_z2,sma_z2,energy_z2,skew_z2,kurt_z2,
                       ])


            for j in range(len(feature)):
                f2.write(str(round(feature[j],16)))
                f2.write(',')
            f2.write(str(int(activity)))
            f2.write("\n")
            feature = []
        print('数据组数：',ln)

    f1.close()
    f2.close()

if __name__ == '__main__':
    infile = '../数据/5.23/安卓/activity4.json'
    outfile = '../myFeature/testfeature_Android_final.txt'
    testA(infile,outfile)