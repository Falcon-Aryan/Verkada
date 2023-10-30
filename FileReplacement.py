import os
import shutil
import time
#from playsound import playsound
#from pygame import mixer

#file = '/Users/aryankhanna/Desktop/Tornado Siren.mp3'

def main(): 

    devicePath = '/Volumes/VPPGLOBAL'
    oldFile1 = '/Volumes/VPPGLOBAL/video/1 Product_Walkthrough_Video_001 .mp4'
    oldFile2 = '/Volumes/VPPGLOBAL/video/2 What_District_Leaders_Say_001.mp4'

    devicePath2 = '/Volumes/VPPGLOBAL 1'
    oldFile12 = '/Volumes/VPPGLOBAL 1/video/1 Product_Walkthrough_Video_001 .mp4'
    oldFile22 = '/Volumes/VPPGLOBAL 1/video/2 What_District_Leaders_Say_001.mp4'
    
    devicePath3 = '/Volumes/VPPGLOBAL 2'
    oldFile13 = '/Volumes/VPPGLOBAL 2/video/1 Product_Walkthrough_Video_001 .mp4'
    oldFile23 = '/Volumes/VPPGLOBAL 2/video/2 What_District_Leaders_Say_001.mp4'
    
    devicePath4 = '/Volumes/VPPGLOBAL 3'
    oldFile14 = '/Volumes/VPPGLOBAL 3/video/1 Product_Walkthrough_Video_001 .mp4'
    oldFile24 = '/Volumes/VPPGLOBAL 3/video/2 What_District_Leaders_Say_001.mp4'
    
    devicePath5 = '/Volumes/VPPGLOBAL 4'
    oldFile15 = '/Volumes/VPPGLOBAL 4/video/1 Product_Walkthrough_Video_001 .mp4'
    oldFile25 = '/Volumes/VPPGLOBAL 4/video/2 What_District_Leaders_Say_001.mp4'
    
    devicePath6 = '/Volumes/VPPGLOBAL 5'
    oldFile16 = '/Volumes/VPPGLOBAL 5/video/1 Product_Walkthrough_Video_001 .mp4'
    oldFile26 = '/Volumes/VPPGLOBAL 5/video/2 What_District_Leaders_Say_001.mp4'

    devicePath7 = '/Volumes/VPPGLOBAL 6'
    oldFile17 = '/Volumes/VPPGLOBAL 6/video/1 Product_Walkthrough_Video_001 .mp4'
    oldFile27 = '/Volumes/VPPGLOBAL 6/video/2 What_District_Leaders_Say_001.mp4'

    newFile1 = '/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/1. Introducing Intercom (reduced).mp4'
    newFile2 = '/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/2. Customer Story - La Cañada SD.mp4'
    
    if os.path.exists(devicePath):
        os.remove(oldFile1)
        print("Old File 1 Deleted on Device 1")
        
        time.sleep(1)
        
        os.remove(oldFile2)
        print("Old File 2 Deleted on Device 1")        
    else:
        print("Device 1 not found.")
        
    time.sleep(2)
        
    if os.path.exists(devicePath):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/1. Introducing Intercom (reduced).mp4', '/Volumes/VPPGLOBAL/video')
        print("New File 1 Added on Device 1")
        
    else:
        print("Device 1 not found.")
            
    time.sleep(2)
 
    if os.path.exists(devicePath):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/2. Customer Story - La Cañada SD.mp4', '/Volumes/VPPGLOBAL/video')
        print("New File 2 Added on Device 1")
        
    else:
        print("Device 1 not found")
        
    
# 2nd Device    
    if os.path.exists(devicePath2):
        os.remove(oldFile12)
        print("Old File 1 Deleted on Device 2")
        
        time.sleep(1)
        
        os.remove(oldFile22)
        print("Old File 2 Deleted on Device 2")        
    else:
        print("Device 2 not found.")
        
    time.sleep(2)
        
    if os.path.exists(devicePath2):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/1. Introducing Intercom (reduced).mp4', '/Volumes/VPPGLOBAL 1/video')
        print("New File 1 Added on Device 2")
        
    else:
        print("Device 2 not found.")
            
    time.sleep(2)
 
    if os.path.exists(devicePath2):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/2. Customer Story - La Cañada SD.mp4', '/Volumes/VPPGLOBAL 1/video')
        print("New File 2 Added on Device 2")
        
    else:
        print("Device 2 not found")
        
        
