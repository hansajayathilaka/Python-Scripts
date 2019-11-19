# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
    for filename in os.listdir("font"): 
        test = '_'.join(filename.lower().split('-'))
        try:
            os.rename(r"C:\Users\Crede48\Desktop\font/" + filename, r"C:\Users\Crede48\Desktop\font/" + test)
        except:
            print(filename, test, sep = '  **  ')
        #os.rename(filename, test)
        
        
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
