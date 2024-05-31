from nmap import PortScanner
from resources import writeToDB
from datetime import datetime
import subprocess
import pathlib
from bs4 import BeautifulSoup

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

class SubdomainFinder:
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    def find_subdomains(self, domain):
        subdomain_list = []
        potential_subdomains = ['www', 'mail', 'ftp', 'webmail']  # Add more potential subdomains here

        for subdomain in potential_subdomains:
            try:
                # Use subprocess to run curl command
                result = subprocess.run(['curl', '-A', self.headers['User-Agent'], f"https://{subdomain}.{domain}"], capture_output=True, text=True)
                data = result.stdout
                soup = BeautifulSoup(data, "html.parser")

                for link in soup.find_all('a'):
                    subdomain_url = link.get('href')

                    if subdomain_url and domain in subdomain_url:
                        subdomain_list.append(subdomain_url.split(domain)[1])
                        data = subdomain_url.split(domain)[1]
                        print(data)
                        writeToDB.conn.connect()
                        writeToDB.c.execute("INSERT INTO SubDomains (SubDomainName) VALUES (?)", (data,))
                        writeToDB.conn.commit()
                        writeToDB.conn.close()

            except:
                print(f"Subdomain {subdomain} not found.")
                continue


        return subdomain_list
