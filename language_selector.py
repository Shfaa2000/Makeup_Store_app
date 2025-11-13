from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize


class LanguageDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.selected_language = "en"   # اللغة الافتراضية
        self.setWindowTitle("Choose Language / اختر اللغة")
        self.setWindowIcon(QIcon('images/globe.jpg'))

        # تقليل حجم الواجهة
        self.setFixedSize(300, 250)
        self.setStyleSheet("""
            QDialog {
                background-color: #f9f3f3;
                border-radius: 12px;
            }
            QLabel {
                font-size: 16px;
                color: #4e3b47;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(15)  # تقليل المسافة بين العناصر
        layout.setContentsMargins(15, 15, 15, 15)

        # العنوان الرئيسي
        label = QLabel("Please select your language\nالرجاء اختيار اللغة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setWordWrap(True)
        layout.addWidget(label)

        # مسافة صغيرة أعلى الأزرار
        layout.addSpacerItem(QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # زر العربية مع أيقونة
        arabic_btn = QPushButton("العربية")
        arabic_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        arabic_btn.setIcon(QIcon("images/arabic.svg"))
        arabic_btn.setIconSize(QSize(20, 20))  # تصغير أيقونة الزر
        arabic_btn.setFixedHeight(40)  # تقليل ارتفاع الزر
        arabic_btn.setStyleSheet("""
            QPushButton {
                background-color: #d16b86;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #b3546a;
            }
        """)
        arabic_btn.clicked.connect(self.select_arabic)
        layout.addWidget(arabic_btn)

        # زر الإنجليزية مع أيقونة
        english_btn = QPushButton("English")
        english_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        english_btn.setIcon(QIcon("images/english.svg"))
        english_btn.setIconSize(QSize(20, 20))  # تصغير أيقونة الزر
        english_btn.setFixedHeight(40)
        english_btn.setStyleSheet("""
            QPushButton {
                background-color: #f2d7d9;
                color: #4e3b47;
                font-size: 14px;
                font-weight: bold;
                border-radius: 10px;
                padding: 6px;
                border: 2px solid #d16b86;
            }
            QPushButton:hover {
                background-color: #eac0c5;
            }
        """)
        english_btn.clicked.connect(self.select_english)
        layout.addWidget(english_btn)

        # مسافة أسفل الأزرار
        layout.addSpacerItem(QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(layout)

    def select_arabic(self):
        self.selected_language = "ar"
        self.accept()

    def select_english(self):
        self.selected_language = "en"
        self.accept()
