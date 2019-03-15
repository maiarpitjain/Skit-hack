
def send_name_in_db(fname,lname,email,mobno,address,department):
    import sqlite3
    connection=sqlite3.connect("my.db")
    crsr=connection.cursor()
    mobno=int(mobno)

    sql_command="""INSERT INTO employee VALUES (?,?,?,?,?,?)"""
    crsr.execute(sql_command,(fname,lname,email,mobno,address,department))

    connection.commit() 
    
    connection.close()

def edit_name_in_excel(value):
    import csv
    print(value)
    myData = []
    for i in range(len(value)):
        myData.append([])
        myData[i].append(value[i])
    print(myData)
    myFile = open('example2.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)
        
    print("Writing complete")

def edit_name_of_present_student():
    pass

def take_student_names(ch):
    
    l=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    l6=[]
    for i in range(ch):
        l.append(input("Enter employee{} fname:".format(i+1)))
        l2.append(input("Enter employee{} lname:".format(i+1)))
        l3.append(input("Enter employee{} email:".format(i+1)))
        l4.append(input("Enter employee{} mobile no:".format(i+1)))
        l5.append(input("Enter employee{} address:".format(i+1)))
        l6.append(input("Enter employee{} department:".format(i+1)))
        send_name_in_db(l[i],l2[i],l3[i],l4[i],l5[i],l6[i])

    edit_name_in_excel(l)    
    return l  
  

def create_ch_folder(ch):
    import os
    
    for i in range(ch):
        newpath = r'G:\skit_project\new{}'.format(i+1) 
        if not os.path.exists(newpath):
            os.makedirs(newpath)

def take_100_images(ch):
    student_names=take_student_names(ch)
    for i in range(ch):
        import cv2
        import numpy as np

        # Load HAAR face classifier
        face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # Load functions
        def face_extractor(img):
            # Function detects faces and returns the cropped face
            # If no face detected, it returns the input image
            
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            
            if faces is ():
                return None
            
            # Crop all faces found
            for (x,y,w,h) in faces:
                cropped_face = img[y:y+h, x:x+w]

            return cropped_face

        # Initialize Webcam
        cap = cv2.VideoCapture(0)
        count = 0
        name= student_names[i]
        # Collect 100 samples of your face from webcam input
        while True:

            ret, frame = cap.read()
            if face_extractor(frame) is not None:
                count += 1
                face = cv2.resize(face_extractor(frame), (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                # Save file in specified directory with unique name
                file_name_path = 'G://skit_project//new{}//{}'.format(i+1,name) + str(count) + '.jpg'
                cv2.imwrite(file_name_path, face)

                # Put count on images and display live count
                cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow('Face Cropper', face)
                
            else:
                print("Face not found")
                pass

            if cv2.waitKey(1) == 13 or count == 100: #13 is the Enter Key
                break
                
        cap.release()
        cv2.destroyAllWindows()      
        print("Collecting Samples Complete")

def create_model_for_all_students(ch):
    l=[]
    for j in range(ch):
        
        import cv2
        import numpy as np
        from os import listdir
        from os.path import isfile, join
        print(cv2.__version__)
        # Get the training data we previously made
        data_path = 'G://skit_project//new{}//'.format(j+1)
        # a=listdir('d:/faces')
        # print(a)
        # """
        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

        # Create arrays for training data and labels
        Training_Data, Labels = [], []

        # Open training images in our datapath
        # Create a numpy array for training data
        for i, files in enumerate(onlyfiles):
            image_path = data_path + onlyfiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(i)
        # 
        # Create a numpy array for both training data and labels
        Labels = np.asarray(Labels, dtype=np.int32)
        global model
        model = cv2.face_LBPHFaceRecognizer.create()
        # Initialize facial recognizer
        # model = cv2.face_LBPHFaceRecognizer.create()
        # model=cv2.f
        # NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()

        # Let's train our model 
        model.train(np.asarray(Training_Data), np.asarray(Labels))
        l.append(model)
        print("Model trained sucessefully")
    return l

def predict_images(ch,student_names):
    l_model=create_model_for_all_students(ch)
    import cv2
    import numpy as np
    import webbrowser
    import time 
    l=[]

    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def face_detector(img, size=0.5):
        
        # Convert image to grayscale
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        if faces is ():
            return img, []
        
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            roi = img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (200, 200))
        return img, roi


    # Open Webcam
    cap = cv2.VideoCapture(0)
    capture_duration=120
    start_time=time.time()
    p_employee=[]



    while (int(time.time()-start_time) < capture_duration):

        ret, frame = cap.read()
        
        image, face = face_detector(frame)
        
        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            # Pass face to prediction model
            # "results" comprises of a tuple containing the label and the confidence value
            results=[]
            confidence=[]
            display_string=[]
            for i in range(ch):
                results.append(i)
                confidence.append(i)
                display_string.append(i)
                results[i]=l_model[i].predict(face)
            
            #print(results1)
                if results[i][1] < 500 :
                    confidence[i] = int( 100 * (1 - (results[i][1])/400) )
                    #print("confidance{}".format(i),confidence[i])
                    display_string[i] = str(confidence[i]) + '% Confident it is User'
            #print(results)
            
            confidence_sort=confidence.copy()
            confidence_sort.sort()
            #print(confidence)
            
            for i in range(ch):
                if confidence_sort[-1]==confidence[i] and confidence[i] > 85:
                    #print(confidence[i])
                    #print(i)
                    if student_names[i] not in p_employee:
                        p_employee.append(student_names[i])
                    cv2.putText(image, display_string[i], (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
                    cv2.putText(image, "Hey {}".format(student_names[i]), (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                    cv2.imshow('Face Recognition', image )
                        
                else:
                    #cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                    cv2.imshow('Face Recognition', image )

        except:
            cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )
            #lin for give output 0 or 1 for swith off lights 
            pass
            
        if cv2.waitKey(1) == 13: #13 is the Enter Key
            break

    cap.release()
    cv2.destroyAllWindows()   
    return p_employee

