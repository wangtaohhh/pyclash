from PyQt6 import QtWidgets
import sys, os

import yaml_analysis
import airport_group
import subprocess, yaml
import extract_server_choosed, change_group_info, kill_clash
import save_subscribe


# rewrite the class: closeEvent()
class ReQMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ReQMainWindow, self).__init__(parent)

    def closeEvent(self, event):
        kill_clash.kill_process_pid()


class PyClashUI(ReQMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("pyclash")
        self.resize(400, 250)

        self.layout = QtWidgets.QFormLayout()

        self.choose_group = QtWidgets.QComboBox(self)
        # self.choose_server = QtWidgets.QComboBox(self)
        self.choose_server = QtWidgets.QListView(self)
        self.subscription_address = QtWidgets.QLineEdit(self)
        self.upgrade_subscription = QtWidgets.QPushButton("update subscription")
        self.test_speed = QtWidgets.QPushButton("test")
        self.connect = QtWidgets.QPushButton("connect")

        self.layout.setSpacing(30)
        self.layout.addRow('group', self.choose_group)
        self.layout.addRow('server', self.choose_server)
        self.layout.addRow('sub_address', self.subscription_address)
        self.layout.addRow(self.upgrade_subscription)
        self.layout.addRow(self.test_speed)
        self.layout.addRow(self.connect)

        # self.subscription_address.setText("paste your address here")

        self.setLayout(self.layout)

        self.group_list = airport_group.group_name_list
        self.server_list = airport_group.server_info_list

        # add two lists into the combobox
        self.choose_group.addItems(self.group_list)
        self.choose_group.currentIndexChanged.connect(self.return_combobox_index)

        # button signal
        self.connect.clicked.connect(self.run_clash)
        self.upgrade_subscription.clicked.connect(self.request_subscription)

    # logic part
    def return_combobox_index(self) -> int:  # return value in this func is useless

        self.choose_server.clear()
        self.choose_server.addItems(self.server_list[self.choose_group.currentIndex()])

        return self.choose_group.currentIndex()

    def run_clash(self):

        self.server_name_in_combobox = self.choose_server.currentText()
        print(self.server_name_in_combobox, type(self.server_name_in_combobox))
        print("----------------===============================-------------------")

        self.generate_config(self.server_name_in_combobox)
        subprocess.Popen(["clash", "-d", "."])
        self.connect.setEnabled(False)

    def generate_config(
        self, server_list
    ) -> dict:  # return the information dict of the server
        self.server_used = extract_server_choosed.extract_server_info(server_list)
        self.server_group = change_group_info.change_all_proxy_groups(server_list)
        yaml_analysis.airport_data["proxies"] == self.server_used
        yaml_analysis.airport_data["proxy-groups"] == self.server_group
        config_yaml = yaml.dump(yaml_analysis.airport_data, allow_unicode=True)
        with open("config.yaml", "w", encoding='utf8') as write_yaml:
            write_yaml.write(config_yaml)

    def request_subscription(self):
        save_subscribe.save_subscription(self.subscription_address.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyClashUI()
    window.show()

    # sys.exit(app.exec_())