# 3rd Device    
    if os.path.exists(devicePath3):
        os.remove(oldFile13)
        print("Old File 1 Deleted on Device 3")
        
        time.sleep(1)
        
        os.remove(oldFile23)
        print("Old File 2 Deleted on Device 3")        
    else:
        print("Device 3 not found.")
        
    time.sleep(2)
        
    if os.path.exists(devicePath3):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/1. Introducing Intercom (reduced).mp4', '/Volumes/VPPGLOBAL 2/video')
        print("New File 1 Added on Device 3")
        
    else:
        print("Device 3 not found.")
            
    time.sleep(2)
 
    if os.path.exists(devicePath3):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/2. Customer Story - La Cañada SD.mp4', '/Volumes/VPPGLOBAL 2/video')
        print("New File 2 Added on Device 3")
        
    else:
        print("Device 3 not found")

  
        
# 4th Device    
    if os.path.exists(devicePath4):
        os.remove(oldFile14)
        print("Old File 1 Deleted on Device 4")
        
        time.sleep(1)
        
        os.remove(oldFile24)
        print("Old File 2 Deleted on Device 4")        
    else:
        print("Device 4 not found.")
        
    time.sleep(2)
        
    if os.path.exists(devicePath4):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/1. Introducing Intercom (reduced).mp4', '/Volumes/VPPGLOBAL 3/video')
        print("New File 1 Added on Device 4")
        
    else:
        print("Device 4 not found.")
            
    time.sleep(2)
 
    if os.path.exists(devicePath4):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/2. Customer Story - La Cañada SD.mp4', '/Volumes/VPPGLOBAL 3/video')
        print("New File 2 Added on Device 4")
        
    else:
        print("Device 4 not found")
        
        
# 5th Device    
    if os.path.exists(devicePath5):
        os.remove(oldFile15)
        print("Old File 1 Deleted on Device 5")
        
        time.sleep(1)
        
        os.remove(oldFile25)
        print("Old File 2 Deleted on Device 5")        
    else:
        print("Device 5 not found.")
        
    time.sleep(2)
        
    if os.path.exists(devicePath5):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/1. Introducing Intercom (reduced).mp4', '/Volumes/VPPGLOBAL 4/video')
        print("New File 1 Added on Device 5")
        
    else:
        print("Device 5 not found.")
            
    time.sleep(2)
 
    if os.path.exists(devicePath5):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/2. Customer Story - La Cañada SD.mp4', '/Volumes/VPPGLOBAL 4/video')
        print("New File 2 Added on Device 5")
        
    else:
        print("Device 5 not found")
        
        
# 6th Device    
    if os.path.exists(devicePath6):
        os.remove(oldFile16)
        print("Old File 1 Deleted on Device 6")
        
        time.sleep(1)
        
        os.remove(oldFile26)
        print("Old File 2 Deleted on Device 6")        
    else:
        print("Device 6 not found.")
        
    time.sleep(2)
        
    if os.path.exists(devicePath6):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/1. Introducing Intercom (reduced).mp4', '/Volumes/VPPGLOBAL 5/video')
        print("New File 1 Added on Device 6")
        
    else:
        print("Device 6 not found.")
            
    time.sleep(2)
 
    if os.path.exists(devicePath6):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/2. Customer Story - La Cañada SD.mp4', '/Volumes/VPPGLOBAL 5/video')
        print("New File 2 Added on Device 6")
        
    else:
        print("Device 6 not found")

  

# 7th Device    
    if os.path.exists(devicePath7):
        os.remove(oldFile17)
        print("Old File 1 Deleted on Device 7")
        
        time.sleep(1)
        
        os.remove(oldFile27)
        print("Old File 2 Deleted on Device 7")        
    else:
        print("Device 7 not found.")
        
    time.sleep(2)
        
    if os.path.exists(devicePath7):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/1. Introducing Intercom (reduced).mp4', '/Volumes/VPPGLOBAL 6/video')
        print("New File 1 Added on Device 7")

    else:
        print("Device 7 not found.")
            
    time.sleep(2)
 
    if os.path.exists(devicePath7):
        
        shutil.copy2('/Users/aryankhanna/Documents/Pipship/Verkada/FileTransfer/Verkada New Vids/New Files/2. Customer Story - La Cañada SD.mp4', '/Volumes/VPPGLOBAL 6/video')
        print("New File 2 Added on Device 7")
         
    else:
        print("Device 7 not found")
        
        
if __name__ == '__main__':
    # invoking main function
    main()
    print("ALL DONE!!")
    os.system('say "I Done"')
    #os.system('say "Come back and reload me!"')
