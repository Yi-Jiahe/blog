#!/usr/bin/env python
import re
from datetime import datetime, timezone

def parse_title_to_filename(title):
    # Remove any invalid characters
    title = re.sub(r'[<>:"/\\|?*]', '', title)  # Removes invalid characters
    title = title.strip()  # Strip leading/trailing whitespace

    # Replace spaces with underscores (or you can use hyphens)
    title = title.replace(" ", "_")

    # Convert to lowercase (optional, but can make filenames more consistent)
    title = title.lower()
    return title

def create_post(title):
  now = datetime.now(timezone.utc)

  post_name = f"{now.strftime('%Y-%m-%d')}_{parse_title_to_filename(title)}.md"

  with open(f"content/posts/{post_name}", "w") as f:
    f.write(f"""---
title: "{title}"
date: {now.strftime("%Y-%m-%dT%H:%M:%S%z")}
slug: {int(now.timestamp())}
draft: true
---
""")

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers(dest="command")

  posts_parser = subparsers.add_parser("posts")
  posts_subparsers = posts_parser.add_subparsers(dest="subcommand")

  new_post_parser = posts_subparsers.add_parser("new")
  new_post_parser.add_argument("title")

  args = parser.parse_args()

  if args.command == "posts":
    if args.subcommand == "new":
      create_post(args.title)


