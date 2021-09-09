#!bin/bash

set -e

echo "Criando admin do mongodb"
mongo <<EOF

use db_crud_python

EOF