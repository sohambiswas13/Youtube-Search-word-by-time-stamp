# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:12:19 2021

@author: Soham
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:12:09 2021

@author: Soham
"""
# importing libs
from youtube_transcript_api import YouTubeTranscriptApi
import webbrowser

# input as channel link
# extract the channel id from link


def open_id(channel_id_link, key_word):
    channel_id = channel_id_link[17:]

    #list containing dic of transcript
    transcript_dic = YouTubeTranscriptApi.get_transcript(channel_id)

    # extracting list of text from the main list
    mapped_list_text = map(lambda x : x['text'], transcript_dic[:len(transcript_dic)])
    transcript_text_list = list(mapped_list_text)
    # extracting list of time stamp from the main list
    mapped_list_timestamp = map(lambda x : x['start'], transcript_dic[:len(transcript_dic)])
    transcript_timestamp_list = list(mapped_list_timestamp)

    test_timestamp_list = []
    for i in transcript_text_list:
        for k in key_word:
            if i.count(k)>0:
                print(k ,transcript_timestamp_list[transcript_text_list.index(i)] )
                test_timestamp_list.append((transcript_timestamp_list[transcript_text_list.index(i)]))
                
            else:
                continue
            
    if len(test_timestamp_list) == 0:
        print('For some video(s) Either transcription unavailable or nor relevant filter matched, search manually.')
        
    # launching youtube at specific time stamp
    open_id = 'https://www.youtube.com/watch?v='
    for i in test_timestamp_list:
        webbrowser.open(open_id+channel_id+'#t='+ str(i)+'s')
        
def open_id_list():
    print('\n Enter channel links seperated by comma:\n')
    channel_id_link_list = str(input())
    channel_id_link_list = channel_id_link_list.replace(' ','').split(',') 
    print('\n Enter filters to search for seperated by comma:\n')
    key_word_list = input()
    key_word_list = key_word_list.replace(' ','').split(',')
    for i in channel_id_link_list:
        if i != ',' :
            open_id(channel_id_link=i, key_word = key_word_list)
        else:
            continue
        
# ___________________________________________________  Test cases of the function in work   ____________________________________________________

open_id_list()
# 
#https://youtu.be/e2ZyYJ_7eQg , https://youtu.be/D5VN56jQMWM
# lambda , duplex