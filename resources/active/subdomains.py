import subprocess
from bs4 import BeautifulSoup
from database_setup import writeToDB, read_from_db

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