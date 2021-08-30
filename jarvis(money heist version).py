import speech_recognition as sr
import pyttsx3
import webbrowser
## Created by Alfred Soegiarto @Codewithfred ##

# ============= Bahasa Inggris ==================
# Please make sure to mention me when using this assistant, I would love to repost your stories!

# ============= Bahasa Indonesia ================
# Jangan lupa buat mention gw pas make asisten virtual ini, gw bakal seneng banget buat repost story kalian! 



## ENV_VARIABLES: Diganti pake punya kamu aja
ig_username = 'vincentciuserico'
favourite_song_link = 'https://www.youtube.com/watch?v=9ao4FEaDGhQ'
qr_code_link = 'https://www.instagram.com/vincentciuserico/'
playlist_link = 'https://open.spotify.com/artist/7vk5e3vY1uw9plTHJAMwjN?si=YMIell42QSq17X8v2UcbUA&dl_branch=1'

#########################################################################################


class PersonalBot:
  def Listen(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print('Listening for orders..')
      r.pause_threshold = 0.7
      audio = r.listen(source)

      try:
        print("Recognizing orders..")
        Query = r.recognize_google(audio,language='in-en')
      
      except Exception as e:
        print(e)
        print("Can you please say your orders again?")
        return "None"

    return Query

  def Speak(self, audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
  jarvis = PersonalBot()
  webbrowser.open('https://static.wikia.nocookie.net/money-heist/images/7/74/Bank_of_Spain.png/revision/latest/scale-to-width-down/1000?cb=20210412165043')
  jarvis.Speak('Welcome Lacasa De Papel')
  jarvis.Speak('hai, this is professor')
  jarvis.Speak('if you need information, say informasi')
  jarvis.Speak('if you need tokyo information, say tokyo')
  jarvis.Speak('if you need oslo information, say oslo')
  jarvis.Speak('if you need rio information, say rio')
  jarvis.Speak('if you need moskow information, say moskow')
  jarvis.Speak('if you need denver information, say denver')
  jarvis.Speak('if you need nairobi information, say nairobi')
  jarvis.Speak('if you need elsinki information, say elsinki')
  jarvis.Speak('if you need berlin information, say berlin')
  jarvis.Speak('if you need allison parker information, say allison parker')
  jarvis.Speak('if you wanna play national anthem, say lagu kebangsaan')
  jarvis.Speak('if you wanna end, say thank you')

  while True:
    result = jarvis.Listen()
    print("Your order is", result)

    ## Basic Commands
      
    if 'informasi' in result.lower():
      webbrowser.open("https://www.google.co.id/maps/@40.4186253,-3.6944076,3a,90y,176.12h,118.87t/data=!3m8!1e1!3m6!1sAF1QipOVQV2ili3x0JE7Od5nsIegyoESxH_X9N0rBZ7y!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOVQV2ili3x0JE7Od5nsIegyoESxH_X9N0rBZ7y%3Dw203-h100-k-no-pi-0-ya101.41453-ro0-fo100!7i6912!8i3456")
      jarvis.Speak('Place : Banco de Espana, Calle de Alcalá, 48, 28014 Madrid, Spanyol')
      jarvis.Speak('Estimated Income : 1 Miliar Euro, can be more')
      jarvis.Speak('Estimated time : 121 Day')
      jarvis.Speak('our job is : print money')
  # 1 Tokyo
    if 'tokyo' in result.lower():
      webbrowser.open("https://static.wikia.nocookie.net/money-heist/images/d/dd/MH_Part_3_Tokyo.jpg/revision/latest/scale-to-width-down/768?cb=20200313172009")
      jarvis.Speak('Name : Silene Oliveira')
      jarvis.Speak('Age : 30')
      jarvis.Speak('Gender : Female')
      jarvis.Speak('Status : Alive')
      jarvis.Speak('A the age of 14, joined her 28 year old boyfriend into a world of crime.')
      jarvis.Speak('Together, they successfully pulled off 15 heists.')
      jarvis.Speak(' she usually acts before she thinks, which sometimes results in things she regrets. She let her relationship with Rio complicate the plans for the heist. She is quick to lose her patience, as well as sometimes being shown to quickly draw conclusions. She can’t control her emotions very well and also expresses them intensely.')
  # 2 Rio 
    if 'rio' in result.lower():
      webbrowser.open('https://static.wikia.nocookie.net/money-heist/images/f/f1/101_Rio_in_class.jpg/revision/latest?cb=20210718025342')
      jarvis.Speak('Name : Aníbal Cortés')
      jarvis.Speak('Age : 23')
      jarvis.Speak('Gender : Male')
      jarvis.Speak('Status : Alive')
      jarvis.Speak('was born in 1997 in Getafe. His nickname given by his mother was Rayo, meaning lightning bolt in Spanish. At young age he became interested in computers and began programming at the age of 6.')
      jarvis.Speak('He often locked himself in his room for hours. His parents believed that he was working or playing on his computer, but he was actually beginning his career as a hacker.')
      jarvis.Speak('In 2010, he engaged in multiple cyber-attacks, which were all done discretely so the police couldn’t track him. He stole banking data and attacked North American servers. These hacks were reported by several online newspapers such as La Voz, La Nación, El Diario.com, however his identity was never discovered.')
   # 3 Moskow
    if 'moskow' in result.lower():
      webbrowser.open('https://static.wikia.nocookie.net/money-heist/images/f/f6/Moscow_-_Part_1_Promo.jpg/revision/latest/scale-to-width-down/1000?cb=20190918223156')
      jarvis.Speak('Name : Agustin Ramos')
      jarvis.Speak('Age : 50 (at time of death)')
      jarvis.Speak('Gender : Male')
      jarvis.Speak('Status : Deceased')
      jarvis.Speak('His first job was a miner in Asturias, but he later became a thief using tools to rob banks.')
      jarvis.Speak('Little is known about Moscows childhood, but we find out in that when his son, Denver, was very young, his wife was struggling with a drug addiction. Moscow revealed that he left his wife at a roundabout to pick up her drugs, but left with Denver before she returned, and moved elsewhere.')
      jarvis.Speak('He explains that he regrets that decision and went back many times to try and find her, but never did. He only told Denver the truth about this during until then Denver thought his mother left them. Before beginning his criminal life of burglary, he used to be a miner, but it was revealed that he was claustrophobic and so left shortly after.')
   # 4 Denver
    if 'denver' in result.lower():
      webbrowser.open('https://static.wikia.nocookie.net/money-heist/images/a/a6/MH_Part_3_Denver.jpg/revision/latest/scale-to-width-down/682?cb=20200313171219')
      jarvis.Speak('Name : Daniel Ramos')
      jarvis.Speak('Age : 20')
      jarvis.Speak('Gender : Male')
      jarvis.Speak('Status : Alive')
      jarvis.Speak('Denver was raised by his father Moscow, who abandoned Denver mother at a roundabout due her drug use. For many years, Moscow led Denver to believe that his mother abandoned him.')
   # 5 Nairobi
    if 'nairobi' in result.lower():
      webbrowser.open('https://static.wikia.nocookie.net/money-heist/images/7/72/MH_Part_3_Nairobi.jpg/revision/latest/scale-to-width-down/682?cb=20200313171721')
      jarvis.Speak('Name : Ágata Jiménez ')
      jarvis.Speak('Age : 33 (at time of death)')
      jarvis.Speak('Gender : Female')
      jarvis.Speak('Status : Deceased')
      jarvis.Speak('She was born as Ágata Jiménez. Due to her poor conditions, she learned to counterfeit money at 13. During her teenage years, she had a boyfriend, who she later became pregnant with. Her boyfriend left after he found out about the pregnancy. Jiménez gave birth to a boy, she named him Axel. However, when Axel was 3, child services took him away from her after finding out she was dealing drugs. It is also revealed that she gave birth to a daughter.')
   # 6 Oslo
    if 'oslo' in result.lower():
      webbrowser.open('https://static.wikia.nocookie.net/money-heist/images/f/f4/Oslo.jpeg/revision/latest/scale-to-width-down/750?cb=20200316105225')
      jarvis.Speak('Name : Radko Dragić')
      jarvis.Speak('Age : 41 (at time of death)')
      jarvis.Speak('Gender : Male')
      jarvis.Speak('Status : Deceased')
      jarvis.Speak('Oslo was born on November 17th, 1974 in Belgrade, Serbia. Oslo fought in the Balkan Wars with his cousin Helsinki. Oslo died on October 24, 2016 at the age of 41.')
   # 7 Elsinki
    if 'elsinki' in result.lower():
      webbrowser.open('https://static.wikia.nocookie.net/money-heist/images/8/87/Money_Heist_Part_5_Promo_18.jpg/revision/latest/scale-to-width-down/1000?cb=20210804110419')
      jarvis.Speak('Name : Mirko Dragic')
      jarvis.Speak('Age : Early 40')
      jarvis.Speak('Gender : Male')
      jarvis.Speak('Status : Alive')
      jarvis.Speak('Helsinki was born in Serbia. He was a soldier in the Yugoslav Wars with his cousin Oslo. He has a family in Serbia, to whom he sends money when he can.')
      jarvis.Speak('During the war, he had a bullet taken out of him in a tractor garage.')
   # 8 Berlin
    if 'berlin' in result.lower():
      webbrowser.open('https://static.wikia.nocookie.net/money-heist/images/4/46/MH_Part_3_Berlin_Mask_Still.jpg/revision/latest/scale-to-width-down/1000?cb=20200313171323')
      jarvis.Speak('Name : Andrés de Fonollosa Gonzalves')
      jarvis.Speak('Age : 50')
      jarvis.Speak('Gender : Male')
      jarvis.Speak('Status : Deceased')
      jarvis.Speak('It is known that his mother had a relation with another man which resulted in the birth of his half brother. Before the events of the series, he was diagnosed with Helmer’s Myopathy.')
      jarvis.Speak('Before joining the Robbers of The Royal Mint of Spain, Berlin was a jewel thief, with twenty-seven robberies to his name of jewelry stores, auction houses, and armored vehicles. His biggest theft, before the Royal Mint of Spain, was 434 diamonds in Champs-Élysées, Paris.')
      jarvis.Speak('Somewhere in his life, he was recruited by his half brother to be the leader of the “greatest robbery ever”. He was trained in various things along with his fellow robbers, and he learned all the details of the heist.')
   # 9 Allison Parker
    if 'allison parker' in result.lower():
      webbrowser.open('https://static.wikia.nocookie.net/money-heist/images/0/00/Alison_Parker.jpeg/revision/latest/scale-to-width-down/699?cb=20191026110852')
      jarvis.Speak('Name : Alison Parker')
      jarvis.Speak('Age : 17')
      jarvis.Speak('Gender : Female')
      jarvis.Speak('Status : Alive')
      jarvis.Speak('the daughter of Sir Benjamin Parker, the British Ambassador in Spain.')
      jarvis.Speak('her father has taken her hunting regularly since she was five years old, but what she really wants to do is dance')
    
    if 'thank you' in result.lower(): 
      jarvis.Speak('no problem')
      break

    if 'lagu kebangsaan' in result.lower():
      jarvis.Speak('searching National anthem')
      webbrowser.open(favourite_song_link, new=1)