import sched
import time
import winsound as ws #the use of this module is set only for Windows
                      #you may need to import other modules for other OS

def alarm(alarm_time, wav_file, message):
    set = sched.scheduler(time.time, time.sleep)
    set.enterabs(alarm_time,1,print,argument=(message))
    set.enterabs(alarm_time,1,ws.PlaySound, argument=(wav_file, ws.SND_FILENAME))
    print('Alarm set for',time.asctime(time.localtime(alarm_time)))
    set.run()
