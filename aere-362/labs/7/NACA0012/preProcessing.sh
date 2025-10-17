#!/bin/bash


if [ -z "$WM_PROJECT" ]; then
  echo "OpenFOAM environment not found"
  exit
fi


echo "Generating mesh.."
python genAirfoilMesh.py &> logMeshGeneration.txt
plot3dToFoam -noBlank volumeMesh.xyz >> logMeshGeneration.txt
autoPatch 45 -overwrite >> logMeshGeneration.txt
createPatch -overwrite >> logMeshGeneration.txt
renumberMesh -overwrite >> logMeshGeneration.txt
echo "Generating mesh.. Done!"


cp -r 0.orig 0
