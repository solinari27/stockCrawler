# -*- coding: utf-8 -*-
#! /usr/bin/env python  
#version 2.7  
import time  
import base64  
import sys  

GLOBAL_INPUT_PATH=""  
GLOBAL_OUTPUT_PATH=""

#convert file stream to base64 and save to file  
def Base64EncodeFileToFile(inputFile,outputFile):  
    fread = open(inputFile, 'rb')  
    fwrite= open(outputFile, 'wb')  
    base64.encode(fread,fwrite)  
    fread.close()  
    fwrite.close()  
    
#decode file stream to orginal and save to file  
def Base64DecodeFileToFile(inputFile,outputFile):  
    fileRead= open(inputFile, 'rb')  
    fileWrite = open(outputFile, 'wb')  
    base64.decode(fileRead, fileWrite)  
    fileRead.close()  
    fileWrite.close()
    











