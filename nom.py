from github2.client import Github
github = Github()
term = 'Chimera'
def do_search(term):
    repositories = github.repos.search(term)
    lang_count= {}
    desc = []
    urls = []
    for repo in repositories:
        lang_count[repo['language']] = lang_count.get(repo['language'], 0) +1
        
        urls.append(repo['url'])
        desc.append(repo['description'])
    return lang_count, urls, desc

if __name__ == '__main__':
    langs, urls, desc = do_search(term)
    print langs
    for k,v in zip(desc, urls):
        print k, v