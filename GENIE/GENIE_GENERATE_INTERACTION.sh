#for NEUT in 14 -14 12 -12
#for NEUT in 12 -12
for NEUT in 14 -14
do
for ENERGY in 5 10 20 30 40 50 100 200 300 400 500 1000 2000 3000 4000 5000
do

    NEUT_NAME="antielectron"
    if [ $NEUT -eq -14 ]
    then
        NEUT_NAME="antimuon"
    elif [ $NEUT -eq 14 ]
    then
        NEUT_NAME="muon"
    elif [ $NEUT -eq -12 ]
    then
        NEUT_NAME="antielectron"
    elif [ $NEUT -eq 12 ]
    then
        NEUT_NAME="electron"
    fi

    XSEC_FILE="xsec_"$NEUT_NAME"_neutrino_target_rock.xml"
    OUTPUT_FILE="gntp.0.ghep."$NEUT_NAME"_neutrino_target_rock_energy_"$ENERGY".root"

    echo     gevgen -p $NEUT \
           -t "1000080160[0.466];1000140280[0.277];1000130270[0.081];1000260560[0.050];1000200400[0.036];1000110230[0.028];1000190390[0.026];1000120240[0.021]" \
           -n 1 \
           -e $ENERGY \
           --event-generator-list Default+MEC \
           --cross-sections xsec_muon_neutrino_target_ROCK_ELEMENTS.xml \
           -o $OUTPUT_FILE
           #--cross-sections $XSEC_FILE \

   done
done
