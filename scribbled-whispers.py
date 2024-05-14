import os
import whisper
from whisper.utils import get_writer
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory



def clear(): os.system('cls')

def printScribbledWhispers():
    print(r'''
  ██████  ▄████▄   ██▀███   ██▓ ▄▄▄▄    ▄▄▄▄    ██▓    ▓█████ ▓█████▄ 
▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓█████▄ ▓█████▄ ▓██▒    ▓█   ▀ ▒██▀ ██▌
░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▒██▒ ▄██▒██▒ ▄██▒██░    ▒███   ░██   █▌
  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██░█▀  ▒██░█▀  ▒██░    ▒▓█  ▄ ░▓█▄   ▌
▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒░██░░▓█  ▀█▓░▓█  ▀█▓░██████▒░▒████▒░▒████▓ 
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ░▒▓███▀▒░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░ ▒▒▓  ▒ 
░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░ ▒ ░▒░▒   ░ ▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░ ░ ▒  ▒ 
░  ░  ░  ░          ░░   ░  ▒ ░ ░    ░  ░    ░   ░ ░      ░    ░ ░  ░ 
      ░  ░ ░         ░      ░   ░       ░          ░  ░   ░  ░   ░    
         ░                           ░       ░                 ░      
 █     █░ ██░ ██  ██▓  ██████  ██▓███  ▓█████  ██▀███    ██████       
▓█░ █ ░█░▓██░ ██▒▓██▒▒██    ▒ ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒       
▒█░ █ ░█ ▒██▀▀██░▒██▒░ ▓██▄   ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░ ▓██▄         
░█░ █ ░█ ░▓█ ░██ ░██░  ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒      
░░██▒██▓ ░▓█▒░██▓░██░▒██████▒▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒▒██████▒▒      
░ ▓░▒ ▒   ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░      
  ▒ ░ ░   ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░      
  ░   ░   ░  ░░ ░ ▒ ░░  ░  ░  ░░          ░     ░░   ░ ░  ░  ░        
    ░     ░  ░  ░ ░        ░              ░  ░   ░           ░    
''')
def printWolf():
    print(r'''
                                        __
                            .d$$b
                          .' TO$;\     AWWWWOOOOOO"
                         /  : TP._;
                        / _.;  :Tb|           YOU HEAR THE HOWL OF A LONE,
                       /   /   ;j$j           HUNGRY VALUE WOLF IN THE DISTANCE...
                   _.-'       d$$$$           THANKS FOR USING SCRIBBLED WHISPERS!
                 .' ..       d$$$$;           THIS IS VALUE FOR VALUE SOFTWARE!
                /  / P'      d$$$$P. |\       IF YOU RECEIVED VALUE FROM USING
               / '      .d$$$P' |\^'l         THIS PROGRAM, CONSIDER RETURNING
             .'           `T$P^''"''  :       EQUIVALENT VALUE IN ONE OF THE
         ._.'      _.'                ;       FOLLOWING WAYS:
      `-.- '.-'-' ._.       _.-'.-''
    `.-' _____  ._              .-'           - SHARE SCRIBBLED WHISPERS WITH A FRIEND
   - (.g$$$$$$$b.              .'             - SLAP ME SOME BITCOIN: 
     '' ^^ T$$$P ^)            .(:              SEND SATS TO:
          _ / -'  /.'         /:/;                  sirspencer@fountain.fm
       ._.'-'`-'  ')/         /;/;                  sirspencer@getalby.com
 `-.- '..--''   ' /         /  ;              
.-' ..--''        -'          :               GOT AN IDEA TO MAKE IT BETTER? SUBMIT A
..--''--.- '         (\      .-(\             PR TO THE PROJECT HERE:
  ..--''              `-\(\/;`                https://github.com/SpencerPearson/scribbled-whispers
    _.                      :                 
                            ;`-               
                        :\                    
                           ; 
          ''')


model = whisper.load_model("small.en")
epsPath = "../../../episodes/"

def main():
    finished = False
    while finished == False:
        clear()
        printScribbledWhispers()
        print('Choose a file to transcribe:')
        input('(Press ENTER to continue)')
        audio = askopenfilename(initialdir="./", filetypes=(("supported files", "*.mp3 *.mp4 *.mpeg *.mpga *.m4a *.wav *.webm"), ("all files", "*.*")))
        result = model.transcribe(audio, verbose=True)
        print('Choose a directory destination to SAVE AS:')
        input('(Press ENTER to continue)')
        outputDir = askdirectory(title='Choose a FOLDER', initialdir='./')
        # srt_writer = get_writer("srt", outputDir)
        # srt_writer(result, audio)
        txt_writer = get_writer("txt", outputDir)
        txt_writer(result, audio)
    
if __name__ == '__main__':
    main()