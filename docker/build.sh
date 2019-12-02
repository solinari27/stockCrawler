cp ../requirements.txt .
docker build -t stockcrawler:v1.0 . 
rm requirements.txt
