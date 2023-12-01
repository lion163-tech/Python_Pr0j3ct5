from pathlib import Path

path = Path('new.txt')
init = path.read_text()
sth = str(input('Say something:'))
print(init)
newinit = path.write_text(sth)
print(newinit)