import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap


class MapWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MapView")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        label = QLabel('Введите в консоль координаты x потом координаты z', self)
        label.move(0, 0)

        self.map_label = QLabel()
        self.layout.addWidget(self.map_label)

        self.setLayout(self.layout)

        #self.show_map(float(input()), float(input()), 10)

    def show_map(self, lat, lon, scale):
        url = f"https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&size=650,450&z={scale}&l=map"
        response = requests.get(url)

        with open("map.png", "wb") as file:
            file.write(response.content)

        pixmap = QPixmap("map.png")
        self.map_label.setPixmap(pixmap)
        self.map_label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())
