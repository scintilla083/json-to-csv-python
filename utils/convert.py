import pandas as pd
from .file_util import FileUsage
class Converter:
    def __init__(self,result,output):
        self.result = result
        self.output = output

    def convert(self):
        """
        convert data to data frame and save it to csv file, save csv file to output folder with same name with json(input file)
        :return:
        no return
        """
        if self.result[0] is True:
            df_rows = pd.json_normalize(self.result[1])
            df = pd.DataFrame(df_rows)
        elif self.result[0] is False:
            #df = pd.DataFrame(self.result[1]) TODO протестировать нужно ли json_normalize обычные json файлы
            df_rows = pd.json_normalize(self.result[1])
            df = pd.DataFrame(df_rows)
        else:
            print('Error with read json data')
            return 0
        FileUsage.file_writer(output=self.output,df=df)

