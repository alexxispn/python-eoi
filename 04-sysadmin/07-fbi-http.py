import requests

URL = 'https://api.fbi.gov/wanted/v1/list'
space_long = 40
space_short = 20


def get_wanted():
    r = requests.get(URL)
    return r.json()['items']


def print_wanted(wanted):
    for wanted in wanted:
        print(f'{wanted["title"]:{space_long}} - {wanted["description"]}')


def main():
    wanted = get_wanted()
    print_wanted(wanted)


if __name__ == '__main__':
    main()
