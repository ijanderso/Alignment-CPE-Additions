TemplateAddition="""process.load("RecoLocalTracker.SiStripRecHitConverter.StripCPEfromTemplate_cfi")
process.StripCPEfromTrackAngleESProducer = process.StripCPEfromTemplateESProducer.clone(ComponentName='StripCPEfromTrackAngle')
process.load("RecoLocalTracker.SiStripRecHitConverter.StripCPEfromTemplate_cfi")
process.StripCPEfromTrackAngleESProducer.UseTemplateReco = True
process.StripCPEfromTrackAngleESProducer.StripTemplateID = .oO[STID]Oo.
process.StripCPEfromTrackAngleESProducer.TemplateRecoSpeed = 0
process.StripCPEfromTrackAngleESProducer.UseStripSplitClusterErrors = True
"""
