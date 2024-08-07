from scp.obj import *
from scp.utl import *
from scp.fnc import *

from pygame.locals import *
import pygame as pg

from time import time as tme
from sys import exit as ext

clr = jsn_dat("eng/dat/clr.json")
scn = {}

scn["siz"] = (256, 256)
scn["pix-siz"] = 4

scn["srf"] = pg.Surface(scn["siz"])

scn["win"] = None
scn["win-bck"] = None

siz = (scn["siz"][0] * scn["pix-siz"], scn["siz"][1] * scn["pix-siz"])
txt = txt_utl("eng/dat/fnt.json", scn["srf"])

tme_cal = {}
fps_cal = {}

tme_cal["str"] = tme()
tme_cal["now"] = 0
tme_cal["dlt"] = 0

fps_cal["fps"] = 0
fps_cal["fps-lit"] = []
fps_cal["fps-avg"] = 0

pg.init()
dpy = pg.display.set_mode(siz, DOUBLEBUF)
pg.display.set_caption("Algebra")
fps = pg.time.Clock()

mos_dat = {}

mos_dat["xy"] = [pg.mouse.get_pos()[0] // scn["pix-siz"], pg.mouse.get_pos()[1] // scn["pix-siz"]]
mos_dat["btt"] = [False, False, False]

while True:
    dpy.fill(clr["white"])
    scn["srf"].fill(clr["white"])

    for a in range(2):
        mos_dat["xy"][a] = pg.mouse.get_pos()[a] // scn["pix-siz"]

    tme_cal["now"] = tme()
    tme_cal["dlt"] = (tme_cal["now"] - tme_cal["str"])
    tme_cal["str"] = tme()

    if tme_cal["dlt"] > 1:
        tme_cal["dlt"] = 1

    fps_cal["fps"] = 1 / tme_cal["dlt"]
    fps_cal["fps-lit"].append(fps_cal["fps"])

    if len(fps_cal["fps-lit"]) > round(fps_cal["fps"]):
        fps_cal["fps-lit"].pop(0)
    
    fps_cal["fps-avg"] = round(sum(fps_cal["fps-lit"]) / len(fps_cal["fps-lit"]))
    
    txt.drw(fps_cal["fps-avg"], 1, (1, 1), clr["red"])

    for evt in pg.event.get():
        if evt.type == pg.QUIT:
            pg.quit()
            ext()

        if evt.type == pg.KEYDOWN:            
            if evt.key == pg.K_ESCAPE:
                pg.quit()
                ext()
                        
        if evt.type == pg.MOUSEBUTTONDOWN:
            for a in range(3):
                if evt.button == a + 1:
                    mos_dat["btt"][a] = True

        if evt.type == pg.MOUSEBUTTONUP:
            for a in range(3):
                if evt.button == a + 1:
                    mos_dat["btt"][a] = False
    
    scn["win"] = pg.transform.scale(scn["srf"], siz)
    scn["win-bck"] = pg.transform.scale(scn["srf"], siz)

    scn["win-bck"].set_alpha(51)

    dpy.blit(scn["win"], (0, 0))
    dpy.blit(scn["win-bck"], (scn["pix-siz"], scn["pix-siz"]))

    pg.display.update() 
    pg.display.flip()
    fps.tick(0)