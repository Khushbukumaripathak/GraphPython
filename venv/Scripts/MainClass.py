from Conversion import *
#from MergeCSV import *
from datetime import timezone
import datetime
import csv
import os
import shutil
import pdb
import os
import glob
import pandas as pd

class mainclass:

    def read_LogFile(self, sensorTag):
        arrFiles = os.listdir('.\\Logs')
        for item in arrFiles:
            os.system('color FF')
            print("\r\n--Analysing "+item+" file--" )
            # Directory path
            parent_dir = ".\\"+item
            #shutil.rmtree(parent_dir)
            os.makedirs(parent_dir, exist_ok=True)
            obj = conversion()
            rssi = []
            temp = []
            vib = []
            date = []
            rows = []
            valueCount = 0
            a=0
            keep_phrases = ["Device:  " + sensorTag + "  :: RSSI Value:",
                            "Device:  " + sensorTag + "  :: Temperature Value:",
                            "Device:  " + sensorTag + "  :: VibX Value:",
                            "Device:  " + sensorTag + "  :: VibY Value:",
                            "Device:  " + sensorTag + "  :: VibZ Value:"]
            with open(os.path.join('.\\Logs\\', item), 'r') as f:
                f = f.readlines()
                for line in f:
                    for phrase in keep_phrases:
                        if phrase in line:
                            value = line.split(':')[len(line.split(':')) - 1].strip();

                            if "RSSI" in phrase:
                                timestamp_rssi, value_rssi=conversion.rssi_conversion(obj, value)
                                rssi.append(value_rssi)
                                dt = datetime.datetime(1970,1,1,0,0,0)
                                timestamp=dt.replace(tzinfo=timezone.utc)
                                timestamp=timestamp + datetime.timedelta(milliseconds=timestamp_rssi)
                                date.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))

                                with open(parent_dir+"\\"+sensorTag+'-RSSI-'+timestamp.date().strftime("%Y-%m-%d")+'.csv', 'a', newline='') as csvfile:
                                    filewriter = csv.writer(csvfile, delimiter=";")
                                    filewriter.writerow([timestamp.strftime("%m/%d/%Y %I:%M:%S %p"), value_rssi])

                            elif "Temperature" in phrase:
                                timestamp_temp, value_temp = conversion.temp_conversion(obj, value)
                                temp.append(value_temp)
                                dt = datetime.datetime(1970, 1, 1, 0, 0, 0)
                                timestamp = dt.replace(tzinfo=timezone.utc)
                                timestamp = timestamp + datetime.timedelta(milliseconds=timestamp_temp)
                                date.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))
                                with open(parent_dir+"\\"+sensorTag+'-AA90-'+timestamp.date().strftime("%Y-%m-%d")+'.csv', 'a', newline='') as csvfile:
                                    filewriter = csv.writer(csvfile, delimiter=";")
                                    filewriter.writerow([timestamp.strftime("%m/%d/%Y %I:%M:%S %p"), value_temp])

                            if "VibX" in phrase or "VibY" in phrase or "VibZ" in phrase:

                                if "VibX" in phrase:
                                    flag = False
                                    value_count, timestamp_vib_x, values_x = conversion.vibration_conversion(obj, value)
                                    valueCount = value_count
                                    dt = datetime.datetime(1970, 1, 1, 0, 0, 0)
                                    timestamp = dt.replace(tzinfo=timezone.utc)
                                    timestamp = timestamp + datetime.timedelta(milliseconds=timestamp_vib_x)
                                    date.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))
                                    file_name = parent_dir+"\\"+sensorTag+'-B080-'+timestamp.date().strftime("%Y-%m-%d")+'.csv';

                                    with open(file_name, 'a', newline='') as csvfile, open(file_name, 'r') as inFile:
                                        filewriter = csv.writer(csvfile, delimiter=";")
                                        if os.path.getsize(file_name) == 0:
                                            line = []
                                            line.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))
                                            line.append(value_count)
                                            for item in values_x:
                                                line.append(item)
                                            filewriter.writerow(line)
                                        else:
                                            for line in inFile:
                                                if timestamp.strftime("%m/%d/%Y %I:%M:%S %p") in line:
                                                    break
                                                else:
                                                    line = []
                                                    line.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))
                                                    line.append(value_count)
                                                    for item in values_x:
                                                        line.append(item)
                                                    filewriter.writerow(line)
                                                    break

                                elif "VibY" in phrase:
                                    value_count, timestamp_vib_y, values_y = conversion.vibration_conversion(obj, value)
                                    valueCount = value_count
                                    dt = datetime.datetime(1970, 1, 1, 0, 0, 0)
                                    timestamp = dt.replace(tzinfo=timezone.utc)
                                    timestamp = timestamp + datetime.timedelta(milliseconds=timestamp_vib_y)
                                    date.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))
                                    file_name = parent_dir+"\\"+sensorTag+'-B081-'+timestamp.date().strftime("%Y-%m-%d")+'.csv';

                                    with open(file_name, 'a', newline='') as csvfile, open(file_name, 'r') as inFile:
                                        filewriter = csv.writer(csvfile, delimiter=";")
                                        if os.path.getsize(file_name) == 0:
                                            line = []
                                            line.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))
                                            line.append(value_count)
                                            for item in values_y:
                                                line.append(item)
                                            filewriter.writerow(line)
                                        else:
                                            for line in inFile:
                                                if timestamp.strftime("%m/%d/%Y %I:%M:%S%p") in line:
                                                    break
                                                else:
                                                    line = []
                                                    line.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))
                                                    line.append(value_count)
                                                    for item in values_y:
                                                        line.append(item)
                                                    filewriter.writerow(line)
                                                    break

                                elif "VibZ" in phrase:
                                    value_count, timestamp_vib_z, values_z = conversion.vibration_conversion(obj, value)
                                    valueCount = value_count
                                    dt = datetime.datetime(1970, 1, 1, 0, 0, 0)
                                    timestamp = dt.replace(tzinfo=timezone.utc)
                                    timestamp = timestamp + datetime.timedelta(milliseconds=timestamp_vib_z)
                                    date.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))
                                    file_name = parent_dir+"\\"+sensorTag+'-B082-'+timestamp.date().strftime("%Y-%m-%d")+'.csv';
                                    with open(file_name, 'a', newline='') as csvfile, open(file_name, 'r') as inFile:
                                        filewriter = csv.writer(csvfile, delimiter=";")
                                        if os.path.getsize(file_name) == 0:
                                            line = []
                                            line.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))
                                            line.append(value_count)
                                            for item in values_z:
                                                line.append(item)
                                            filewriter.writerow(line)
                                        else:
                                            for line in inFile:
                                                if timestamp.strftime("%m/%d/%Y %I:%M:%S %p") in line:
                                                    break
                                                else:
                                                    line = []
                                                    line.append(timestamp.strftime("%m/%d/%Y %I:%M:%S %p"))
                                                    line.append(value_count)
                                                    for item in values_z:
                                                        line.append(item)
                                                    filewriter.writerow(line)
                                                    break

                            break
        print("--Analysing Data completed--")

    with open('input.csv') as input_file:
        try:
            csv_reader = csv.reader(input_file, delimiter = ';')
            line_count = 0
            for row in csv_reader:
               if line_count == 0:
                   line_count+=1
                   continue
               else:
                   line_count += 1
                   print("\r\n--Extracting data for sensor "+row[0]+"--")
                   read_LogFile(conversion(), row[0])
        except Exception as e:
            print("Error")
            raise e

    arrFiles = os.listdir('.\\Logs')
    if(len(arrFiles)):
        print("\r\n--Started merging the files with same name--")
        #mergecsv.merge_csvfiles(conversion())
        files = pd.DataFrame([file for file in glob.glob("*.log/*")], columns=["fullpath"])
        #files = pd.DataFrame([file for file in glob.glob("dist/*.log/*")], columns=["fullpath"])
        files_split = files['fullpath'].str.rsplit("\\", 1, expand=True).rename(columns={0: 'path', 1: 'filename'})
        files = files.join(files_split)

        for f in files['filename'].unique():
            paths = files[files['filename'] == f]['fullpath']
            dfs = [pd.read_csv(path, header=None, index_col=None) for path in paths]
            if (len(paths) > 1):
                concat_df = pd.concat(dfs)
                count = 0
                for path in paths:
                    if (count > 0):
                        print("Removed file : " + path)
                        os.remove(path)
                    else:
                        concat_df.to_csv(path, index=False, header=False)
                        print("Data written in file: " + path)
                    count += 1

        print("Merged Successfully!")

    # Function to create new folder if not exists
    def make_new_folder(folder_name, parent_folder):

        # Path
        path = os.path.join(parent_folder, folder_name)

        # Create the folder
        # 'new_folder' in
        # parent_folder
        try:
            # mode of the folder
            mode = 0o777

            # Create folder
            os.mkdir(path, mode)
        except OSError as error:
            print(error)

    # current folder path
    current_folder = os.getcwd()

    # list of folders to be merged
    list_dir = os.listdir('.\\Logs')

    # enumerate on list_dir to get the
    # content of all the folders ans store
    # it in a dictionary
    content_list = {}
    for index, val in enumerate(list_dir):
        path = os.path.join(current_folder, val)
        content_list[list_dir[index]] = os.listdir(path)

    # folder in which all the content will
    # be merged
    merge_folder = 'Gateway\\Messages\\'

    # merge_folder path - current_folder
    # + merge_folder
    merge_folder_path = os.path.join(current_folder, merge_folder)

    files = glob.glob(merge_folder_path)
    for f in files:
        shutil.rmtree(f)

    if(os.path.isdir(merge_folder_path) == False):
        # create merge_folder if not exists
        make_new_folder(merge_folder, current_folder)

    # loop through the list of folders
    for sub_dir in content_list:

        # loop through the contents of the
        # list of folders
        for contents in content_list[sub_dir]:
            # make the path of the content to move
            path_to_content = sub_dir + "/" + contents

            # make the path with the current folder
            dir_to_move = os.path.join(current_folder, path_to_content)

            # move the file
            shutil.move(dir_to_move, merge_folder_path)

    for folder in list_dir:
        shutil.rmtree(os.path.join(current_folder, folder))

input("\r\nPress enter to close the program")


