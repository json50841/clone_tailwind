from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

users_db = {"admin": "123456"}
tokens_db = set()

class MyHandler(BaseHTTPRequestHandler):
    def _set_cors_headers(self):
        """统一设置 CORS 头"""
        self.send_header('Access-Control-Allow-Origin', '*')  # 可以换成前端地址
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')

    def _set_headers(self, status=200, content_type='application/json'):
        """统一设置响应头"""
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self._set_cors_headers()
        self.end_headers()

    def do_OPTIONS(self):
        """处理 CORS 预检请求"""
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query = parse_qs(parsed_url.query)

        # 登录接口
        if path == '/login':
            username = query.get("username", [None])[0]
            password = query.get("password", [None])[0]
            if username and password and users_db.get(username) == password:
                token = f"{username}_token"
                tokens_db.add(token)
                self._set_headers()
                self.wfile.write(json.dumps({"message": "登录成功", "token": token}).encode('utf-8'))
            else:
                self._set_headers(401)
                self.wfile.write(json.dumps({"error": "用户名或密码错误"}).encode('utf-8'))
            return

        # 带 token 的 posts 接口
        if path == '/posts':
            auth_header = self.headers.get('Authorization')
            if not auth_header or not auth_header.startswith("Bearer "):
                self._set_headers(401)
                self.wfile.write(json.dumps({"error": "未授权"}).encode('utf-8'))
                return

            token = auth_header.split(" ")[1]
            if token not in tokens_db:
                self._set_headers(401)
                self.wfile.write(json.dumps({"error": "无效 token"}).encode('utf-8'))
                return

            self._set_headers()
            posts = [
                {"id": 1, "title": "第一篇文章", "summary": "这是第一篇文章的摘要"},
                {"id": 2, "title": "第二篇文章", "summary": "这是第二篇文章的摘要"},
            ]
            self.wfile.write(json.dumps(posts).encode('utf-8'))
            return

        # 其他路径
        self._set_headers(404, 'text/plain')
        self.wfile.write(b'Not Found')

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "请求体不是合法 JSON"}).encode('utf-8'))
            return

        if self.path == '/login':
            username = data.get("username")
            password = data.get("password")
            if username and password and users_db.get(username) == password:
                token = f"{username}_token"
                tokens_db.add(token)
                self._set_headers()
                self.wfile.write(json.dumps({"message": "登录成功", "token": token}).encode('utf-8'))
            else:
                self._set_headers(401)
                self.wfile.write(json.dumps({"error": "用户名或密码错误"}).encode('utf-8'))
        else:
            self._set_headers(404, 'text/plain')
            self.wfile.write(b'Not Found')


if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), MyHandler)
    print('✅ Server running at http://0.0.0.0:8000')
    server.serve_forever()
