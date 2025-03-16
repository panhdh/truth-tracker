from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 啟用跨域支持

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

if __name__ == '__main__':
    app.run(port=5000, debug=True)