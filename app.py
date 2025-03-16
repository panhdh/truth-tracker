from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from datetime import datetime
import re
import sqlite3
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # 啟用跨域支持

# 初始化數據庫
def init_db():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS votes
                 (candidate TEXT PRIMARY KEY, count INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS comments
                 (comment TEXT, timestamp TEXT)''')
    
    # 初始化投票數據
    c.execute('INSERT OR IGNORE INTO votes (candidate, count) VALUES (?, ?)', ('Andy', 0))
    c.execute('INSERT OR IGNORE INTO votes (candidate, count) VALUES (?, ?)', ('家寧', 0))
    conn.commit()
    conn.close()

init_db()

# 預設時間軸事件
default_events = [
    {'date': '2024-10-01', 'desc': 'Andy 發布11分鐘爆料影片，指控家寧奪權'},
    {'date': '2024-10-04', 'desc': '家寧回應，否認指控並稱有合約證據'},
    {'date': '2024-10-05', 'desc': '家寧哥哥雞肉攤頂讓，網友質疑轉移焦點'},
    {'date': '2025-03-14', 'desc': '家寧和母親正式回應，公開部分合約細節'},
    {'date': '2025-03-14', 'desc': 'Andy直播反駁，稱將公開更多證據'},
    {'date': '2025-03-15', 'desc': '網友爆料家寧疑似準備推出新頻道'}
]

# 用戶提交的事件
user_events = []

@app.route('/')
def index():
    return app.send_static_file('index.html')

# 事件相關 API
@app.route('/api/events', methods=['GET'])
def get_events():
    # 合併預設事件和用戶提交的事件
    all_events = default_events + user_events
    # 按日期排序
    all_events.sort(key=lambda x: x['date'])
    return jsonify(all_events)

@app.route('/api/event', methods=['POST'])
def add_event():
    data = request.get_json()
    date = data.get('date')
    event = data.get('event')
    
    # 驗證日期格式
    if not date or not re.match(r'\d{4}-\d{2}-\d{2}$', date):
        return jsonify({'success': False, 'error': '無效的日期格式'}), 400
    
    if not event:
        return jsonify({'success': False, 'error': '事件描述不能為空'}), 400
    
    # 新增事件
    user_events.append({
        'date': date,
        'desc': event
    })
    
    # 返回更新後的時間軸
    return get_events()

# 投票 API
@app.route('/api/vote', methods=['POST'])
def vote():
    data = request.get_json()
    candidate = data.get('candidate')
    
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    
    try:
        c.execute('SELECT count FROM votes WHERE candidate = ?', (candidate,))
        result = c.fetchone()
        if result is not None:
            c.execute('UPDATE votes SET count = count + 1 WHERE candidate = ?', (candidate,))
            conn.commit()
            return jsonify({'success': True})
        return jsonify({'success': False, 'error': '無效的候選人'}), 400
    finally:
        conn.close()

@app.route('/api/vote', methods=['GET'])
def get_votes():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    
    try:
        c.execute('SELECT candidate, count FROM votes')
        results = c.fetchall()
        votes_dict = {candidate: count for candidate, count in results}
        total = sum(votes_dict.values())
        return jsonify({
            'votes': votes_dict,
            'total': total
        })
    finally:
        conn.close()

# 留言 API
@app.route('/api/comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    comment = data.get('comment')
    
    if comment:
        conn = sqlite3.connect('votes.db')
        c = conn.cursor()
        try:
            timestamp = datetime.now().isoformat()
            c.execute('INSERT INTO comments (comment, timestamp) VALUES (?, ?)', (comment, timestamp))
            conn.commit()
            return jsonify({'success': True})
        finally:
            conn.close()
    return jsonify({'success': False, 'error': '留言不能為空'}), 400

@app.route('/api/comments', methods=['GET'])
def get_comments():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    try:
        c.execute('SELECT comment, timestamp FROM comments ORDER BY timestamp DESC')
        results = c.fetchall()
        comments_list = [{'comment': comment, 'timestamp': timestamp} for comment, timestamp in results]
        return jsonify(comments_list)
    finally:
        conn.close()

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)