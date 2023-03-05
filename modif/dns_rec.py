import dns.resolver, os
from colorama import Fore, init
init()

def dns_rec():
	os.system('cls')
	target_domain=input(Fore.GREEN + 'Enter domain: ' + Fore.CYAN)
	record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
	resolver = dns.resolver.Resolver()
	print()
	for record_type in record_types:
		try:
			answer = resolver.resolve(target_domain, record_type)
		except dns.resolver.NoAnswer:
			continue
		print(Fore.YELLOW + f"{record_type} records {target_domain}:")
		for rdata in answer:
			print(f'{rdata}')
	input(Fore.GREEN + "\nDone, press Enter to continue... ")