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

    width = file1.getsampwidth()

    print("numframes: ", num_frames, "rate: ", rate, "width: ", width)

    for i in range(start*rate*width,finish*rate*width):
        samples[i]=0
    
    p2lib.write('output3.wav',file1,num_frames,samples)
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
    
    finalLength = int(num_frames + num_frames*(1/3))
    finalSamples = []
    #shift by a third
    
    zeroes = [0]* int(num_frames* (1/3))
    samples1 = zeroes #prepend 0s
    samples2 = samples[:] #append 0s
            
    for i in range(0, len(samples)):
        samples1.append(samples[i])
    
    for i in range(0, int(num_frames*(1/3))):
        samples2.append(0)
        
    for i in range(0,finalLength):
        finalSamples.append(samples1[i]+samples2[i])
    
    #for i in range(0,int(num_frames*1/3)):
    #    finalSamples.append(samples[i])

    print("Len of FinalSample = ", len(finalSamples))

    #for i in range(0, int(num_frames-num_frames*1/3)):
    #    finalSamples.append(samples[i] + samples[int(i+num_frames*1/3)])

        
    #for i in range(int(num_frames-num_frames*1/3),int(num_frames)):
    #    finalSamples.append(samples[i])

    print(len(samples1),len(samples2),finalLength)
    for i in range(0,finalLength):
        if finalSamples[i] >= 255:
            finalSamples[i] = 255
        elif finalSamples[i] <= 0:
            finalSamples[i] = 0

    
    print("Final Length = ",finalLength)
    p2lib.write('output4.wav',file1,finalLength,finalSamples)
    file1.close()
    
    
def copyfile():
##    file = wave.open("Twinkle.wav",'r')
    file = wave.open("RowRow.wav",'r')
    num_frames = file.getnframes()
    frames =file.readframes(num_frames)
    samples = list(frames)
    print("channels:",file.getnchannels())
    print("sample width:", file.getsampwidth())
    print("frame rate:", file.getframerate())
    print("number of frames:", num_frames)
    print("frames length", len(frames))
    print("list length:", len(samples))
    for m in range(len(samples)):
        if samples[m]!= 0:
            break
    print(m,samples[m+0], samples[m+1], samples[m+2],samples[m+3],
            samples[m+4], samples[m+5], samples[m+6], samples[m+7],
            samples[m+8], samples[m+9], samples[m+10], samples[m+11]
          )
    for m in range(num_frames):
        if frames[m] != 0:
            break
    print(frames[m],frames[m+1],frames[m+2],frames[m+3])
##    p2lib.write('output0.wav',file,num_frames,samples)
    file.close()
    
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
            copyfile()
        else:
            break
#main()

