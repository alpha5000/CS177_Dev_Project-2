#CS177 Fall 2013 Project 2
#Audio Manipulation
#Author: Marco Centracchio
#mcentrac@purdue.edu

import wave
import p2lib

def combine():
    f1 = input("Please enter the name of the first file\n")
    f2 = input("Please enter the name of the second file\n")
    file1 = wave.open(f1)
    file2 = wave.open(f2)
    num_frames1 = file1.getnframes()
    num_frames2 = file2.getnframes()

    samples1=file1.readframes(num_frames1)
    samples1= list(samples1)
    
    samples2=file2.readframes(num_frames2)
    samples2=list(samples2)
    
    output_list = samples1+samples2
    p2lib.write('output1.wav',file1,(num_frames1+num_frames2),output_list)
    file1.close()
    file2.close()
    
def silence():
    f1 = input("Please enter the name of the file\n")
    file1 = wave.open(f1)
    start = int(input("Input the start point of the silence (in seconds)\n"))
    finish = int(input("Input the end point of the silence (in seconds)\n"))
    
    num_frames = file1.getnframes()
    samples = file1.readframes(num_frames)
    samples = list(samples)
    rate = file1.getframerate()

    for i in range(start*rate,finish*rate):
        samples[i]=0
    
    output_list = bytearray(samples)
    p2lib.write('output3.wav',file1,num_frames,output_list)
    file1.close()

def change_volume():
    f1 = input("Please enter the name of the file\n")
    file1 = wave.open(f1)
    change = float(input("Input change in volume. Input <1 to decrease, >1 to increase; 1 leaves volume the same.\n"))
    
    num_frames = file1.getnframes()
    samples = file1.readframes(num_frames)
    samples = list(samples)
    rate = file1.getframerate()
    
    for x in range(0,num_frames):
        samples[x]=float(samples[x])
    
    for x in range(0,num_frames):
        y = change*samples[x]
        if y>=255:
            samples[x]=255
        elif y <=0:
            samples[x]=0
        else:
            samples[x] = change*samples[x]
  
    for x in range(0,num_frames):
        samples[x] = int(samples[x])
        
    samples = bytearray(samples)
    output_list = samples
    p2lib.write('output2.wav',file1,num_frames,output_list)
    file1.close()
    
def makeRound():
    f1 = input("Please enter the name of the file\n")
    file1 = wave.open(f1)
    
    num_frames = file1.getnframes()
    samples = file1.readframes(num_frames)
    samples = list(samples)
    rate = file1.getframerate()

    num_samples = len(samples)
    num_shift = int(num_frames/3)
    print(num_frames, num_samples, num_frames*4)
    finalLength = (num_samples + num_shift)
    finalSamples = (finalLength*[0])
    #shift by a third
    listShift = (num_shift*[0])
    samples1 = listShift + samples[:] #prepend 0s
    samples2 = samples[:] + listShift #append 0s
    
    for i in range(finalLength-1):
        finalSamples[i] = samples1[i] #+samples2[i]
    print(len(samples1),len(samples2),len(samples),len(listShift))
    print("Len of FinalSample = ", len(finalSamples))
    print(max(finalSamples))
    
    for i in range(0,finalLength):
        if finalSamples[i] >= 255:
            finalSamples[i] = finalSamples[i]//2
        elif finalSamples[i] <= 0:
            finalSamples[i] = 0

    print(max(finalSamples))
    print("Final Length = ",finalLength)
    
    output_list = bytearray(finalSamples)
    p2lib.write('output4b.wav',file1,finalLength//4,output_list)
    file1.close()
    
def main(): 
    while 1:
        print("Please Select an function")
        print("1 = Audio File Merge")
        print("2 = Adjust Volume")
        print("3 = Generate Silence")
        print("4 = Create a Round")
        selection = int(input('Please enter selection\n'))
        if selection == 1:
            combine()
        elif selection == 2:
            change_volume()
        elif selection == 3:
            silence()
        elif selection == 4:
            makeRound()
main()

