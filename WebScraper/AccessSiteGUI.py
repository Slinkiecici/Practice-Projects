import random
import wx
import os
from AccessSite import SiteActions
import wx.grid as gridlib

class InterfaceScraper(wx.Panel):
    """Class holding all GUI info for AccessSite.py.
    The application takes a file input in .xlsx format downloaded from odoo server
    The application then uses Internal Ref to scrape the Siemens Mall website with login details provided in seperate credentials file
    The GUI displays all products processed and determines whetehr they were successfully scraped or not"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundColour("#F5F5F5")
        self.site_action = SiteActions()                                                            #Create Instance of class in AccessSite.py
        self.scraper_page()
    
    def scraper_page(self):
        #Elements to be used in GUI created
        self.file_to_scrape_button = wx.Button(self, label="Choose file to scrape")
        heading = wx.StaticText(self, id = 1, label = "WebScraper", style = wx.ALIGN_CENTER)
        self.successful_parts = wx.TextCtrl(self, size = (200,100),style = wx.TE_MULTILINE | wx.TE_READONLY)
        self.failed_parts = wx.TextCtrl(self, size = (200,100),style = wx.TE_MULTILINE | wx.TE_READONLY)
        self.sheet_name_label = wx.StaticText(self, label = "Please provide file name to save to(.xlsx): ")
        self.sheet_name = wx.TextCtrl(self)
        self.scrape_outcome_label = wx.StaticText(self, label = " ")
        success_label = wx.StaticText(self, id = 1, label = "Successfully Scraped Products", style = wx.ALIGN_CENTER)
        failed_label = wx.StaticText(self, id = 1, label = "Unsuccessful Products", style = wx.ALIGN_CENTER)
        self.file_label = wx.StaticText(self, id = 1, label = "File name will appear here", style = wx.ALIGN_CENTER)
        
        #Formatting of font for text below
        font = wx.Font(18, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
        heading.SetFont(font)

        #Elements added to relevant sizers for layout to be readable
        sizer = wx.BoxSizer(wx.VERTICAL)
        parts_processed_successful_sizer = wx.BoxSizer(wx.VERTICAL)
        parts_processed_failed_sizer = wx.BoxSizer(wx.VERTICAL)
        parts_processed_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sheet_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(heading, 0, wx.CENTER, 10)
        parts_processed_failed_sizer.Add(failed_label, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        parts_processed_successful_sizer.Add(success_label, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        parts_processed_successful_sizer.Add(self.successful_parts, 0, wx.ALL, 10)
        parts_processed_failed_sizer.Add(self.failed_parts, 0, wx.ALL, 10)
        
        
        parts_processed_sizer.Add(parts_processed_successful_sizer, 0, wx.ALL, 10)
        parts_processed_sizer.Add(parts_processed_failed_sizer, 0, wx.ALL, 10)
        sheet_sizer.Add(self.sheet_name_label, 0, wx.ALL, 10)
        sheet_sizer.Add(self.sheet_name, 0, wx.ALL, 10)

        sizer.Add(parts_processed_sizer, 0, wx.ALL, 10)
        sizer.Add(self.file_to_scrape_button, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)
        sizer.Add(self.file_label, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)  
        sizer.Add(sheet_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)
        sizer.Add(self.scrape_outcome_label, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)   
        self.file_to_scrape_button.Bind(wx.EVT_BUTTON, self.on_click_file_chooser)                  #Binding button to on_click_file_chooser which executes relevant code in AccessSite.py
        self.SetSizer(sizer)


    def on_click_file_chooser(self, e): 
        wildcard = "Text Files (*.xlsx)|*.xlsx"                                                     #Ensure only files with .xlsx suffix is displayed
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)
        user_file_name = self.sheet_name.GetValue()
        if len(user_file_name) > 1:
            if user_file_name.endswith(".xlsx"):                                                    #Ensuring file extention is correct
                print (user_file_name)
            else:
                user_file_name = user_file_name + ".xlsx"
                print (user_file_name)
            if dlg.ShowModal() == wx.ID_OK:
                paths = dlg.GetPaths()
                for path in paths:
                    self.file_label.SetLabel(path)
                    self.site_action.compile_list_for_scrape(path)
                    for named in self.site_action.failed:
                        self.failed_parts.AppendText(str(named)+ "\n")                              #take all failed products and add them to the failed textctrl (from list in accessite)
                    for named in self.site_action.success:
                        self.successful_parts.AppendText(str(named)+ "\n")                          #take all successful products and add them to the successful textctrl (from list in accessite)
            self.site_action.write_to_excel(user_file_name)
            self.scrape_outcome_label.SetLabel("Successfully scraped product details have been saved to " + str(user_file_name))    #Final line if all else is executed successfully
        elif self.sheet_name_label.GetLabel() == ("PLEASE! A FILE NAME FIRST SIR!"):                #raise exception if no file name is entered
            self.sheet_name_label.SetLabel("PLEASE! YOU CAN NAME IT WHATEVER!")                     #raise exception if no file name is entered (BEING EXTRA SASS!)
        else: 
            self.sheet_name_label.SetForegroundColour(wx.Colour(255,0,0))
            self.sheet_name_label.SetLabel("PLEASE! A FILE NAME FIRST SIR!")                
        dlg.Destroy()

class InterfaceOdoo(wx.Panel):
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundColour("#F5F5F5")
        self.odoo_access_page()
    
    def odoo_access_page(self):
        #Elements to be used in GUI created
        heading = wx.StaticText(self, id = 1, label = "Inventory Access", style = wx.ALIGN_CENTER)
        product_grid_label = wx.StaticText(self, id = 1, label = "Product Details", style = wx.ALIGN_CENTER)
        self.inventory_list = gridlib.Grid(self)
        self.inventory_list.CreateGrid(5,5)

        self.product_name = wx.TextCtrl(self)
        self.search_intput_button = wx.Button(self, label="search")

        self.inventory_list.SetColLabelValue(0, "Stock Code")
        self.inventory_list.SetColLabelValue(1, "Description")
        self.inventory_list.SetColLabelValue(2, "List Price")
        self.inventory_list.SetColLabelValue(3, "Customer price")
        self.inventory_list.SetColLabelValue(4, "Quantity")

        #self.sheet_name_label = wx.StaticText(self, label = "Please provide file name to save to(.xlsx): ")
        
        #Formatting of font for text below
        font = wx.Font(18, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
        heading.SetFont(font)

        #Elements added to relevant sizers for layout to be readable
        sizer = wx.BoxSizer(wx.VERTICAL)
        search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(heading, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)
        sizer.Add(product_grid_label, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)  
        sizer.Add(self.inventory_list, 0, wx.ALL, 20)
        search_sizer.Add(self.product_name, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)
        search_sizer.Add(self.search_intput_button, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)   
        sizer.Add(search_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)
        self.SetSizer(sizer)

class MainApplication(wx.Frame):
    """
    Frame that holds all other widgets and panels, base of application.
    """

    def __init__(self):
        """Constructor"""        
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Stock Management",
                          size=(600,400)
                          )
        panel = wx.Panel(self)

        notebook = wx.Notebook(panel)
        tabOne = InterfaceScraper(notebook)
        notebook.AddPage(tabOne, "Price Updater")

        tabTwo = InterfaceOdoo(notebook)
        notebook.AddPage(tabTwo, "Inventory")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()

        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainApplication()
    app.MainLoop()