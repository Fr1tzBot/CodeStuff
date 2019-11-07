from os import system
def runshell(maybe):
  if maybe:
    while True:
      a = input(">>")
      if a == "exit":
        break
      else:
        system(a)
    return
  else:
    return
def exe(command, maybe):
  if maybe:
    system(command)
def reset(yes):
  if yes:
    exe("rm -rf /tmp/GradeManager")
  else:
    return