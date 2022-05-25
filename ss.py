def elevetor(*n):
    diff =0
    up= n.count("^")
    down =n.count("v")
    if up<down:
        diff = down - up
    elif down <up:
        diff = up - down
    print(diff)
elevetor("^v^^v^v^vv^^vvv^^v^^^vv^^^vv^v^^vvv^^^^^v^v^v^v^vv^^vvv^^^^vvv^^vvv^^^^^vv")
name = "^v^^v^v^vv^^vvv^^v^^^vv^^^vv^v^^vvv^^^^^v^v^v^v^vv^^vvv^^^^vvv^^vvv^^^^^vv"
print(name.count("^"))
print(name.count("v"))
