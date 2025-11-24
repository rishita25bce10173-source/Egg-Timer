import sys
import time
import datetime

text='''


                                                                                                                                                                              
                                                                                                                                                                              
EEEEEEEEEEEEEEEEEEEEEE       GGGGGGGGGGGGG        GGGGGGGGGGGGG     TTTTTTTTTTTTTTTTTTTTTTTIIIIIIIIIIMMMMMMMM               MMMMMMMMEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR   
E::::::::::::::::::::E    GGG::::::::::::G     GGG::::::::::::G     T:::::::::::::::::::::TI::::::::IM:::::::M             M:::::::ME::::::::::::::::::::ER::::::::::::::::R  
E::::::::::::::::::::E  GG:::::::::::::::G   GG:::::::::::::::G     T:::::::::::::::::::::TI::::::::IM::::::::M           M::::::::ME::::::::::::::::::::ER::::::RRRRRR:::::R 
EE::::::EEEEEEEEE::::E G:::::GGGGGGGG::::G  G:::::GGGGGGGG::::G     T:::::TT:::::::TT:::::TII::::::IIM:::::::::M         M:::::::::MEE::::::EEEEEEEEE::::ERR:::::R     R:::::R
  E:::::E       EEEEEEG:::::G       GGGGGG G:::::G       GGGGGG     TTTTTT  T:::::T  TTTTTT  I::::I  M::::::::::M       M::::::::::M  E:::::E       EEEEEE  R::::R     R:::::R
  E:::::E            G:::::G              G:::::G                           T:::::T          I::::I  M:::::::::::M     M:::::::::::M  E:::::E               R::::R     R:::::R
  E::::::EEEEEEEEEE  G:::::G              G:::::G                           T:::::T          I::::I  M:::::::M::::M   M::::M:::::::M  E::::::EEEEEEEEEE     R::::RRRRRR:::::R 
  E:::::::::::::::E  G:::::G    GGGGGGGGGGG:::::G    GGGGGGGGGG             T:::::T          I::::I  M::::::M M::::M M::::M M::::::M  E:::::::::::::::E     R:::::::::::::RR  
  E:::::::::::::::E  G:::::G    G::::::::GG:::::G    G::::::::G             T:::::T          I::::I  M::::::M  M::::M::::M  M::::::M  E:::::::::::::::E     R::::RRRRRR:::::R 
  E::::::EEEEEEEEEE  G:::::G    GGGGG::::GG:::::G    GGGGG::::G             T:::::T          I::::I  M::::::M   M:::::::M   M::::::M  E::::::EEEEEEEEEE     R::::R     R:::::R
  E:::::E            G:::::G        G::::GG:::::G        G::::G             T:::::T          I::::I  M::::::M    M:::::M    M::::::M  E:::::E               R::::R     R:::::R
  E:::::E       EEEEEEG:::::G       G::::G G:::::G       G::::G             T:::::T          I::::I  M::::::M     MMMMM     M::::::M  E:::::E       EEEEEE  R::::R     R:::::R
EE::::::EEEEEEEE:::::E G:::::GGGGGGGG::::G  G:::::GGGGGGGG::::G           TT:::::::TT      II::::::IIM::::::M               M::::::MEE::::::EEEEEEEE:::::ERR:::::R     R:::::R
E::::::::::::::::::::E  GG:::::::::::::::G   GG:::::::::::::::G           T:::::::::T      I::::::::IM::::::M               M::::::ME::::::::::::::::::::ER::::::R     R:::::R
E::::::::::::::::::::E    GGG::::::GGG:::G     GGG::::::GGG:::G           T:::::::::T      I::::::::IM::::::M               M::::::ME::::::::::::::::::::ER::::::R     R:::::R
EEEEEEEEEEEEEEEEEEEEEE       GGGGGG   GGGG        GGGGGG   GGGG           TTTTTTTTTTT      IIIIIIIIIIMMMMMMMM               MMMMMMMMEEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRR'''
                                                                                                                                                                              
                                                                                                                                                                              
                                                                                                                                                                              
                                                                                                                                                                              
                                                                                                                                                                              
