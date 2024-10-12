gmkspl -p 14 \
-t 1000080160,1000140280,1000130270,1000260560,1000200400,1000110230,1000190390,1000120240 \
-n 100 \
-e 1000 \
--event-generator-list Default+MEC \
--output-cross-sections xsec_muon_neutrino_target_ROCK_ELEMENTS.xml


#$for target in 1000080160 1000140280 1000130270 1000260560 1000200400 1000110230 1000190390 1000120240
#$do
    #echo gmkspl -p 14 \
    #       -t $target \
    #       -n 100 \
    #       -e 1000 \
    #       --event-generator-list Default \
    #       --output-cross-sections xsec_muon_neutrino_target_"$target".xml

         #gmkspl -p 14 \
           #-t $target \
           #-n 100 \
           #-e 1000 \
           #--event-generator-list Default \
           #--output-cross-sections xsec_muon_neutrino_target_"$target".xml

         #gmkspl -p -14 \
           #-t $target \
           #-n 100 \
           #-e 1000 \
           #--event-generator-list Default \
           #--output-cross-sections xsec_antimuon_neutrino_target_"$target".xml
#
         #gmkspl -p -12 \
           #-t $target \
           #-n 100 \
           #-e 1000 \
           #--event-generator-list Default \
           #--output-cross-sections xsec_antielectron_neutrino_target_"$target".xml
#
         #gmkspl -p 12 \
           #-t $target \
           #-n 100 \
           #-e 1000 \
           #--event-generator-list Default \
           #--output-cross-sections xsec_electron_neutrino_target_"$target".xml
#
#done
