import os
import glob
import pandas as pd
import tornado

class mergecsv:

    try:
        def merge_csvfiles(self):
            files = pd.DataFrame([file for file in glob.glob("dist/*.log/*")], columns=["fullpath"])
            files_split = files['fullpath'].str.rsplit("\\", 1, expand=True).rename(columns={0: 'path', 1: 'filename'})
            files = files.join(files_split)

            for f in files['filename'].unique():
                paths = files[files['filename'] == f]['fullpath']
                dfs = [pd.read_csv(path, header=None, index_col=None) for path in paths]
                if(len(paths)>1):
                    concat_df = pd.concat(dfs)
                    count = 0
                    for path in paths:
                        if(count > 0):
                            print("Removed file : "+path)
                            os.remove(path)
                        else:
                            concat_df.to_csv(path, index=False, header=False)
                            print("Data written in file: "+path)
                        count+=1

            print("Merged Successfully!")

    except Exception as f:
        print("Merging Error:", f)