text1='''
                                                                    
                                                                    
TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEE
T:::::::::::::::::::::TH:::::::H     H:::::::HE::::::::::::::::::::E
T:::::::::::::::::::::TH:::::::H     H:::::::HE::::::::::::::::::::E
T:::::TT:::::::TT:::::THH::::::H     H::::::HHEE::::::EEEEEEEEE::::E
TTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H    E:::::E       EEEEEE
        T:::::T          H:::::H     H:::::H    E:::::E             
        T:::::T          H::::::HHHHH::::::H    E::::::EEEEEEEEEE   
        T:::::T          H:::::::::::::::::H    E:::::::::::::::E   
        T:::::T          H:::::::::::::::::H    E:::::::::::::::E   
        T:::::T          H::::::HHHHH::::::H    E::::::EEEEEEEEEE   
        T:::::T          H:::::H     H:::::H    E:::::E             
        T:::::T          H:::::H     H:::::H    E:::::E       EEEEEE
      TT:::::::TT      HH::::::H     H::::::HHEE::::::EEEEEEEE:::::E
      T:::::::::T      H:::::::H     H:::::::HE::::::::::::::::::::E
      T:::::::::T      H:::::::H     H:::::::HE::::::::::::::::::::E
      TTTTTTTTTTT      HHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEE'''

text2='''
                                                                                                                                                     
                                                                                                                                                     
PPPPPPPPPPPPPPPPP   EEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR   FFFFFFFFFFFFFFFFFFFFFFEEEEEEEEEEEEEEEEEEEEEE       CCCCCCCCCCCCCTTTTTTTTTTTTTTTTTTTTTTT
P::::::::::::::::P  E::::::::::::::::::::ER::::::::::::::::R  F::::::::::::::::::::FE::::::::::::::::::::E    CCC::::::::::::CT:::::::::::::::::::::T
P::::::PPPPPP:::::P E::::::::::::::::::::ER::::::RRRRRR:::::R F::::::::::::::::::::FE::::::::::::::::::::E  CC:::::::::::::::CT:::::::::::::::::::::T
PP:::::P     P:::::PEE::::::EEEEEEEEE::::ERR:::::R     R:::::RFF::::::FFFFFFFFF::::FEE::::::EEEEEEEEE::::E C:::::CCCCCCCC::::CT:::::TT:::::::TT:::::T
  P::::P     P:::::P  E:::::E       EEEEEE  R::::R     R:::::R  F:::::F       FFFFFF  E:::::E       EEEEEEC:::::C       CCCCCCTTTTTT  T:::::T  TTTTTT
  P::::P     P:::::P  E:::::E               R::::R     R:::::R  F:::::F               E:::::E            C:::::C                      T:::::T        
  P::::PPPPPP:::::P   E::::::EEEEEEEEEE     R::::RRRRRR:::::R   F::::::FFFFFFFFFF     E::::::EEEEEEEEEE  C:::::C                      T:::::T        
  P:::::::::::::PP    E:::::::::::::::E     R:::::::::::::RR    F:::::::::::::::F     E:::::::::::::::E  C:::::C                      T:::::T        
  P::::PPPPPPPPP      E:::::::::::::::E     R::::RRRRRR:::::R   F:::::::::::::::F     E:::::::::::::::E  C:::::C                      T:::::T        
  P::::P              E::::::EEEEEEEEEE     R::::R     R:::::R  F::::::FFFFFFFFFF     E::::::EEEEEEEEEE  C:::::C                      T:::::T        
  P::::P              E:::::E               R::::R     R:::::R  F:::::F               E:::::E            C:::::C                      T:::::T        
  P::::P              E:::::E       EEEEEE  R::::R     R:::::R  F:::::F               E:::::E       EEEEEEC:::::C       CCCCCC        T:::::T        
PP::::::PP          EE::::::EEEEEEEE:::::ERR:::::R     R:::::RFF:::::::FF           EE::::::EEEEEEEE:::::E C:::::CCCCCCCC::::C      TT:::::::TT      
P::::::::P          E::::::::::::::::::::ER::::::R     R:::::RF::::::::FF           E::::::::::::::::::::E  CC:::::::::::::::C      T:::::::::T      
P::::::::P          E::::::::::::::::::::ER::::::R     R:::::RF::::::::FF           E::::::::::::::::::::E    CCC::::::::::::C      T:::::::::T      
PPPPPPPPPP          EEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRRFFFFFFFFFFF           EEEEEEEEEEEEEEEEEEEEEE       CCCCCCCCCCCCC      TTTTTTTTTTT'''

                 
hard='''
                                         
            :=+====-:.           
         .=+++++===----.         
        :++++++++==-----.        
       -+++++++++===--::-:       
      :+*****++++==---:::-:      
      =******++++===--::::-      
     :+**+++*++++===--::::-.     
     -+++++++++++===---::::-     
     -=++++++++++===---::::.     
     .-=++++++++=====---:::      
      :-=+++++++======---:.      
       -==+++++++=====---:       
       .-=+++++++++====-:        
         :++++++++++===.         
           :+****+++=:           
         ..::-+++=-.             
                                 '''

