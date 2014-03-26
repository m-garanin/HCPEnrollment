# !/bin/sh

psql -d template1 -c "DROP DATABASE test_hcpenroll;" -U $1
psql -d template1 -c "CREATE DATABASE test_hcpenroll ENCODING='UNICODE';" -U $1




