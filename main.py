from PyQt6.QtCore import QUrl, QByteArray
from PyQt6.QtWidgets import QApplication
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import sys

app = QApplication(sys.argv)

url = QUrl('http://127.0.0.1:8000/')

manager = QNetworkAccessManager()

request = QNetworkRequest(url)
request.setHeader(QNetworkRequest.ContentTypeHeader, 'application/x-www-form-urlencoded')

data = QByteArray()
data.append('title=My%20Post')
data.append('&')
data.append('content=This%20is%20my%20first%20post.')

reply = manager.post(request, data)


def handle_response(reply: QNetworkReply):
    if reply.error() == QNetworkReply.NoError:
        print('Post created successfully')
    else:
        print('Error:', reply.errorString())
    app.quit()


reply.finished.connect(handle_response)

sys.exit(app.exec())