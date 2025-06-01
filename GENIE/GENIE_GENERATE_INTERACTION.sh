NEVENTS=10000
#for NEUT in 14 -14 12 -12
#for NEUT in 12 -12
#for NEUT in 14 -14
for NEUT in 14 
do
#for ENERGY in 5 10 20 30 40 50 100 200 300 400 500 990 #1000 2000 3000 4000 5000
for ENERGY in 300
do

    NEUT_NAME="electron_neutrino"
    if [ $NEUT -eq -14 ]
    then
        NEUT_NAME="muon_antineutrino"
    elif [ $NEUT -eq 14 ]
    then
        NEUT_NAME="muon_neutrino"
    elif [ $NEUT -eq -12 ]
    then
        NEUT_NAME="electron_antineutrino"
    elif [ $NEUT -eq 12 ]
    then
        NEUT_NAME="electron_neutrino"
    fi

    XSEC_FILE="xsec_"$NEUT_NAME"_target_rock.xml"
    OUTPUT_FILE="gntp.0.ghep."$NEUT_NAME"_target_rock_energy_"$ENERGY"_nevents_"$NEVENTS".root"
    OUTPUT_FILE2="gntp.0.hepmc3."$NEUT_NAME"_target_rock_energy_"$ENERGY"_nevents_"$NEVENTS".ascii"

                 gevgen -p $NEUT \
           -t "1000080160[0.466];1000140280[0.277];1000130270[0.081];1000260560[0.050];1000200400[0.036];1000110230[0.028];1000190390[0.026];1000120240[0.021]" \
           -n $NEVENTS \
           -e $ENERGY \
           --event-generator-list Default \
           --cross-sections xsec_"$NEUT_NAME"_list_Default_target_ROCK_ELEMENTS.xml \
           -o $OUTPUT_FILE,ghep,$OUTPUT_FILE2,hepmc
           #--cross-sections $XSEC_FILE \
           #--event-level-print-record 0 \
           #--message-thresholds quiet-thresholds.xml \

   done
done
