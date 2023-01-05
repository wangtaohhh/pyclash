from PyQt5 import QtWidgets
import sys
import json
import analysis_json


class SaveSubscribeGroup(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.layout = QtWidgets.QFormLayout()

        self.subscription_table = QtWidgets.QTableWidget(self)
        self.subscription_table.setColumnCount(2)
        self.how_many_subscriptions_groups = analysis_json.len_dict
        self.subscription_table.setRowCount(self.how_many_subscriptions_groups)
        self.subscription_table.setHorizontalHeaderLabels(['name','link'])
        self.subscription_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # left & right alignment
        

        for i in range(analysis_json.len_dict):
            self.subscription_table.setItem(i, 0, QtWidgets.QTableWidgetItem(analysis_json.dict_keys[i]))
            self.subscription_table.setItem(i, 1, QtWidgets.QTableWidgetItem(analysis_json.dict_values[i]))


        self.add_subscription_name_line_edit = QtWidgets.QLineEdit()
        self.add_subscription_link_line_edit = QtWidgets.QLineEdit()
        
        
        self.add_subscription_button = QtWidgets.QPushButton('add')


        self.add_subscription_button.clicked.connect(self.add_subscription_button_function)


        self.layout.addRow(self.subscription_table)
        self.layout.addRow('add subscription name: ', self.add_subscription_name_line_edit)
        self.layout.addRow('add subscription link: ', self.add_subscription_link_line_edit)
        self.layout.addWidget(self.add_subscription_button)
        
        self.setLayout(self.layout)

    

    def initUI(self):
        
        self.setWindowTitle('save subscribe')
        self.resize(900, 600)

    

    def add_subscription_button_function(self):
        

        self.subscription_name_for_function = self.add_subscription_name_line_edit.text()
        self.subscription_link_for_function = self.add_subscription_link_line_edit.text()

        self.subscription_dict = {
            str(self.subscription_name_for_function): str(self.subscription_link_for_function)
        }
        self.subscription_json = json.dumps(self.subscription_dict)

        with open('subscription.json', 'r') as f:
            json_airport_content = json.load(f)
        json_airport_content.update(self.subscription_dict)

        with open("subscription.json", 'w') as f:
            json.dump(json_airport_content, f, indent=4)

        self.add_subscription_name_line_edit.setText("")
        self.add_subscription_link_line_edit.setText("")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SaveSubscribeGroup()
    window.show()

    sys.exit(app.exec_())