soft='''
        @@@@@@@@@@@#-...:+%@@@@@@@@@@@
        @@@@@@@@%:          :%@@@@@@@@
        @@@@@@%:              :@@@@@@@
        @@@@@#                  @@@@@@
        @@@@%:                   @@@@@
        @@@@=                    .@@@@
        @@@#.     ...........     %@@@
        @@@+    ..............    =@@@
        @@@=   ................   -@@@
        @@@-   ..:..............  =@@@
        @@@=   ....:............  %@@@
        @@@#   ................  .@@@@
        @@@@=   ..............  .@@@@@
        @@@@@=    ..........   .@@@@@@
        @@@@@@#.              +@@@@@@@
                                      '''

omelette='''
            *****#@@@%@@@@@@@@@@@@@@@@@@@@@@@*:.           :
            %@@@@@@@@@@@@@@@@@*:   .   ::#@@@@@@@@:    .- =*
            @@@@@@%@@@@@*   =::=: -..:...:-*  -@@@@@@:  **- 
            +==:.@@@@%    *+-.  : =-=+:.*.  .  .  .%@@@@*+##
            .  #@@@*    -  .  .-  :....::        = : %@@@@@%
              @@@#       ..  ==  .     =*-.  .++-+... =@@@@@
             *@@=  . .*      :=::.:-     .  =     ..-..%+@@@
             @@#.  . -=   .:-  :    .. . -=.:  :* :::: :@+@#
            .@@+   .  :... : ..: -     :+-++=.    -: :*-@-@@
            :@@* :. . :* .     .++:=: -... .+++     .-:*@-%@
             +@%: = .:=  - -:=-..  :-  ::==  .     .*-.@**@@
             -%@#.-@@- =.-**: .**    =*::-*  :--:=:*-+@@@@@@
              =@@@-:@@#--=..- =   .*==*- :  *=-**-**@@@@@@@@
               .@@@%:=@@*+*+****.  -:  =*+**-=-**@@@@@@@@@@@
                                                            '''
sunny='''
        **+++++======++=====++=+*%*+%%%##
        ++=====           =++*#@%%##****+
        ======  = =*#===   +*=#%*++====+=
        ===     == ==   +=  =  =++=======
        ==       = ==             ==== = 
        *==           ==++++++=     +=   
        =*=    =   ====+++++++++==   ==  
        ==+        ====+++++++++====  ==+
        === =     ====++++++++++++==   *=
        = ==     ====+++++++++++++==   =+
        ==*=     ====++++++++++++++=   =+
        ==**   =#======+++++++++++==   =+
        ==*+=  +#= ===+++++++++====    +=
        =++==     = ==++++++======    *= 
        ++==           ========     =*=  
        ==                         ++    
                                          '''

