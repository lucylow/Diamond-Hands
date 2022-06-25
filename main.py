import poetry
import requests
from termcolor import cprint


def get_profile(username):
  url = 'https://bitclout.com/api/v0/get-single-profile'
  data = {
   "Username": username,
   "PublicKeyBase58Check": "",
  }
  response = requests.post(url,  json=data)
  print(response.text)
  response_json = response.json()
  print(response_json)


def get_posts(username, last_post_hash_hex):
 url = 'https://bitclout.com/api/v0/get-posts-for-public-key'
 data = {
   "PublicKeyBase58Check": "",
   "Username": "diamond_handz",
   "ReaderPublicKeyBase58Check": "",
   "LastPostHashHex": last_post_hash_hex,
   "NumToFetch": 4,
   "MediaRequired": False
 }
 response = requests.post(url,  json=data)
 response_json = response.json()
 print(response_json)
 if response_json["LastPostHashHex"]:
   last_post_hash_hex = response_json["LastPostHashHex"]
 return response_json["Posts"], last_post_hash_hex

def print_posts(username, last_post_hash_hex):
 posts, last_post_hash_hex = get_posts(username, last_post_hash_hex)
 if not posts:
   return None
 for post in posts:
   print("_" * 30)
   if post["Body"]:
     print(post["Body"])
     if post["RepostedPostEntryResponse"]:
       cprint(post["RepostedPostEntryResponse"]["Body"], 'blue')
   else:
     cprint(post["RepostedPostEntryResponse"]["Body"], 'blue')
 return last_post_hash_hex

def main():
 username = input("Whose posts would you like to see? (type in DeSo username)\n")
 get_profile(username)
 

 last_post_hash_hex = ''
 cprint("*" * 30, "green")
 cprint(f"Posts for {username}", "green")
 cprint("*" * 30, "green")
 while True:
   last_post_hash_hex = print_posts(username, last_post_hash_hex)
   if last_post_hash_hex:
     cprint("If there are more posts, would you like to continue? (Y/N)", "green")
     user_reponse = input("\n")
     if user_reponse[0].upper() != "Y":
       cprint("Goodbye!", 'red')
       break
   else:
     cprint(f"No more posts from {username}.", "red")
     break

main()
