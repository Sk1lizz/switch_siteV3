import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from design import Ui_MainWindow

from switch import switch_on, switch_off, switch_add, switch_delete, filter_site
import switch 

import config as cfg

sitelist_i = []

sitelist_text = switch.site_list()

sitelist_split = sitelist_text.split("\n")

for i in range(1, (len(sitelist_split)-1)):
    sitelist_i.append(sitelist_split[i])



class Program(QMainWindow):
    page = 1 
    sitelist = []
    def __init__(self):
        super(Program, self).__init__()
        self.sitelist = sitelist_i
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.site_list()

        self.ui.add_site.setText(cfg.btn_add_site)
        self.ui.add_site.setShortcut("RETURN")

        if self.get_program():
                self.ui.btn_adctivate.setText(cfg.btn_deactivate)
        self.ui.btn_adctivate.setText(cfg.btn_activate)
        self.ui.btn_list_site.setText(cfg.btn_update_list)
        
        if len(self.sitelist) > 5:   self.ui.btn_next_page.setEnabled(True) 
        self.ui.btn_become_page.setEnabled(False)

        self.ui.add_site.clicked.connect(self.add_site_list)
        self.ui.btn_list_site.clicked.connect(lambda: self.update_list(1))
        self.ui.btn_next_page.clicked.connect(lambda: self.set_site(self.page+1))
        self.ui.btn_become_page.clicked.connect(lambda: self.set_site(self.page-1))
        self.ui.btn_delete_site_1.clicked.connect(lambda: self.delete_site(page=self.page, number=1))
        self.ui.btn_delete_site_2.clicked.connect(lambda: self.delete_site(page=self.page, number=2))
        self.ui.btn_delete_site_3.clicked.connect(lambda: self.delete_site(page=self.page, number=3))
        self.ui.btn_delete_site_4.clicked.connect(lambda: self.delete_site(page=self.page, number=4))
        self.ui.btn_delete_site_5.clicked.connect(lambda: self.delete_site(page=self.page, number=5))
        self.ui.btn_adctivate.clicked.connect(self.program)
    
    def add_site_list(self) -> None:
        if self.ui.le_site_rq.text() != "":
            #print(self.ui.le_site_rq.text())
            site = self.ui.le_site_rq.text()
            self.ui.le_site_rq.setText("")
            
            #print(switch_add(site))

            self.sitelist.append(filter_site(site))

            self.site_list()
    
    def site_list(self) -> None:
        list_i = {}
        first_int = 1
        second_int = 6
        count = 0

        self.page = 1

        self.ui.btn_become_page.setEnabled(False)

        for i in range(first_int, second_int):
            if (i >= first_int) and (i <= (5)):
                try: 
                    list_i[f"{count+1}"] = f"{self.sitelist[i-1]}"
                    count += 1
                    self.ui.btn_next_page.setEnabled(True)
                    if (second_int > len(self.sitelist)):
                        self.ui.btn_next_page.setEnabled(False)
                        self.ui.btn_become_page.setEnabled(True)

                except:
                    list_i[f"{count+1}"] = ""
                    count += 1
                    self.ui.btn_next_page.setEnabled(False)
        #print(list_i)
        self.ui.lbl_site_list_1.setText(list_i["1"])
        self.ui.lbl_site_list_2.setText(list_i["2"])
        self.ui.lbl_site_list_3.setText(list_i["3"])
        self.ui.lbl_site_list_4.setText(list_i["4"])
        self.ui.lbl_site_list_5.setText(list_i["5"])
        if list_i["1"] == "":
            self.ui.btn_delete_site_1.setText("")
            self.ui.btn_delete_site_2.setText("")
            self.ui.btn_delete_site_3.setText("")
            self.ui.btn_delete_site_4.setText("")
            self.ui.btn_delete_site_5.setText("")
                
            self.ui.btn_delete_site_1.setEnabled(False)
            self.ui.btn_delete_site_2.setEnabled(False)
            self.ui.btn_delete_site_3.setEnabled(False)
            self.ui.btn_delete_site_4.setEnabled(False)
            self.ui.btn_delete_site_5.setEnabled(False)

        elif list_i["2"] == "":
            self.ui.btn_delete_site_1.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_2.setText("")
            self.ui.btn_delete_site_3.setText("")
            self.ui.btn_delete_site_4.setText("")
            self.ui.btn_delete_site_5.setText("")

            self.ui.btn_delete_site_1.setEnabled(True)
            self.ui.btn_delete_site_2.setEnabled(False)
            self.ui.btn_delete_site_3.setEnabled(False)
            self.ui.btn_delete_site_4.setEnabled(False)
            self.ui.btn_delete_site_5.setEnabled(False)

        elif list_i["3"] == "":
            self.ui.btn_delete_site_1.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_2.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_3.setText("")
            self.ui.btn_delete_site_4.setText("")
            self.ui.btn_delete_site_5.setText("")

            self.ui.btn_delete_site_1.setEnabled(True)
            self.ui.btn_delete_site_2.setEnabled(True)
            self.ui.btn_delete_site_3.setEnabled(False)
            self.ui.btn_delete_site_4.setEnabled(False)
            self.ui.btn_delete_site_5.setEnabled(False)
            
        elif list_i["4"] == "":
            self.ui.btn_delete_site_1.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_2.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_3.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_4.setText("")
            self.ui.btn_delete_site_5.setText("")

            self.ui.btn_delete_site_1.setEnabled(True)
            self.ui.btn_delete_site_2.setEnabled(True)
            self.ui.btn_delete_site_3.setEnabled(True)
            self.ui.btn_delete_site_4.setEnabled(False)
            self.ui.btn_delete_site_5.setEnabled(False)
            
                
        elif list_i["5"] == "":
            self.ui.btn_delete_site_1.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_2.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_3.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_4.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_5.setText("")
                
            self.ui.btn_delete_site_1.setEnabled(True)
            self.ui.btn_delete_site_2.setEnabled(True)
            self.ui.btn_delete_site_3.setEnabled(True)
            self.ui.btn_delete_site_4.setEnabled(True)
            self.ui.btn_delete_site_5.setEnabled(False)
            
        else: 
            self.ui.btn_delete_site_1.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_2.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_3.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_4.setText(cfg.btn_delete_site)
            self.ui.btn_delete_site_5.setText(cfg.btn_delete_site)

            self.ui.btn_delete_site_1.setEnabled(True)
            self.ui.btn_delete_site_2.setEnabled(True)
            self.ui.btn_delete_site_3.setEnabled(True)
            self.ui.btn_delete_site_4.setEnabled(True)
            self.ui.btn_delete_site_5.setEnabled(True)

        self.page = 1
    
    def set_site(self, page: int) -> None:
        #print("2", self.sitelist)
        if page >= 1:
            list_i = {}
            first_int = page*5 - 4
            second_int = first_int + 5
            count = 0

            self.page = page


            if page == 1:
                self.ui.btn_become_page.setEnabled(False)
            else:
                self.ui.btn_become_page.setEnabled(True)

            for i in range(first_int, second_int):
                if (i >= first_int) and (i <= (5*page)):
                    try: 
                        list_i[f"{count+1}"] = f"{self.sitelist[i-1]}"
                        count += 1
                        self.ui.btn_next_page.setEnabled(True)
                        if (second_int > len(self.sitelist)):
                            self.ui.btn_next_page.setEnabled(False)
                            self.ui.btn_become_page.setEnabled(True)

                    except:
                        list_i[f"{count+1}"] = ""
                        count += 1
                        self.ui.btn_next_page.setEnabled(False)
            #print(list_i)
            self.ui.lbl_site_list_1.setText(list_i["1"])
            self.ui.lbl_site_list_2.setText(list_i["2"])
            self.ui.lbl_site_list_3.setText(list_i["3"])
            self.ui.lbl_site_list_4.setText(list_i["4"])
            self.ui.lbl_site_list_5.setText(list_i["5"])
            if list_i["1"] == "":
                self.ui.btn_delete_site_1.setText("")
                self.ui.btn_delete_site_2.setText("")
                self.ui.btn_delete_site_3.setText("")
                self.ui.btn_delete_site_4.setText("")
                self.ui.btn_delete_site_5.setText("")
                
                self.ui.btn_delete_site_1.setEnabled(False)
                self.ui.btn_delete_site_2.setEnabled(False)
                self.ui.btn_delete_site_3.setEnabled(False)
                self.ui.btn_delete_site_4.setEnabled(False)
                self.ui.btn_delete_site_5.setEnabled(False)

            elif list_i["2"] == "":
                self.ui.btn_delete_site_1.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_2.setText("")
                self.ui.btn_delete_site_3.setText("")
                self.ui.btn_delete_site_4.setText("")
                self.ui.btn_delete_site_5.setText("")

                self.ui.btn_delete_site_1.setEnabled(True)
                self.ui.btn_delete_site_2.setEnabled(False)
                self.ui.btn_delete_site_3.setEnabled(False)
                self.ui.btn_delete_site_4.setEnabled(False)
                self.ui.btn_delete_site_5.setEnabled(False)

            elif list_i["3"] == "":
                self.ui.btn_delete_site_1.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_2.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_3.setText("")
                self.ui.btn_delete_site_4.setText("")
                self.ui.btn_delete_site_5.setText("")

                self.ui.btn_delete_site_1.setEnabled(True)
                self.ui.btn_delete_site_2.setEnabled(True)
                self.ui.btn_delete_site_3.setEnabled(False)
                self.ui.btn_delete_site_4.setEnabled(False)
                self.ui.btn_delete_site_5.setEnabled(False)
            
            elif list_i["4"] == "":
                self.ui.btn_delete_site_1.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_2.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_3.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_4.setText("")
                self.ui.btn_delete_site_5.setText("")

                self.ui.btn_delete_site_1.setEnabled(True)
                self.ui.btn_delete_site_2.setEnabled(True)
                self.ui.btn_delete_site_3.setEnabled(True)
                self.ui.btn_delete_site_4.setEnabled(False)
                self.ui.btn_delete_site_5.setEnabled(False)
            
                
            elif list_i["5"] == "":
                self.ui.btn_delete_site_1.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_2.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_3.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_4.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_5.setText("")
                
                self.ui.btn_delete_site_1.setEnabled(True)
                self.ui.btn_delete_site_2.setEnabled(True)
                self.ui.btn_delete_site_3.setEnabled(True)
                self.ui.btn_delete_site_4.setEnabled(True)
                self.ui.btn_delete_site_5.setEnabled(False)
            
            else: 
                self.ui.btn_delete_site_1.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_2.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_3.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_4.setText(cfg.btn_delete_site)
                self.ui.btn_delete_site_5.setText(cfg.btn_delete_site)

                self.ui.btn_delete_site_1.setEnabled(True)
                self.ui.btn_delete_site_2.setEnabled(True)
                self.ui.btn_delete_site_3.setEnabled(True)
                self.ui.btn_delete_site_4.setEnabled(True)
                self.ui.btn_delete_site_5.setEnabled(True)
    
    def delete_site(self, page: int, number: int) -> None:
        site_number = (page-1)*5+number
        switch_delete(self.sitelist[site_number-1])
        self.update_list(1)
    
    def update_list(self, page: int) -> None:
        if page >= 1:
            sitelist_i = []

            sitelist_text = switch.site_list()
            sitelist_split = sitelist_text.split("\n")
            for i in range(1, (len(sitelist_split)-1)):
                sitelist_i.append(sitelist_split[i])
            self.sitelist = sitelist_i
            #print("1:", self.sitelist)
            self.set_site(page=page)

    def get_program(self) -> bool:
        import json
        with open(r"files\config\current_state.json", "r", encoding='utf-8') as file:
            data = json.load(file)
        
        state = data["state"]
        return bool(state)
    
    def program(self) -> None:
        if (self.get_program()):
            switch_off()
            self.ui.btn_adctivate.setText(cfg.btn_activate)
            #print(self.get_program())
            #print()
        else:
            switch_on()
            self.ui.btn_adctivate.setText(cfg.btn_deactivate)
            #print(self.get_program())
            #print()

app = QApplication(sys.argv)

window = Program()
window.show()

sys.exit(app.exec())