dot="Please wait...................................................................."

def intro():
    time.sleep(1)
    print()
    print()
    print(text1)
    print()
    print()
    time.sleep(1)
    print(text2)
    print()
    print()
    time.sleep(1)
    print(text)
    time.sleep(1)
    time.sleep(1)
def main():
    print()
    print()
    ques="What kind of egg do you want?\n\n\n"
    time.sleep(1)
    for cha in ques:
        time.sleep(0.0955)
        sys.stdout.write(cha)
        sys.stdout.flush()
    ques1="a soft boiled egg"
    for ch in ques1:
        time.sleep(0.0955)
        sys.stdout.write(ch)
        sys.stdout.flush()
    print()
    ques2="a hard boiled egg"
    for c in ques2:
        time.sleep(0.0955)
        sys.stdout.write(c)
        sys.stdout.flush()
    print()
    ques3="a fluffy omelet"
    for qu in ques3:
        time.sleep(0.0955)
        sys.stdout.write(qu)
        sys.stdout.flush()
    print()
    ques4="sunny side up"
    for q in ques4:
        time.sleep(0.0955)
        sys.stdout.write(q)
        sys.stdout.flush()      
    print()
    print()
    time.sleep(1)
    choice= int(input("Please enter the type of egg you want: (1/2/3/4) "))
    if choice==1:
        global choi
        choi=1
        print()
        print()
        global chi
        chi="a soft boiled egg: liquid yolk with soft whites (It will take about 3-6 minutes to make)."
        print()
        print()
    elif choice==2:
        choi=2
        print()
        print()
        chi="a hard boiled egg: solid, and slightly crumbly yolk with hard whites (It will take about 12-15 minutes to make)."
        print()
        print()
    elif choice==3:
        choi=3
        print()
        print()
        chi="a fluffy omelet: golden cloud with tender, airy curds, perfectly folded. (8–10 minutes)"
        print()
        print()
    elif choice==4:
        choi=4
        print()
        print()
        chi="sunny side up: a vibrant disc of liquid gold surrounded by crisp white, awaiting the perfect pierce. (3–5 minutes)"
        print()
        print()    
