import os
import re
import pandas as pd

def get_data():
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(data_path, 'data', '_chat.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        
        date = re.findall(r'\d{2}/\d{2}/\d{4}', data)
        time = re.findall(r'\d{2}:\d{2}', data)
        name = re.findall(r'~\u202f(.*?):', data)
        message = re.findall(r': (\w*[a-zA-Z0-9 ].*)', data)
        
        df = pd.DataFrame(list(zip(date, time, name, message)), columns = ['Date', 'Time', 'Name', 'Message'])
        
        return df
    
get_data()