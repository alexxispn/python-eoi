import requests

URL = 'https://api.github.com/search/users'
USERNAME = 'alexxispn'
space_long = 40
space_short = 20


def get_user(username):
    r = requests.get(URL, params={'q': username})
    return r.json()['items'][0]


def print_user_info(user):
    for key, value in user.items():
        print(f'{key:{space_short}} = {value}')


def get_repos(user):
    r = requests.get(user['repos_url'])
    return r.json()


def print_repos(repos):
    for repo in repos:
        print(f'{repo["name"]:{space_long}} - {repo["language"]}')


def get_followers(user):
    r = requests.get(user['followers_url'])
    return r.json()


def print_followers(followers):
    for follower in followers:
        print(f'{follower["login"]:{space_short}} - {follower["html_url"]}')


def get_following(user):
    r = requests.get(user['following_url'].replace('{/other_user}', ''))
    return r.json()


def print_following(following):
    for follow in following:
        print(f'{follow["login"]:{space_short}} - {follow["html_url"]}')


def get_starred(user):
    r = requests.get(user['starred_url'].replace('{/owner}{/repo}', ''))
    return r.json()


def print_starred(starred):
    for star in starred:
        print(f'{star["name"]:{space_long}} - {star["html_url"]}')


def main():
    user = get_user(USERNAME)
    print_user_info(user)
    print()
    print('Repos:')
    repos = get_repos(user)
    print_repos(repos)
    print()
    print('Followers:')
    followers = get_followers(user)
    print_followers(followers)
    print()
    print('Following:')
    following = get_following(user)
    print_following(following)
    print()
    print('Starred:')
    starred = get_starred(user)
    print_starred(starred)


if __name__ == '__main__':
    main()
