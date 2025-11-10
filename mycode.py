from pathlib import Path
import pandas as pd

dict = {
    'alice':[24 , 'F' , 'New York' ],
    'bob':[30 , 'M' , 'Los Angeles' ],
    'charlie':[22 , 'M' , 'Chicago' ],
    'diana':[28 , 'F' , 'Miami' ]
}
df = pd.DataFrame(dict)
p = Path.cwd()
if(p / 'data').exists() == False:
    (p / 'data').mkdir()

df.to_csv(str(p / 'data' /'file.csv') , index_label='name')