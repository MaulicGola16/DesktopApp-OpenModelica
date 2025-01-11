import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QGroupBox, QHBoxLayout,
    QVBoxLayout, QLineEdit, QPushButton, QFileDialog, QLabel, QMessageBox
)
from PyQt6.QtCore import QProcess


class OpenModelicaRunner(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("OpenModelica Model Runner")
        self.setGeometry(300, 150, 450, 250)

        # Main Layout
        main_layout = QVBoxLayout()

        # File Selection Box
        file_box = QGroupBox("Executable Selection")
        file_layout = QHBoxLayout()
        self.exe_path_field = QLineEdit()
        self.exe_path_field.setPlaceholderText("Click 'Browse' to select an executable")
        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.select_executable)
        file_layout.addWidget(self.exe_path_field)
        file_layout.addWidget(browse_button)
        file_box.setLayout(file_layout)

        # Simulation Parameters Box
        param_box = QGroupBox("Simulation Parameters")
        param_layout = QGridLayout()
        self.start_time_field = QLineEdit()
        self.start_time_field.setPlaceholderText("Enter start time (0-4)")
        self.stop_time_field = QLineEdit()
        self.stop_time_field.setPlaceholderText("Enter stop time (1-5)")
        param_layout.addWidget(QLabel("Start Time:"), 0, 0)
        param_layout.addWidget(self.start_time_field, 0, 1)
        param_layout.addWidget(QLabel("Stop Time:"), 1, 0)
        param_layout.addWidget(self.stop_time_field, 1, 1)
        param_box.setLayout(param_layout)

        # Run Button
        run_button = QPushButton("Run Simulation")
        run_button.clicked.connect(self.run_simulation)

        # Status Label
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color: green; font-weight: bold;")

        # Add Widgets to Layout
        main_layout.addWidget(file_box)
        main_layout.addWidget(param_box)
        main_layout.addWidget(run_button)
        main_layout.addWidget(self.status_label)

        self.setLayout(main_layout)

    def select_executable(self):
        exe_file, _ = QFileDialog.getOpenFileName(self, "Select Executable File", "", "Executable Files (*.exe)")
        if exe_file:
            self.exe_path_field.setText(exe_file)

    def validate_inputs(self):
        try:
            start_time = int(self.start_time_field.text())
            stop_time = int(self.stop_time_field.text())
        except ValueError:
            QMessageBox.critical(self, "Invalid Input", "Start and Stop times must be integers.")
            return None

        if not (0 <= start_time < stop_time < 5):
            QMessageBox.critical(self, "Invalid Range", "Ensure 0 ≤ Start Time < Stop Time < 5.")
            return None

        exe_path = self.exe_path_field.text().strip()
        if not exe_path:
            QMessageBox.critical(self, "Missing File", "Please select an executable file.")
            return None

        return exe_path, start_time, stop_time

    def run_simulation(self):
        inputs = self.validate_inputs()
        if not inputs:
            return

        exe_path, start_time, stop_time = inputs
        process = QProcess(self)
        process.setProgram(exe_path)
        process.setArguments([str(start_time), str(stop_time)])
        process.start()

        if process.waitForStarted():
            self.status_label.setText("Simulation started successfully!")
            self.status_label.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.status_label.setText("Failed to start the simulation.")
            self.status_label.setStyleSheet("color: red; font-weight: bold;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    runner = OpenModelicaRunner()
    runner.show()
    sys.exit(app.exec())

