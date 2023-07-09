# starting page
animation = ["""
 ██████╗         
██╔════╝         
██║  ███╗      
██║   ██║        
╚██████╔╝         
 ╚═════╝         
                                                                                
""",
             """
 ██████╗     ██████╗     
██╔════╝     ██╔══██╗       
██║  ███╗    ██████╔╝        
██║   ██║    ██╔══██╗       
╚██████╔╝    ██║  ██║        
 ╚═════╝     ╚═╝  ╚═╝    
""",
             """
 ██████╗     ██████╗      ██████╗         
██╔════╝     ██╔══██╗    ██╔═══██╗    
██║  ███╗    ██████╔╝    ██║   ██║        
██║   ██║    ██╔══██╗    ██║   ██║         
╚██████╔╝    ██║  ██║    ╚██████╔╝          
 ╚═════╝     ╚═╝  ╚═╝     ╚═════╝     
""",
             """
 ██████╗     ██████╗      ██████╗      ██████╗      
██╔════╝     ██╔══██╗    ██╔═══██╗    ██╔════╝    
██║  ███╗    ██████╔╝    ██║   ██║    ██║              
██║   ██║    ██╔══██╗    ██║   ██║    ██║         
╚██████╔╝    ██║  ██║    ╚██████╔╝    ╚██████╗          
 ╚═════╝     ╚═╝  ╚═╝     ╚═════╝      ╚═════╝       
""",
             """
 ██████╗     ██████╗      ██████╗      ██████╗    ███████╗       
██╔════╝     ██╔══██╗    ██╔═══██╗    ██╔════╝    ██╔════╝     
██║  ███╗    ██████╔╝    ██║   ██║    ██║         █████╗         
██║   ██║    ██╔══██╗    ██║   ██║    ██║         ██╔══╝       
╚██████╔╝    ██║  ██║    ╚██████╔╝    ╚██████╗    ███████╗    
 ╚═════╝     ╚═╝  ╚═╝     ╚═════╝      ╚═════╝    ╚══════╝     
""",
             """
 ██████╗     ██████╗      ██████╗      ██████╗    ███████╗    ██████╗        
██╔════╝     ██╔══██╗    ██╔═══██╗    ██╔════╝    ██╔════╝    ██╔══██╗      
██║  ███╗    ██████╔╝    ██║   ██║    ██║         █████╗      ██████╔╝          
██║   ██║    ██╔══██╗    ██║   ██║    ██║         ██╔══╝      ██╔══██╗          
╚██████╔╝    ██║  ██║    ╚██████╔╝    ╚██████╗    ███████╗    ██║  ██║         
 ╚═════╝     ╚═╝  ╚═╝     ╚═════╝      ╚═════╝    ╚══════╝    ╚═╝  ╚═╝     
""",
             """ 
 ██████╗     ██████╗      ██████╗      ██████╗    ███████╗    ██████╗     ██╗   ██╗    
██╔════╝     ██╔══██╗    ██╔═══██╗    ██╔════╝    ██╔════╝    ██╔══██╗    ╚██╗ ██╔╝    
██║  ███╗    ██████╔╝    ██║   ██║    ██║         █████╗      ██████╔╝     ╚████╔╝     
██║   ██║    ██╔══██╗    ██║   ██║    ██║         ██╔══╝      ██╔══██╗      ╚██╔╝      
╚██████╔╝    ██║  ██║    ╚██████╔╝    ╚██████╗    ███████╗    ██║  ██║       ██║       
 ╚═════╝     ╚═╝  ╚═╝     ╚═════╝      ╚═════╝    ╚══════╝    ╚═╝  ╚═╝       ╚═╝     """]

from time import sleep
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_animation():
    for i in animation:
        clear_screen()
        print(i)
        sleep(0.5)
    clear_screen()



logo = animation[-1]