def body(choi,chi):
    time.sleep(1)
    chit="Okay, so you want "+chi
    
    for z in chit:
        time.sleep(0.0955)
        sys.stdout.write(z)
        sys.stdout.flush()
    print()
    print()
    n=int(input("please enter the number of eggs you want (between 1 and 6): "))
    print()
    print()
    h=0
    while h<n:
        time.sleep(1)
        print(hard,end="")
        h+=1
    print()
    print()
    if choi==1:
        minute=4
        secs=30
        time.sleep(1)
        print("It's going to take ",minute,"minutes and ",secs," seconds")
        print()
        print()
        st=input("Do you want to start boiling the eggs ?(YES,yes,Y,y) ")
        Y=["YES","yes","Y","y"]
        if st in Y:
            now = datetime.datetime.now()
            time_to_add = datetime.timedelta(minutes=minute, seconds=secs)
            future_datetime = now + time_to_add
            time_format = "%I:%M:%S %p"
            current_time_str = now.strftime(time_format)
            future_time_str = future_datetime.strftime(time_format)
            print("Current Time: ",current_time_str)
            print()
            print()
            print("Future Time (after 4 min 30 sec): ",future_time_str)
            print()
            print()
            print("STARTING THE TIMER NOW")
            print()
            for r in dot:
                time.sleep(0.5)
                sys.stdout.write(r)
                sys.stdout.flush()
            print()
            print()
            print()
            print()
            print("Your eggs are boiled, please take them out")
            print()
            print()
            p=0
            while p<n:
                time.sleep(1)
                print(soft,end="")
                p+=1
            print()
            print()
            print()
            print("Have a nice day")
                
            
            
    
    elif choi==2:
        minute=13
        secs=30
        time.sleep(1)
        print("It's going to take ",minute,"minutes and ",secs," seconds")
        print()
        print()
        st=input("Do you want to start boiling the eggs ?(YES,yes,Y,y) ")
        Y=["YES","yes","Y","y"]
        if st in Y:
            now = datetime.datetime.now()
            time_to_add = datetime.timedelta(minutes=minute, seconds=secs)
            future_datetime = now + time_to_add
            time_format = "%I:%M:%S %p"
            current_time_str = now.strftime(time_format)
            future_time_str = future_datetime.strftime(time_format)
            print("Current Time: ",current_time_str)
            print()
            print()
            print("Future Time (after 13 min 30 sec): ",future_time_str)
            print()
            print()
            print("STARTING THE TIMER NOW")
            print()
            for r in dot:
                time.sleep(0.5)
                sys.stdout.write(r)
                sys.stdout.flush()
            print()
            print()
            print()
            print()
            print("Your eggs are boiled, please take them out")
            print()
            print()
            p=0
            while p<n:
                time.sleep(1)
                print(soft,end="")
                p+=1
            print()
            print()
            print()
            print("Have a nice day")
    elif choi==3:
        minute=9
        secs=0
        time.sleep(1)
        print("It's going to take ",minute,"minutes and ",secs," seconds")
        print()
        print()
        st=input("Do you want to start boiling the eggs ?(YES,yes,Y,y) ")
        Y=["YES","yes","Y","y"]
        if st in Y:
            now = datetime.datetime.now()
            time_to_add = datetime.timedelta(minutes=minute, seconds=secs)
            future_datetime = now + time_to_add
            time_format = "%I:%M:%S %p"
            current_time_str = now.strftime(time_format)
            future_time_str = future_datetime.strftime(time_format)
            print("Current Time: ",current_time_str)
            print()
            print()
            print("Future Time (after 13 min 30 sec): ",future_time_str)
            print()
            print()
            print("STARTING THE TIMER NOW")
            print()
            for r in dot:
                time.sleep(0.5)
                sys.stdout.write(r)
                sys.stdout.flush()
            print()
            print()
            print()
            print()
            print("Your omelettes are made, please take them out")
            print()
            print()
            p=0
            while p<n:
                time.sleep(1)
                print(omelette,end="")
                p+=1
            print()
            print()
            print()
            print("Have a nice day")
    elif choi==4:
        minute=4
        secs=0
        time.sleep(1)
        print("It's going to take ",minute,"minutes and ",secs," seconds")
        print()
        print()
        st=input("Do you want to start boiling the eggs ?(YES,yes,Y,y) ")
        Y=["YES","yes","Y","y"]
        if st in Y:
            now = datetime.datetime.now()
            time_to_add = datetime.timedelta(minutes=minute, seconds=secs)
            future_datetime = now + time_to_add
            time_format = "%I:%M:%S %p"
            current_time_str = now.strftime(time_format)
            future_time_str = future_datetime.strftime(time_format)
            print("Current Time: ",current_time_str)
            print()
            print()
            print("Future Time (after 13 min 30 sec): ",future_time_str)
            print()
            print()
            print("STARTING THE TIMER NOW")
            print()
            for r in dot:
                time.sleep(0.5)
                sys.stdout.write(r)
                sys.stdout.flush()
            print()
            print()
            print()
            print()
            print("Your eggs are made, please take them out")
            print()
            print()
            p=0
            while p<n:
                time.sleep(1)
                print(sunny,end="")
                p+=1
            print()
            print()
            print()
            print("Have a nice day")
            print()
            print()
            print()
            time.sleep(3)
        
                
                
intro()
main()
body(choi,chi)
                    
            
    
    

        
        
        
        
        
        
    
    
