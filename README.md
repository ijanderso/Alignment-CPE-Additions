Alignment-CPE-Additions
=======================

To use CPE templates in the All In One Alignment tool, a few additional files and modifications are needed. This repository has those pieces.

# Installation 

	cmsrel CMSSW_X_Y_Z
	cd CMSSW_X_Y_Z/src
	cmsenv
	git cms-addpkg Alignment/OfflineValidation
	git cms-addpkg MuonAnalysis/MomentumScaleCalibration
	git cms-addpkg RecoLocalTracker/SiStripRecHitConverter
	git clone https://github.com/ijanderso/Alignment-CPE-Additions
	chmod +X Alignment-CPE-Additions/copyAdditions.sh
	./Alignment-CPE-Additions/copyAdditions.sh
	scram b -j 8

# Use

To use in any config file, simply add TemplateAddition = SID to the validation to run, i.e.

	[alignment:wtemplate] 
	globaltag = START53_V7A::All
	condition TrackerAlignmentRcd = sqlite_file:/afs/cern.ch/work/a/anderso/public/Alignment/ideal.db, Alignments
	condition TrackerAlignmentErrorRcd = sqlite_file:/afs/cern.ch/work/a/anderso/public/Alignment/ideal.db, AlignmentErrors
	TemplateAddition = 60

SID = 60 is currently the most up to date version of the templates.

# Comments

Use has only been validated in CMSSW_53X. Runs on SLC5/6, but ZMuMu tests may still not work (likely fault of AllInOneTool).