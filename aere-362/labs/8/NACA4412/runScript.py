#!/usr/bin/env python


import os
import argparse
from mpi4py import MPI
from dafoam import PYDAFOAM, optFuncs
from pygeo import *
from pyspline import *
from idwarp import *
from pyoptsparse import Optimization, OPT
import numpy as np



parser = argparse.ArgumentParser()
parser.add_argument('--opt', help='optimizer to use', type=str, default='ipopt')
parser.add_argument('--task', help='type of run to do', type=str, default='opt')
args = parser.parse_args()
gcomm = MPI.COMM_WORLD

U0 = 99.3864
p0 = 101325
nuTilda0 = 0.00025
k0 = 1.48165
epsilon0 = 790.301
omega0 = 5926.59
T0 = 273.15
CL_target = 0.4
alpha0 = 3
rho0 = 1
A0 = 0.0996057



daOptions = {
    'designSurfaces': ['wing'],
    'solverName': 'DARhoSimpleFoam',
    'primalMinResTol': 1e-08,
    'printInterval' : 10,
    'primalBC': {
        'U0': {'variable': 'U', 'patches': ['inout'], 'value': [U0, 0.0, 0.0]},
        'p0': {'variable': 'p', 'patches': ['inout'], 'value': [p0]},
        'T0': {'variable': 'T', 'patches': ['inout'], 'value': [T0]},
        'nuTilda0': {'variable': 'nuTilda', 'patches': ['inout'], 'value': [nuTilda0]},
        'k0': {'variable': 'k', 'patches': ['inout'], 'value': [k0]},
        'omega0': {'variable': 'omega', 'patches': ['inout'], 'value': [omega0]},
        'epsilon0': {'variable': 'epsilon', 'patches': ['inout'], 'value': [epsilon0]},
        'useWallFunction': True,
    },
    # variable bounds for compressible flow conditions
    'primalVarBounds': {
        'UMax': 1000.0,
        'UMin': -1000.0,
        'pMax': 500000.0,
        'pMin': 20000.0,
        'eMax': 500000.0,
        'eMin': 100000.0,
        'rhoMax': 5.0,
        'rhoMin': 0.2},
    'objFunc': {
        'CD': {
            'part1': {
                'type': 'force',
                'source': 'patchToFace',
                'patches': ['wing'],
                'directionMode': 'parallelToFlow',
                'alphaName': 'alpha',
                'scale': 1.0 / (0.5 * rho0 * U0 * U0 * A0),
                'addToAdjoint': True,
            }
        },
        'CL': {
            'part1': {
                'type': 'force',
                'source': 'patchToFace',
                'patches': ['wing'],
                'directionMode': 'normalToFlow',
                'alphaName': 'alpha',
                'scale': 1.0 / (0.5 * rho0 * U0 * U0 * A0),
                'addToAdjoint': True,
            }
        },
    },
    'adjEqnOption': {'gmresRelTol': 1e-06, 'pcFillLevel': 1, 'jacMatReOrdering': 'rcm'},

    'normalizeStates': {
        'U': U0,
        'p': p0,
        'nuTilda': nuTilda0 * 10.0,
        'k': k0 ,
        'epsilon': epsilon0 * 0.1,
        'omega': omega0 * 0.01,
        'phi': 1.0,
    },
    'checkMeshThreshold': {'maxAspectRatio': 100000.0}, 
    'adjPartDerivFDStep': {'State': 1e-6, 'FFD': 1e-3},
    'primalMinResTolDiff': 1.0e5, 
    'adjPCLag': 100,
    'designVar': {},
}


meshOptions = {
    'gridFile': os.getcwd(),
    'fileType': 'openfoam',
    'symmetryPlanes': [[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]], [[0.0, 0.0, 0.1], [0.0, 0.0, 1.0]]],
}


if args.opt == 'snopt':
    optOptions = {
        'Major feasibility tolerance': 1e-06,
        'Major optimality tolerance': 1e-06,
        'Function precision': 1.0e-7,
        'Function precision': 1.0e-7,
        'Verify level': -1,
        'Major iterations limit': 50,
        'Nonderivative linesearch': None,
        'Print file': 'opt_SNOPT_print.out',
        'Summary file': 'opt_SNOPT_summary.out',
    }
elif args.opt == 'ipopt':
    optOptions = {
       'tol': 1e-06,
       'constr_viol_tol': 1e-06,
       'max_iter': 50,
       'output_file': 'opt_IPOPT.txt',
       'mu_strategy': 'adaptive',
       'limited_memory_max_history': 10,
       'nlp_scaling_method': 'none',
       'alpha_for_y': 'full',
       'recalc_y': 'yes',
  }
