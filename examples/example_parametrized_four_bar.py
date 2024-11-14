import aview_python as avp

MODEL_NAME = "Four_Bar"

POINTS = {
    "O": [0,0,0],
    "A": [0,100,0],
    "B": [200,250,0],
    "C": [200,0,0],
}

LINKS = {
    "OA": ("O","A"),
    "AB": ("A","B"),
    "CB": ("C","B")
}


JOINTS = {
    "J1": ("OA","ground","O"),
    "J2": ("AB","OA","A"),
    "J3": ("AB","CB","B"),
    "J4": ("CB","ground","C")
}

pl = avp.PlanarLinkage(MODEL_NAME, POINTS, LINKS, JOINTS)
pl.create_parametrized_linkage()
