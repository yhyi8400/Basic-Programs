import os

#Function to rename multiple files
def main():
    i=1
    for filename in os.listdir("bike"):
        dst = 'apple_'+str(i) + ".jpg"
        src = 'bike/'+filename
        dst = 'bike/'+dst

        #rename() function will
        #rename all the files
        os.rename(src,dst)
        i += 1


main()

### Drive Code
##if__name__ == "__main__":
##    #Calling main() function
##    main()
