#!/usr/bin/python

###printing one by one, separately

# for i in range(1, 20):
#    for j in range(1, i):
#        print(f"*", end="")
#    print("")

# -----------------------------------------------------------------

# for i in range(20, 1, -1):
#    for j in range(i, 1, -1):
#        print(f"*", end="")
#    print()

# -------------------------------------------------------------------

# for i in range(20, 1, -1):
#    for k in range(0, 20 - i):
#        print(" ", end="")

#    for j in range(i, 1, -1):
#        print(f"*", end="")
#    print()
# --------------------------------------------------------------------

# for i in range(1, 20):
#    for j in range(0, 20 - i):
#        print(f" ", end="")

#    for k in range(0, i):
#        print(f"*", end="")

#    print()

# ---------------------------------------------------------------------
#### 90 degree triangle
##### print all of them in one go

for i in range(1, 12):
    for j in range(0, i):
        print(f"*", end="")
    for k in range(0, 12 - i):
        print(f" ", end="")

    print(f"\t\t", end="")

    for x in range(12, i, -1):
        print(f"*", end="")
    for z in range(0, i):
        print(f" ", end="")

    print(f"\t\t", end="")

    for b in range(0, i):
        print(f" ", end="")
    for k in range(0, 12 - i):
        print("*", end="")

    print(f"\t\t", end="")

    for a in range(12 - i, 1, -1):
        print(f" ", end="")
    for c in range(0, i):
        print(f"*", end="")

    print()




