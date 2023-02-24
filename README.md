
# IPv4Scanner-POC
**Pv4Scanner-POC is a program that performs a port scan of the entered IP address and automatically downloads a PoC code associated with the vulnerability if a CVE vulnerability exists.**

It was created utilizing the API of motikan2010's [PoC-in-GitHub]([https://poc-in-github.motikan2010.net/](https://poc-in-github.motikan2010.net/)) and the search engine of [Criminal IP]([https://www.criminalip.io](https://www.criminalip.io/)).

You need to create an API key, accessible through a free account at  [criminalip.io](http://criminalip.io/).
  
# Installation  
  
Clone repository:  
  
```  
$ git clone https://github.com/KamilDogo/IPv4Scanner-POC.git  
```  
  
```  
$ cd ipv4scanner-poc
```  
  
```  
$ python3 -m venv .venv  
$ source .venv/bin/activate  
```  
  
```  
$ pip3 install -r requirements.txt  
```  
  
  
  
# Usage  
  
```  
$ python3 ipv4scanner-poc.py --api_key [your-criminalip-api-key]  
```  
  
  
  
# Optional Arguments  
  
| Flag | MetaVar | Usage |  
| -------------- | ----------- | ----------------------------------------------------- |  
| `--api_key` | **API key** | api authentication with a valid [criminalip.io](http://criminalip.io) api key |  
| `--ip` | **Exploit Query** | Return IP data from query and download cve github source code |
