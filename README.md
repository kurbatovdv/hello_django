docker build -t hello_django .   
docker run -d -v //c/scripts/hello_django:/app -p 3000:3000  hello_django
