import os
import sys
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QDialogButtonBox, QFormLayout, QGridLayout,
                             QHBoxLayout, QLabel, QLineEdit, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout)
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Spider osztály a Scrapy-hoz
class WebSpider(CrawlSpider):
    name = "web_spider"

    def __init__(self, allowed_domains, start_urls, download_delay, depth):
        self.allowed_domains = allowed_domains
        self.start_urls = start_urls
        self.rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]
        self.download_delay = download_delay
        self.depth_limit = depth

    def parse_item(self, response):
        self.logger.info('Parsing: %s', response.url)

# Dialógus ablak osztály a beállítások kiválasztásához
class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)

        self.domains = QLineEdit(self)
        self.urls = QLineEdit(self)
        self.delay = QSpinBox(self)
        self.depth = QSpinBox(self)

        self.domains.setPlaceholderText("Enter allowed domains separated by commas")
        self.urls.setPlaceholderText("Enter start URLs separated by commas")
        self.delay.setSuffix(" seconds")
        self.delay.setMinimum(0)
        self.delay.setMaximum(10)
        self.depth.setMinimum(0)
        self.depth.setMaximum(10)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow(QLabel("Allowed domains:"), self.domains)
        layout.addRow(QLabel("Start URLs:"), self.urls)
        layout.addRow(QLabel("Download delay:"), self.delay)
        layout.addRow(QLabel("Depth limit:"), self.depth)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def settings(self):
        return {
            "allowed_domains": self.domains.text(),
            "start_urls": self.urls.text(),
            "download_delay": self.delay.value(),
            "depth": self.depth.value()
        }

# Fő ablak osztály a letöltések kezeléséhez
class DownloadManager(QDialog):
    def __init__(self, parent=None):
        super(DownloadManager, self).__init__(parent)

        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['URL', 'Status'])

        add_button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        add_button.accepted.connect(self.add_download)
        add_button.rejected.connect(self.reject)

        settings_button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        settings_button.accepted.connect(self.settings_dialog)
        settings_button.rejected.connect(self.reject)

        download_button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        download_button.accepted.connect(self.download)
        download_button.rejected.connect(self.reject)
        
        add_layout = QHBoxLayout()
        add_layout.addWidget(add_button)
        add_layout.addWidget(settings_button)
        add_layout.addWidget(download_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        main_layout.addLayout(add_layout)

        self.setLayout(main_layout)

    def add_download(self):
        url, ok = QLineEdit.getText(QLineEdit(self), "Add download", "URL:")
        if ok and url:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(url))
            self.table.setItem(row, 1, QTableWidgetItem("Queued"))

    def settings_dialog(self):
        dialog = SettingsDialog(self)
        if dialog.exec_():
            settings = dialog.settings()
            row = self.table.rowCount()
            for i in range(row):
                self.table.setItem(i, 1, QTableWidgetItem("Queued"))
            self.download_settings(settings)

    def download_settings(self, settings):
        domains = [d.strip() for d in settings['allowed_domains'].split(",")]
        urls = [u.strip() for u in settings['start_urls'].split(",")]
        process = CrawlerProcess(get_project_settings())
        process.crawl(WebSpider, allowed_domains=domains, start_urls=urls, download_delay=settings['download_delay'], depth=settings['depth'])
        process.start()

    def download(self):
        for row in range(self.table.rowCount()):
            if self.table.item(row, 1).text() == "Queued":
                url = self.table.item(row, 0).text()
                self.table.setItem(row, 1, QTableWidgetItem("Downloading"))
                settings = {"allowed_domains": "", "start_urls": url, "download_delay": 0, "depth": 0}
                self.download_settings(settings)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = DownloadManager()
    manager.show()
    sys.exit(app.exec_())

        
