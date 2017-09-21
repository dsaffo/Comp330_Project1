# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:10:15 2017

@author: dsaffo, jramirez09
""" 

#import backed module

def main():
    level = 0
    while (level == 0):
        print("Hello welcome to noterizerthingy!")
        print("Type exit to quit at any time")
        path = input("Please enter your folder path: ")
        if path == "exit":
            break
        #if file path is valid
        level = 1
        while (level == 1):
            print("How would you like to sort your notes?")
            print("possible commands are; file, mark, keyword, mention, topic, and back to return to previous menu")
            search = input("Search by: ")
            if (search == 'back'):
                level = 0
            elif (search == 'exit'):
                break
            
            elif(search == 'file'):
                level = 2
                while(level == 2):
                    file = input("Please enter file name or back to return to previous menu: ")
                    if(file == 'back'):
                        level = 1
                    elif(file == 'exit'):
                        break
                    #TODO add function
                    else:
                        level = 2
            
            
            
            elif(search == 'mark'):
                
                
                
                level = 3
                while(level == 3):
                    mark = input("Please enter mark or back to return to previous menu: ")
                    commands = ["@","#","!","^","url"]
                    if(mark == 'back'):
                        level = 1
                    elif(mark == 'exit'):
                        break
                    elif(mark in commands):
                        level = 1
                    else:
                        level = 3
                    
                
            #if(mark not in [("@","#","!","^","url")]):
                 #   print("Error. Mark was not found.")
                    #exit
            
            
            elif(search == 'keyword'): 
                
                
                level = 4
                while(level == 4):
                    keyword = input("Please enter mark or back to return to previous menu: ")
                    if(keyword == 'back'):
                        level = 1
                    elif(keyword == 'exit'):
                        break
                    elif(keyword[0]=='#'):
                        level = 1
                    else:
                        print ("not a valid keyword")
                        level = 4
                
                #TODO add function
                
            
            
            elif(search == 'mention'):
                
                level = 5
                while(level == 5):
                    mention = input("Please enter mark or back to return to previous menu: ")
                    if(mention == 'back'):
                        level = 1
                    elif(mention == 'exit'):
                        break
                    elif(mention[0]=='@'):
                        print('not a valid search')
                        level = 1
                    else:
                        print ("not a valid keyword")
                        level = 5
                
                
            
            elif(search == 'topic'):
                
            
                level = 6
                while(level == 6):
                    topic = input("Please enter mark or back to return to previous menu: ")
                    if(topic == 'back'):
                        level = 1
                    elif(topic == 'exit'):
                        break
                    elif(topic[0]=='!'):
                        print('not a valid search')
                        level = 1
                        
                    else:
                        print ("not a valid entry")
                        level = 6
                    
                    
                
            else: 
               print("That search option does not exist. Try again." )
               level = 1
        
        
        
        
        
    
main()

#File - Ask for file name 
#Mark - ask for what mark (@,#,!,^,url)
#Keyword - ask for the keyword (#somthing)
#Mention - ask for who is mentioned (@someone)
#Topic - ask for what topic to look for (!somethin #
                                        #
                                        

