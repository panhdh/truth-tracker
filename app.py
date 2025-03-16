from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # 啟用跨域支持

# 全局變量存儲投票數據和留言
votes = {'Andy': 0, '家寧': 0}
comments = []

@app.route('/')
def index():
    return app.send_static_file('index.html')

# 硬編碼的事件數據
EVENTS = {
    '家寧Andy爭議': {
        'timeline': [
            {
                'date': '2024-10-01',
                'event': 'Andy 發布11分鐘爆料影片，指控家寧奪權'
            },
            {
                'date': '2024-10-04',
                'event': '家寧回應，否認指控並稱有合約證據'
            },
            {
                'date': '2024-10-05',
                'event': '家寧哥哥雞肉攤頂讓，網友質疑轉移焦點'
            }
        ],
        'analysis': '雙方各執一詞，Andy 強調受害者身份，家寧稱有法律依據，事件真相待證實。'
    }
}

@app.route('/search/<keyword>')
def search(keyword):
    # 查找事件數據
    event_data = EVENTS.get(keyword, {
        'timeline': [],
        'analysis': ''
    })
    return jsonify(event_data)

# 投票 API
@app.route('/api/vote', methods=['POST'])
def vote():
    data = request.get_json()
    candidate = data.get('candidate')
    
    if candidate in votes:
        votes[candidate] += 1
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': '無效的候選人'}), 400

@app.route('/api/vote', methods=['GET'])
def get_votes():
    total = sum(votes.values())
    return jsonify({
        'votes': votes,
        'total': total
    })

# 留言 API
@app.route('/api/comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    comment = data.get('comment')
    
    if comment:
        comment_data = {
            'comment': comment,
            'timestamp': datetime.now().isoformat()
        }
        comments.append(comment_data)
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': '留言不能為空'}), 400

@app.route('/api/comments', methods=['GET'])
def get_comments():
    # 按時間倒序排序
    sorted_comments = sorted(comments, key=lambda x: x['timestamp'], reverse=True)
    return jsonify(sorted_comments)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)