"""
    Simple speech recognition program using the Google API
    The program has the ability to recognize recorded wav file or record and 
    recognize in real-time.
"""
import speech_recognition as sr 
  

def recorded_speech_recognition(audio_file):  
    # AUDIO_FILE = ("LDC93S1.wav") 
    
    # use the audio file as the audio source 
    
    r = sr.Recognizer() 
    
    with sr.AudioFile(audio_file) as source: 
        #reads the audio file. Here we use record instead of 
        #listen 
        audio = r.record(source)
    
    try: 
        transcribed_text = r.recognize_google(audio)
        print("The audio file says: " + transcribed_text) 
        return transcribed_text
    
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
        return 1
    
    except sr.RequestError as e: 
        print("Could not request results from Google Speech  Recognition service; {0}".format(e))
        return 1

# Record and recognize using microphone
def real_time_recognition():
    # Credit: https://github.com/frozenparadox99/real-time-speech-recognition/blob/master/speechRec.ipynb

    mic_list = sr.Microphone.list_microphone_names() 
    # print the list of available mics
    print(mic_list)
    sample_rate=48000
    chunk_size=4096
    with sr.Microphone(device_index = 0, sample_rate = sample_rate,  chunk_size = chunk_size) as source: 
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source) 
        print ("Say Something")
        #listens for the user's input 
        audio = r.listen(source) 
            
        try: 
            text = r.recognize_google(audio) 
            print ("you said: " ,text )
            return text
        
        #error occurs when google could not understand what was said 
        
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio") 
            return 1
        
        except sr.RequestError as e: 
            print("Could not request results from Google  Speech Recognition service; {0}".format(e))
            return 1