elif args.opt == 'slsqp':
    optOptions = {
        'ACC': 1.0e-7,
        'MAXIT': 50,
        'IFILE': 'opt_SLSQP.out',
    }
else:
    print('opt arg not valid!')
    exit(0)


def alpha(val, geo):
    aoa = val[0] * np.pi / 180.0
    inletU = [float(U0 * np.cos(aoa)), float(U0 * np.sin(aoa)), 0]
    DASolver.setOption('primalBC', {'U0': {'variable': 'U', 'patches': ['inout'], 'value': inletU}})
    DASolver.updateDAOption()

DVGeo = DVGeometry('./FFD/wingFFD.xyz')
DVGeo.addRefAxis('bodyAxis', xFraction=0.25, alignIndex='k')
iVol = 0
pts = DVGeo.getLocalIndex(iVol)
indexList = pts[:, :, :].flatten()
PS = geo_utils.PointSelect('list', indexList)
DVGeo.addGeoDVLocal('shapey', lower=-1.0, upper=1.0, axis='y', scale=1.0, pointSelect=PS)
daOptions['designVar']['shapey'] = {'designVarType': 'FFD'}
DVGeo.addGeoDVGlobal('alpha', [alpha0], alpha, lower=0.0, upper=10.0, scale=1.0)
daOptions['designVar']['alpha'] = {'designVarType': 'AOA', 'patches': ['inout'], 'flowAxis': 'x', 'normalAxis': 'y'}



DASolver = PYDAFOAM(options=daOptions, comm=gcomm)
DASolver.setDVGeo(DVGeo)
mesh = USMesh(options=meshOptions, comm=gcomm)
DASolver.addFamilyGroup(DASolver.getOption('designSurfaceFamily'), DASolver.getOption('designSurfaces'))
DASolver.printFamilyList()
DASolver.setMesh(mesh)
evalFuncs = []
DASolver.setEvalFuncs(evalFuncs)



DVCon = DVConstraints()
DVCon.setDVGeo(DVGeo)
DVCon.setSurface(DASolver.getTriangulatedMeshSurface(groupName=DASolver.getOption('designSurfaceFamily')))

leList = [[0.01, 0, 0.01], [0.01, 0, 0.09]]
teList = [[0.946057, 0, 0.01], [0.946057, 0, 0.09]]
DVCon.addVolumeConstraint(leList, teList, nSpan=2, nChord=10, lower=1, upper=3, scaled=True)

DVCon.addThicknessConstraints2D(leList, teList, nSpan=2, nChord=10, lower=0.8, upper=3, scaled=True)

nFFDs_x = pts.shape[0]
indSetA = []
indSetB = []
for i in range(nFFDs_x):
    for j in [0, 1]:
        indSetA.append(pts[i, j, 1])
        indSetB.append(pts[i, j, 0])
DVCon.addLinearConstraintsShape(indSetA, indSetB, factorA=1.0, factorB=-1.0, lower=0.0, upper=0.0)

indSetA = []
indSetB = []
for i in [0, nFFDs_x - 1]:
    for k in [0]:
        indSetA.append(pts[i, 0, k])
        indSetB.append(pts[i, 1, k])
DVCon.addLinearConstraintsShape(indSetA, indSetB, factorA=1.0, factorB=1.0, lower=0.0, upper=0.0)


optFuncs.DASolver = DASolver
optFuncs.DVGeo = DVGeo
optFuncs.DVCon = DVCon
optFuncs.evalFuncs = evalFuncs
optFuncs.gcomm = gcomm



if args.task == 'opt':

    alpha4CLTarget = optFuncs.solveCL(CL_target, 'alpha', 'CL')
    alpha([alpha4CLTarget], None)

    optProb = Optimization('opt', objFun=optFuncs.calcObjFuncValues, comm=gcomm)
    DVGeo.addVariablesPyOpt(optProb)
    DVCon.addConstraintsPyOpt(optProb)

    optProb.addObj('CD', scale=1)
    optProb.addCon('CL', lower=CL_target, upper=CL_target, scale=1)

    if gcomm.rank == 0:
        print(optProb)

    DASolver.runColoring()

    opt = OPT(args.opt, options=optOptions)
    histFile = './%s_hist.hst' % args.opt
    sol = opt(optProb, sens=optFuncs.calcObjFuncSens, storeHistory=histFile)
    if gcomm.rank == 0:
        print(sol)

elif args.task == 'runPrimal':

    optFuncs.runPrimal()

else:
    print('task arg not found!')
    exit(0)
