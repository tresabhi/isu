#!/usr/bin/env python


from pyhyp import pyHyp
import numpy
from pyspline import *


prefix = './profiles/'
airfoilProfilePS = prefix + 'NACA4412_lower.txt'
airfoilProfileSS = prefix + 'NCAA4412_upper.txt'
ZSpan = 0.1
nSpan = 2
dX1PS = 0.005
Alpha1PS = 1.2
dX2PS = 0.002
Alpha2PS = 1.2
dXMaxPS = 0.02

dX1SS = 0.005
Alpha1SS = 1.2
dX2SS = 0.002
Alpha2SS = 1.2
dXMaxSS = 0.02

NpTE = 5

NpExtrude = 32
yWall = 0.004
marchDist = 20



fPS = open(airfoilProfilePS, 'r')
linesPS = fPS.readlines()
fPS.close()
xPS = []
yPS = []
zPS = []
for line in linesPS:
    cols = line.split()
    xPS.append(float(cols[0]))
    yPS.append(float(cols[1]))

for i in range(len(xPS)):
    zPS.append(0.0)

fSS = open(airfoilProfileSS, 'r')
linesSS = fSS.readlines()
fSS.close()
xSS = []
ySS = []
zSS = []
for line in linesSS:
    cols = line.split()
    xSS.append(float(cols[0]))
    ySS.append(float(cols[1]))
for i in range(len(xSS)):
    zSS.append(0.0)



tmp = dX1PS
for i in range(1000):
    if tmp > dXMaxPS:
        nStretch1PS = i
        break
    else:
        tmp = tmp * Alpha1PS
tmp = dX2PS
for i in range(1000):
    if tmp > dXMaxPS:
        nStretch2PS = i
        break
    else:
        tmp = tmp * Alpha2PS

xLPSConst = xPS[-1]
xLPS1 = 0
xLPS2 = 0
for i in range(nStretch1PS):
    xLPS1 += dX1PS * (Alpha1PS ** i)
    xLPSConst -= dX1PS * (Alpha1PS ** i)
for i in range(nStretch2PS):
    xLPS2 += dX2PS * (Alpha2PS ** i)
    xLPSConst -= dX2PS * (Alpha2PS ** i)
nXConstPS = int(xLPSConst / dXMaxPS)
dXMaxPS = xLPSConst / nXConstPS

xInterpPS = [0]
tmp = dX1PS
for i in range(nStretch1PS):
    xInterpPS.append(xInterpPS[-1] + tmp)
    tmp = tmp * Alpha1PS
for i in range(nXConstPS):
    xInterpPS.append(xInterpPS[-1] + dXMaxPS)
tmp = dX2PS * (Alpha2PS ** (nStretch2PS - 1))
for i in range(nStretch2PS):
    xInterpPS.append(xInterpPS[-1] + tmp)
    tmp /= Alpha2PS
c1PS = pySpline.Curve(x=xPS, y=yPS, z=zPS, k=3)
XPS = c1PS(xInterpPS)
c2PS = pySpline.Curve(X=XPS, k=3)
x1PS = c2PS.X[:, 0]
y1PS = c2PS.X[:, 1]



tmp = dX1SS
for i in range(1000):
    if tmp > dXMaxSS:
        nStretch1SS = i
        break
    else:
        tmp = tmp * Alpha1SS
tmp = dX2SS
for i in range(1000):
    if tmp > dXMaxSS:
        nStretch2SS = i
        break
    else:
        tmp = tmp * Alpha2SS

xLSSConst = xSS[-1]
xLSS1 = 0
xLSS2 = 0
for i in range(nStretch1SS):
    xLSS1 += dX1SS * (Alpha1SS ** i)
    xLSSConst -= dX1SS * (Alpha1SS ** i)
for i in range(nStretch2SS):
    xLSS2 += dX2SS * (Alpha2SS ** i)
    xLSSConst -= dX2SS * (Alpha2SS ** i)
nXConstSS = int(xLSSConst / dXMaxSS)
dXMaxSS = xLSSConst / nXConstSS

xInterpSS = [0]
tmp = dX1SS
for i in range(nStretch1SS):
    xInterpSS.append(xInterpSS[-1] + tmp)
    tmp = tmp * Alpha1SS
for i in range(nXConstSS):
    xInterpSS.append(xInterpSS[-1] + dXMaxSS)
tmp = dX2SS * (Alpha2SS ** (nStretch2SS - 1))
for i in range(nStretch2SS):
    xInterpSS.append(xInterpSS[-1] + tmp)
    tmp /= Alpha2SS
c1SS = pySpline.Curve(x=xSS, y=ySS, z=zSS, k=3)
XSS = c1SS(xInterpSS)
c2SS = pySpline.Curve(X=XSS, k=3)
x1SS = c2SS.X[:, 0]
y1SS = c2SS.X[:, 1]

delta_y = numpy.linspace(y1PS[-1], y1SS[-1], NpTE, 'd')
delta_y = delta_y[1:]
delta_x = numpy.ones_like(delta_y, 'd')
for i in range(len(delta_x)):
    delta_x[i] = x1SS[-1]

x1SS_Flip = x1SS[::-1]
xAll = numpy.append(x1SS_Flip, x1PS[1:])
xAll = numpy.append(xAll, delta_x)

y1SS_Flip = y1SS[::-1]
yAll = numpy.append(y1SS_Flip, y1PS[1:])
yAll = numpy.append(yAll, delta_y)


print('nPoints for PS: ', nStretch1PS + nStretch2PS + nXConstPS)
print('nPoints for SS: ', nStretch1SS + nStretch2SS + nXConstSS)
print('nPoints for TE: ', NpTE)
print('nPoints Total: ', nStretch1PS + nStretch2PS + nXConstPS + nStretch1SS + nStretch2SS + nXConstSS + NpTE)
print(
    'Mesh cells: ',
    (nStretch1PS + nStretch2PS + nXConstPS + nStretch1SS + nStretch2SS + nXConstSS + NpTE - 1)
    * (NpExtrude - 1)
    * (nSpan - 1),
)


f = open('surfaceMesh.xyz', 'w')
f.write('1\n')
f.write('%d %d %d\n' % (len(xAll), nSpan, 1))
for iDim in range(3):
    for z in numpy.linspace(0.0, ZSpan, nSpan):
        for i in range(len(xAll)):
            if iDim == 0:
                f.write('%20.16f\n' % xAll[i])
            elif iDim == 1:
                f.write('%20.16f\n' % yAll[i])
            else:
                f.write('%20.16f\n' % z)
f.close()


options = {
    #        Input Parameters
    'inputFile': 'surfaceMesh.xyz',
    'unattachedEdgesAreSymmetry': False,
    'outerFaceBC': 'farField',
    'autoConnect': True,
    'BC': {1: {'jLow': 'zSymm', 'jHigh': 'zSymm'}},
    'families': 'wall',
    #        Grid Parameters
    'N': NpExtrude,
    's0': yWall,
    'marchDist': marchDist,
    #   Pseudo Grid Parameters
    'ps0': -1,
    'pGridRatio': -1,
    'cMax': 0.5,
    #   Smoothing parameters
    'epsE': 2.0,
    'epsI': 4.0,
    'theta': 2.0,
    'volCoef': 0.20,
    'volBlend': 0.0005,
    'volSmoothIter': 20,
}

hyp = pyHyp(options=options)
hyp.run()
# hyp.writeCGNS('volumeMesh.cgns')
hyp.writePlot3D('volumeMesh.xyz')
