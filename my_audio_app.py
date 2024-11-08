import sys
import os
import whisper
import ffmpeg
import warnings
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QFileDialog, QLabel, QProgressBar, QMessageBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal

# Suppress warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Worker Thread for Transcription
class TranscriptionWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(bool)

    def __init__(self, video_file, output_file, language):
        super().__init__()
        self.video_file = video_file
        self.output_file = output_file
        self.language = language

    def run(self):
        try:
            # Step 1: Extract audio from video
            audio_file = "output_audio.wav"
            ffmpeg.input(self.video_file).output(audio_file).run(overwrite_output=True, quiet=True)
            self.progress.emit(50)

            # Step 2: Transcribe audio using Whisper
            model = whisper.load_model("base")
            result = model.transcribe(audio_file, language=self.language)

            with open(self.output_file, "w", encoding="utf-8") as f:
                f.write(result["text"])

            self.progress.emit(100)
            self.finished.emit(True)

            # Cleanup audio file
            os.remove(audio_file)
        except Exception as e:
            print(f"Error: {e}")
            self.finished.emit(False)

# Main Application Window
class TranscriptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video to Text Transcription App')
        layout = QVBoxLayout()

        # Button to select video file
        self.video_label = QLabel('Select video file:')
        layout.addWidget(self.video_label)

        self.select_video_btn = QPushButton('Browse Video')
        self.select_video_btn.clicked.connect(self.select_video_file)
        layout.addWidget(self.select_video_btn)

        # Button to select output text file
        self.output_label = QLabel('Select output file:')
        layout.addWidget(self.output_label)

        self.select_output_btn = QPushButton('Browse Output File')
        self.select_output_btn.clicked.connect(self.select_output_file)
        layout.addWidget(self.select_output_btn)

        # Progress Bar
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        # Button to start transcription
        self.start_btn = QPushButton('Start Transcription')
        self.start_btn.clicked.connect(self.start_transcription)
        layout.addWidget(self.start_btn)

        self.setLayout(layout)

    def select_video_file(self):
        self.video_file, _ = QFileDialog.getOpenFileName(self, 'Select Video File', '', 'Video Files (*.mp4 *.mov *.avi *.mkv)')
        if self.video_file:
            self.video_label.setText(f'Video File: {self.video_file}')

    def select_output_file(self):
        self.output_file, _ = QFileDialog.getSaveFileName(self, 'Save Output File', '', 'Text Files (*.txt)')
        if self.output_file:
            self.output_label.setText(f'Output File: {self.output_file}')

    def start_transcription(self):
        if hasattr(self, 'video_file') and hasattr(self, 'output_file'):
            language = "en"  # You can modify this to support other languages, or add a dropdown for user selection
            self.worker = TranscriptionWorker(self.video_file, self.output_file, language)
            self.worker.progress.connect(self.update_progress)
            self.worker.finished.connect(self.on_finished)
            self.worker.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def on_finished(self, success):
        if success:
            QMessageBox.information(self, 'Success', 'Transcription completed successfully!')
        else:
            QMessageBox.critical(self, 'Error', 'Transcription failed!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TranscriptionApp()
    window.show()
    sys.exit(app.exec_())
