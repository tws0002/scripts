global SMTD_AutoLoadSuccessful = true
try(fileIn (getDir #userScripts + "/SubmitMaxToDeadline_Functions.ms") quiet:true )catch(::SMTD_AutoLoadSuccessful = false)
try(fileIn (getDir #userScripts + "/SubmitMaxToDeadline_SanityCheck_Private.ms") quiet:true )catch(::SMTD_AutoLoadSuccessful = false)
try(fileIn (getDir #userScripts + "/SubmitMaxToDeadline_SanityCheck_General.ms") quiet:true )catch(::SMTD_AutoLoadSuccessful = false)
try(fileIn (getDir #userScripts + "/SubmitMaxToDeadline_SanityCheck.ms") quiet:true )catch(::SMTD_AutoLoadSuccessful = false)
