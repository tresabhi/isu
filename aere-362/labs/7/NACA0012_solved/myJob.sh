#!/bin/bash
#SBATCH --time=0:15:00           # walltime limit (HH:MM:SS)
#SBATCH --nodes=1                # number of nodes
#SBATCH --ntasks-per-node=16     # CPU cores per node 
#SBATCH --output="log-%j.txt"    # simulation log file name
#SBATCH --partition=instruction  # node type
#SBATCH --account=[REDACTED]
#SBATCH --constraint=intel

. /work/class-faculty/phe/dafoam/loadDAFoam.sh
chmod -R 750 *
./preProcessing.sh
mpirun -np 16 python runScript.py
reconstructPar
rm -rf processor*
