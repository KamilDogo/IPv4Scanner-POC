import argparse 
import os
import requests   
import colorama 
import logging
import sys
   

def debug(msg):
    globals()['logger'].debug(str(msg))

class Cip_Github_Downloader() : 

    def __init__(self, api_key = None, ip = None, path = None) : 
        
        self._api_key = api_key
        self._ip = ip
        self._session = requests.Session()
        self._base_url =  'https://api.criminalip.io'  
        self._path = path 
       
        
    def run(self):
        
        if self._api_key and self._ip :   
          
            base_url =  "{}{}".format(self._base_url , '/v1/ip/data') 
            params = {'ip': self._ip}
            headers = {'x-api-key': self._api_key} 
            result = self._session.get(base_url , params=params, headers=headers)  
 
            if result.status_code == 200:
               result = result.json()
               self.download(result)
            else:
                result = None  
 

    def download(self, res = None ):
        if not os.path.exists('{}/download'.format(self._path)):
            os.mkdir('{}/download'.format(self._path)) 
        
        for vd in res['vulnerability']['data']:
            if vd['cve_id']:
                vuln = vd['cve_id'] 
                github_url = motikan_api(vuln)
                if github_url is not None : 
                    output = os.system('cd {}/download && git clone {}'.format(self._path, github_url))
                    if int(output) == 0:
                        print("download success into 'download' folder")  
                    elif int(output) == 32768:
                        print("already exists in 'download' folder") 
                else:
                    print("no data")


                


def motikan_api(cve_id):
    url = 'https://poc-in-github.motikan2010.net/api/v1'  
    params = {'cve_id': cve_id} 
    result = requests.get(url=url, params=params)
    github_url = None 

    if result.status_code == 200:
        result = result.json() 
        if result['pocs']:
            github_url = result['pocs'][0]['html_url'] 

    return github_url       
   
 
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Find database by using criminalip service')
    parser.add_argument('--api_key', help='criminalip api key')
    parser.add_argument('--ip', help='scan an IP') 
    args = parser.parse_args()
    path = os.getcwd()  
 
    if args.api_key:
        api_key = args.api_key  

        if os.path.isfile('{}/.api_key'.format(path)):
            x = input('Do you want to update your api_key? (Y/n) ')
            if x in ['y', 'Y']:
                with open('{}/.api_key'.format(path), 'w') as file:
                    file.write(api_key)
                print('\nSuccessfully updated\n')
            else:
                print('\nCanceled\n')
        else:
            with open('{}/.api_key'.format(path), 'w') as file:
                file.write(api_key)
    else:
        with open('{}/.api_key'.format(path), 'r') as file:
            api_key = file.readline().strip()
            

    downloader = Cip_Github_Downloader(args.api_key, args.ip , path)    
    downloader.run()

   
