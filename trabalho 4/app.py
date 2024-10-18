import re
import pandas as pd
import numpy as np

with open('_chat.txt', 'r') as file:
    data = file.read()
    
    # Extracting the date and time
    date = re.findall(r'\d{2}/\d{2}/\d{4}', data)
    time = re.findall(r'\d{2}:\d{2}', data)
    name = re.findall(r'~\u202f(.*?):', data)
    message = re.findall(r': (\w*[a-zA-Z0-9 ].*)', data)
    
    df = pd.DataFrame(list(zip(date, time, name, message)), columns = ['Date', 'Time', 'Name', 'Message'])
    
    print(df)