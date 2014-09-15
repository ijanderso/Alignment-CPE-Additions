#!/bin/sh

cp Alignment-CPE-Additions/TkAllInOneTool_Additions/* Alignment/OfflineValidation/python/TkAlAllInOneTool/.
cp Alignment-CPE-Additions/CPE_Additions/interface/* RecoLocalTracker/SiStripRecHitConverter/interface/.
cp Alignment-CPE-Additions/CPE_Additions/plugins/* RecoLocalTracker/SiStripRecHitConverter/plugins/.
cp Alignment-CPE-Additions/CPE_Additions/python/* RecoLocalTracker/SiStripRecHitConverter/python/.
cp Alignment-CPE-Additions/CPE_Additions/src/* RecoLocalTracker/SiStripRecHitConverter/src/.

rm -rf Alignment-CPE-Additions