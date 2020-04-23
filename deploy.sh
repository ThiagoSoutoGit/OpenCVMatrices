set -e

cd _build/html

git init

git add .

git commit -m 'New deployment'

git remote add origin git@github.com:ThiagoSoutoGit/OpenCVMatrices.git

git push -f origin master:gh-pages

cd -