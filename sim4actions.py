from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import json
import os

input_file_name = input('File Name \n')
file = input_file_name

input_string = input('Enter timeframes separated by space \n')
toCut = input_string.split()
input_action = input(f'Enter actions separated by comma  ({len(toCut)-1} required) \n')
metaData = input_action.split(',')

metaDataJson = [{"id":'','actions':[]}]
oldMetaDataJson = []
metaFile = './meta_data_Sim4Actions.json'



for i in range(len(toCut)-1):
    # to cut the video based on metadata on 
    # https://github.com/aroitberg/sims4action
    if not os.path.exists(input_file_name):
        os.makedirs(input_file_name)
    ffmpeg_extract_subclip(file+".mp4", int(toCut[i])/30, int(toCut[i+1])/30, targetname=file+"/"+file+str(i+1)+".mp4")
    metaDataJson[0]['actions'].append({"action":metaData[i]})    

# check if file exists
if not os.path.exists(metaFile):
    with open(metaFile, 'w') as file:
        metaDataJson[0]['id'] = input_file_name    
        print(metaDataJson)
        json.dump(metaDataJson, file, indent=2) 
else:
    with open(metaFile, 'r') as file:
        oldMetaDataJson = json.load(file)
        metaDataJson[0]['id'] = input_file_name
        print(metaDataJson)
        # metaDataJson[0]['actions'].append({'action':metaData[i]})
        oldMetaDataJson.append(metaDataJson[0])
    with open(metaFile, 'w') as file:
            json.dump(oldMetaDataJson, file, indent=2)
        
