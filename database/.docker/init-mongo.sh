#!bin/bash

set -e

echo "Criando admin do mongodb"
mongo <<EOF

use db-crud-python

EOF