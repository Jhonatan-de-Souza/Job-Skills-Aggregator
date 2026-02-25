from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QColor


class ScraperThread(QThread):
    finished = Signal()
    error = Signal(str)

    def __init__(self, callback, job_title):
        super().__init__()
        self._callback = callback
        self._job_title = job_title

    def run(self):
        try:
            self._callback(self._job_title)
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

class JobSearchWindow(QMainWindow):
    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback
        self.setWindowTitle("Job Skills Scraper")
        self.setGeometry(100, 100, 500, 400)
        self.setMinimumWidth(500)
        self.setMinimumHeight(400)
        
        # Set Reddit light theme stylesheet
        self.setStyleSheet(self.get_reddit_stylesheet())
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        
        # Title label
        title_label = QLabel("🔍 Find Your Job")
        title_font = QFont("Helvetica", 28, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("title")
        layout.addWidget(title_label)
        
        # Subtitle
        subtitle_label = QLabel("Search multiple jobs listings")
        subtitle_font = QFont("Helvetica", 11)
        subtitle_label.setFont(subtitle_font)
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setObjectName("subtitle")
        layout.addWidget(subtitle_label)
        
        layout.addSpacing(10)
        
        # Job title label
        job_label = QLabel("Job Title")
        job_font = QFont("Helvetica", 13, QFont.Bold)
        job_label.setFont(job_font)
        job_label.setObjectName("label")
        layout.addWidget(job_label)
        
        # Job title input field
        self.job_entry = QLineEdit()
        self.job_entry.setPlaceholderText("e.g., Software Engineer, Data Scientist")
        self.job_entry.setMinimumHeight(48)
        self.job_entry.setObjectName("input_field")
        entry_font = QFont("Helvetica", 12)
        self.job_entry.setFont(entry_font)
        
        # Add shadow effect to input
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(8)
        shadow.setColor(QColor(0, 0, 0, 15))
        shadow.setOffset(0, 2)
        self.job_entry.setGraphicsEffect(shadow)
        
        layout.addWidget(self.job_entry)
        
        layout.addSpacing(25)
        
        # Search button
        search_button = QPushButton("Search")
        search_button.setMinimumHeight(48)
        search_button.setObjectName("search_button")
        button_font = QFont("Helvetica", 14, QFont.Bold)
        search_button.setFont(button_font)
        search_button.setCursor(Qt.PointingHandCursor)
        
        # Add shadow effect to button
        button_shadow = QGraphicsDropShadowEffect()
        button_shadow.setBlurRadius(8)
        button_shadow.setColor(QColor(255, 69, 0, 30))
        button_shadow.setOffset(0, 4)
        search_button.setGraphicsEffect(button_shadow)
        
        search_button.clicked.connect(self.on_search_click)
        layout.addWidget(search_button)
        
        # Footer
        footer_label = QLabel("Made by Jhonatan de Souza")
        footer_font = QFont("Helvetica", 10)
        footer_label.setFont(footer_font)
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setObjectName("footer")
        layout.addSpacing(20)
        layout.addWidget(footer_label)
        
        layout.addStretch()
        central_widget.setLayout(layout)
    
    @staticmethod
    def get_reddit_stylesheet():
        """Return complete QSS stylesheet with Reddit light theme"""
        return """
        QMainWindow {
            background-color: #ffffff;
        }
        
        QLabel#title {
            color: #030303;
            font-weight: bold;
        }
        
        QLabel#subtitle {
            color: #818384;
            margin: 8px 0px;
        }
        
        QLabel#label {
            color: #030303;
            margin-bottom: 5px;
        }
        
        QLabel#footer {
            color: #818384;
            font-size: 10px;
        }
        
        QLineEdit#input_field {
            background-color: #f6f7f8;
            border: 1px solid #ccc;
            border-radius: 8px;
            color: #030303;
            padding: 12px 14px;
            font-size: 12px;
            selection-background-color: #ff4500;
        }
        
        QLineEdit#input_field:hover {
            background-color: #fafbfc;
            border: 1px solid #b8bbbe;
        }
        
        QLineEdit#input_field:focus {
            border: 2px solid #ff4500;
            background-color: #ffffff;
            outline: none;
        }
        
        QLineEdit#input_field::placeholder {
            color: #818384;
        }
        
        QPushButton#search_button {
            background-color: #ff4500;
            color: #ffffff;
            border: none;
            border-radius: 8px;
            padding: 12px;
            font-weight: bold;
            font-size: 14px;
        }
        
        QPushButton#search_button:hover {
            background-color: #ff5e22;
        }
        
        QPushButton#search_button:pressed {
            background-color: #e63900;
        }
        
        QPushButton#search_button:disabled {
            background-color: #ccc;
            color: #818384;
        }
        """
    
    def on_search_click(self):
        """Handle search button click with animation"""
        job_title = self.job_entry.text().strip()

        if not job_title:
            self.show_error_message("Error", "Please enter a job title")
            return

        sender = self.sender()
        sender.setEnabled(False)
        sender.setText("Searching...")

        self._thread = ScraperThread(self.callback, job_title)
        self._thread.finished.connect(lambda: self._on_scraping_finished(sender))
        self._thread.error.connect(lambda err: self._on_scraping_error(sender, err))
        self._thread.start()

    def _on_scraping_finished(self, button):
        button.setEnabled(True)
        button.setText("Search")

    def _on_scraping_error(self, button, error):
        button.setEnabled(True)
        button.setText("Search")
        self.show_error_message("Error", error)
    
    def show_error_message(self, title, message):
        """Show error message with Reddit styling"""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)
        
        # Style message box
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #ffffff;
            }
            QMessageBox QLabel {
                color: #030303;
            }
            QMessageBox QPushButton {
                background-color: #ff4500;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 6px 16px;
                min-width: 60px;
            }
            QMessageBox QPushButton:hover {
                background-color: #ff5e22;
            }
        """)
        
        msg_box.exec()