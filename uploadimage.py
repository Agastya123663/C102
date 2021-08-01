import cv2
import dropbox
import time
import random

start_time = time.time()

def takeSnapshot():
    number = random.randint(0,100)
    print(number)

    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        img_name = 'img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        result = False
    videocaptureobject.release()
    cv2.destroyAllWindows()
    print('snapshot taken')
    return img_name

def upload_file(img_name):
    access_token = 'hnbPmrBxdncAAAAAAAAAAQ5UR1EBpHx90VDbWtL4TkJSig7XwUX-ljk34bLC5x5E'
    file = img_name
    file_from = file
    file_to = '/securitysystem/'+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('File uploaded successfully')

def main():
    while(True):
        if((time.time()-start_time)>=40):
            name = takeSnapshot()
            upload_file(name)

main()
         