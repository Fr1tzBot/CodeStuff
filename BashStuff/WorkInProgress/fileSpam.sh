mkdir spam
counter=0
while true; do
    counter=$((counter+1))
    echo $counter
    path="spam/"
    path="${path}${counter}"
    path="${path}.bin"
    echo $path
    touch $path
    break
done
rm -rf spam