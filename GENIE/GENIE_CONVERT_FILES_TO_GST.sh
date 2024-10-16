for INFILE in $*
do
    echo $INFILE
    gntpc -i $INFILE -f gst
done
