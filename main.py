#https://www.youtube.com/watch?v=zp-kAt1Ih5k

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Datafame')

#df = pd.DataFrame({
#    'No.1':[1,2,3,4],
#    'No.2':[10,20,30,40]
#})


#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0),width=200,height=200)#datafreameは引数の指定可能
#st.table(df)#静的表現

#df = pd.DataFrame(
#    np.random.rand(20,3),
#    columns=['a','b','c']
#)

#st.dataframe(df,height=800)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

st.dataframe(df,height=800)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
st.map(df)

st.write('DataImage')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は、',option,'です'


if st.checkbox('showimage'):
    img =Image.open('test.png')
    st.image(img,'test')#use_column_width=True)


st.write('Interractive Widgetrs')


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write("ここは右カラム")
    
expander1=st.expander('問い合わせ')
expander1.write('内容')
expander2=st.expander('問い合わせ')
expander2.write('内容')
expander3=st.expander('問い合わせ')
expander3.write('内容')


st.write('プログレスバー')
'start!'
lastest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    lastest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
    
'end!'  



text = st.text_input(
    'あなたの趣味を教えてください'
)

condition = st.slider('あたなのいまの調子は',0,100,50)
'コンディション',condition
'あなたの趣味は',text


"""
# 章
## 節
### 項目

```python    
import streamlit as st
import numpy as np
import pandas as pd   
```   
    
    
"""



