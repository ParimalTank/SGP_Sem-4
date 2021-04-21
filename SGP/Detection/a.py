# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)
stop_data = cv2.CascadeClassifier('stop_data.xml')
f_data = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
wall_data = cv2.CascadeClassifier('haarcascade_wallclock.xml')

while (True):
    ret, frame = vid.read()
    found = stop_data.detectMultiScale(frame, minSize=(20, 20))
    foundfdata = f_data.detectMultiScale(frame, minSize=(20, 20))
    foundfdatawall = wall_data.detectMultiScale(frame, minSize=(20, 20))


    for (x, y, width, height) in found:

        # every recognized sign
        cv2.rectangle(frame, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 5)
        cv2.putText(frame,'stop signal board', (80, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
        print('\n')
    for (x, y, width, height) in foundfdata:

        # every recognized sign
        cv2.rectangle(frame, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 5)
        cv2.putText(frame, '        Person', (80, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)

    for (x, y, width, height) in foundfdatawall:

        # every recognized sign
        cv2.rectangle(frame, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 5)
        cv2.putText(frame,'                     wallclock', (80, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()



