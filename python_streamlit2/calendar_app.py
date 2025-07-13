import streamlit as st
import json
import os
from datetime import date

EVENT_FILE = 'events.json'

def load_events():
    if os.path.exists(EVENT_FILE) and os.path.getsize(EVENT_FILE) > 0:
        with open(EVENT_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_events(events):
    with open(EVENT_FILE, 'w') as f:
        json.dump(events, f)

st.title("📝 予定管理アプリ")

st.info("👉 予定の追加・検索・ソートは左側のサイドバーを開いて操作してください。")

events = load_events()

# --- サイドバー ---
st.sidebar.header("予定を追加")

add_date = st.sidebar.date_input("日付を選択", date.today())
add_text = st.sidebar.text_input("予定内容")

if st.sidebar.button("追加"):
    if add_text.strip() == "":
        st.sidebar.warning("予定内容を入力してください")
    else:
        add_date_str = add_date.strftime("%Y-%m-%d")
        if add_date_str not in events:
            events[add_date_str] = []
        events[add_date_str].append(add_text.strip())
        save_events(events)
        st.sidebar.success(f"{add_date_str} に予定を追加しました")
        st.rerun()

st.sidebar.markdown("<br><br>", unsafe_allow_html=True)  # 空白（改行）を追加
st.sidebar.markdown("### 検索機能")  # 検索機能のタイトル

search_query = st.sidebar.text_input("予定をキーワード検索")


# ソート条件選択
sort_key = st.sidebar.selectbox(
    "並び替え方法",
    options=[
        "日付昇順",
        "日付降順",
    ],
    index=0
)

# --- 予定一覧表示 ---
st.header("📅 全ての予定一覧")

# 全ての予定を (日付, 予定内容) のタプルに分解
all_items = []
for day_str, events_list in events.items():
    for e in events_list:
        if search_query.lower() in e.lower() if search_query else True:
            all_items.append( (day_str, e) )

# ソート
if sort_key == "日付昇順":
    all_items.sort(key=lambda x: x[0])
elif sort_key == "日付降順":
    all_items.sort(key=lambda x: x[0], reverse=True)

# 表示
if not all_items:
    st.info("表示する予定がありません。")

current_date = None
for idx, (day_str, event_text) in enumerate(all_items):
    if day_str != current_date:
        st.subheader(day_str)
        current_date = day_str

    col1, col2 = st.columns([8,1])
    col1.write(event_text)
    if col2.button("削除", key=f"del_{day_str}_{idx}"):
        events[day_str].remove(event_text)
        if not events[day_str]:
            del events[day_str]
        save_events(events)
        st.success(f"{day_str} の予定を削除しました")
        st.rerun()
