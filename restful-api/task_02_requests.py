#!/usr/bin/python3
"""
asdfghjkl
"""
import requests
import csv


def fetch_and_print_posts():
    """
    asdfghjkl
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    asdfghjkl
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code == 200:
        posts = r.json()
        data_to_save = []
        for post in posts:
            data_to_save.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })

        with open('posts.csv', 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)
