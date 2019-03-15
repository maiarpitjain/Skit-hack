import sched, time, datetime
s=sched.scheduler(time.time,time.sleep)

def run_video():
    import classA
    import os
    os.system("cd video")
    classA.start_lecture()



def run_voice():
   import classA
   

import check_date
r=check_date.return_delay()

if 1:
    def prog():
        
        s.enter(r,2,run_video)
        s.enter(r,1,run_voice)
        s.run()
    import threading    
    import predict_images
    thread2 = threading.Thread(target=prog)
    thread1 = threading.Thread(target=predict_images.run_attendance)
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
 
else:
    print("Check date")

