#!/usr/bin/env python
# (c) 2011 Jrabbit Under GPL v3 or later.
from github import Github
github = Github()
def do_search(term='Chimera'):
    repositories = github.legacy_search_repos(term)
    lang_count= {}
    desc = []
    urls = []
    for repo in repositories:
        lang_count[repo.language] = lang_count.get(repo.language, 0) +1
        urls.append(repo.url)
        desc.append(repo.description)
    return lang_count, urls, desc

if __name__ == '__main__':
    import sys
    langs, urls, desc = do_search(sys.argv[1])
    print langs
    for k,v in zip(desc, urls):
        print k, v
