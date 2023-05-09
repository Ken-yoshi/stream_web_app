import streamlit as st
from PIL import Image
import datetime

st.title('アプリ')
st.caption('テストアプリ')
st.subheader('サンプルページを作成中です')
st.text('PythonのコードだけでWebページを作成\nできるかのテストページです。')

code = '''
import streamlit as st

st.title('アプリ')

'''
st.code(code , language='Python')

#画像
image = Image.open('9-2.png')
st.image(image, width=200)

video_file = open('gass.mp4' , 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

with st.form(key='profile_form'):

    name = st.text_input('名前')
    address = st.text_input('住所')

    #日付
    today = st.date_input(
        '作業日',
        datetime.date(2023,5,10)
    )
    #セレクトボックス
    age_category = st.selectbox(
        '年齢層:',
        ('20代','30代','40代')
    )

    #ラジオ
    age_category = st.radio(
        '年齢層:',
        ('20代','30代','40代')
    )

    #複数選択
    hobby = st.multiselect(
        '趣味',
        ('Sport', 'programming', 'annime','fisshing')
    )


    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ{name}さん {address}からお越しですね!')
        st.text(f'年齢層：{ age_category}')
        st.text(f'趣味: {",".join(hobby)}')
