#!/bin/bash

echo "Exécution des tests pour le projet Blokus..."

# Ajouter le dossier courant au PYTHONPATH pour permettre les imports
export PYTHONPATH=$(pwd)

# Exécuter tous les tests dans le dossier 'test/'
pytest -s test/

echo "Tous les tests sont terminés."

