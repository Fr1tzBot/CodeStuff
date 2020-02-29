mkdir spam
counter=0
path="spam/"
while true; do
    counter=$((counter+1))
    echo $counter
    path="${path}${counter}"
    path="${path}.bin"
    echo $path
    touch $path
    break
done
rm -rf spam