import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import time

class Charts:
    def __init__(self, username):
        self.username = username
        self.conn = sqlite3.connect('recon.db')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS UserNotes (Charts glob, Chart_Graphic TEXT)")
        self.conn.commit()
        self.conn.close()

    def chart(self):
        self.conn = sqlite3.connect('recon.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM Charts WHERE Chart_Graphic LIKE ?", (self.username + "_%",))
        charts = self.c.fetchall()
        self.conn.close()
        return charts

    def chart_data(self, chart_name):
        self.conn = sqlite3.connect('recon.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT Chart_Graphic FROM Charts WHERE Chart_Graphic = ?", (chart_name,))
        chart_data = self.c.fetchall()
        self.conn.close()
        return chart_data

    def create_chart(self, chart_name, chart_data):
        self.conn = sqlite3.connect('recon.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO Charts (Chart_Graphic, Chart_Data) VALUES (?, ?)", (chart_name, chart_data))
        self.conn.commit()
        self.conn.close()
        return True

    def bar_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='bar')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        time.sleep(2)

    def line_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='line')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        time.sleep(2)

    def scatter_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='scatter')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        time.sleep(2)

    def pie_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='pie')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        time.sleep(2)

    def hist_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='hist')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        time.sleep(2)

    def box_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='box')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        time.sleep(2)

    def area_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='area')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        time.sleep(2)

