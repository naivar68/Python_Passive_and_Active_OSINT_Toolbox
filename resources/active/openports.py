from nmap import PortScanner
from database_setup import writeToDB, readFromDB
from datetime import datetime
import subprocess
import pathlib

class OpenPorts:
    def __init__(self, ip):
        self.ip = ip
        self.nmap = PortScanner()
        self.data = self.get_data()
        self.df = self.get_df()
        self.save_data()

    def get_data(self):
        query = input("What ip address are you scanning? ")
        self.nmap.scan(query, arguments="-T1 -sV -p 1-100 --osscan-guess")
        writeToDB.connect()
        c = writeToDB.cursor()
        # save to database
        for host in self.nmap.all_hosts():
            for proto in self.nmap[host].all_protocols():
                lport = self.nmap[host][proto].keys()
                for port in lport:
                    c.execute("INSERT INTO open_ports (ip, port, protocol, state, service, version, product, os) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (host, port, proto, self.nmap[host][proto][port]['state'], self.nmap[host][proto][port]['name'], self.nmap[host][proto][port]['version'], self.nmap[host][proto][port]['product'], self.nmap[host][proto][port]['osmatch']))
        writeToDB.commit()
        writeToDB.close()
        return self.nmap[query]


class runningServices:
    def __init__(self, running_services):
        pass

