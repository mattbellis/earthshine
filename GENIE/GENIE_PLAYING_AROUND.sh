#gmkspl -p 14 -e 20 -n 100 -t 1000080160 --event-generator-list CCQE -o xsec_playing_around.xml
# Doesn't work
#gmkspl -p 14 -e 20 -n 100 -t 1000080160 --event-generator-list CCQE,NCQE,CCRES,NCRES,CCDIS,NCDIS,CCCOH,NCCOH,CCMEC,NCMEC,IMD,NuEElastic,NuE -o xsec_playing_around_LIST_BY_HAND.xml
#gevgen -p 14 -e 5 -n 10 -t 1000080160   --event-generator-list CCQE --cross-sections xsec_muon_neutrino_target_1000080160.xml
#gevgen -p 14 -e 5 -n 10 -t 1000080160   --event-generator-list CCQE --cross-sections xsec_playing_around.xml
#gmkspl -p 14 -e 20 -n 100 -t 1000080160 --event-generator-list Default+MEC -o xsec_playing_around_LIST_BY_HAND.xml
#gevgen -p 14 -e 5 -n 10 -t 1000080160   --event-generator-list Default+MEC --cross-sections xsec_playing_around_LIST_BY_HAND.xml

#gmkspl -p 14 -e 20 -n 10 -t 1000060120 --event-generator-list Default -o xsec_playing_around_Default.xml
gevgen -p 14 -e 5 -n 10 -t 1000060120 --event-generator-list Default --cross-sections xsec_playing_around_Default.xml

#gevgen -p 14 -e 5 -n 10 -t 1000080160 --event-generator-list Default --cross-section xsec_muon_neutrino_target_rock.xml
#gevgen -p 14 -e 5 -n 10 -t 1000080160 --event-generator-list Default --cross-sections xsec_muon_neutrino_target_1000080160.xml
