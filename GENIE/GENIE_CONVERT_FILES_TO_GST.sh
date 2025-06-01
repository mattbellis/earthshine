for INFILE in $*
do
    #echo $INFILE
    OUTFILE=$(basename $INFILE root | sed 's/ghep.//')"gst.root"
    echo gntpc -i $INFILE -f gst -o $OUTFILE
         gntpc -i $INFILE -f gst -o $OUTFILE
done
