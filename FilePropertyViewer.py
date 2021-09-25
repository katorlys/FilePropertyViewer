def showFileProperty(path):
    import time,os
    for root,files in os.walk(path,True):
        print("Location: " + root + "\n")
        for filename in files:
            state = os.stat(os.path.join(root,filename))
            info = "File Name: " + filename + "\n"
            info = info + "Size: " + ("%d" % state[-4]) + "\n"
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-1]))
            info = info + "Date Created: " + t + "\n"
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-2]))
            info = info + "Date Modified: " + t + "\n"
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-3]))
            info = info + "Date Accessed: " + t + "\n"
            print(info + "\n")

if __name__ == "__main__":
    path = r"%LOCAL_PATH%"
    showFileProperty(path)
