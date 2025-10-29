# description: 
from earsketch import *
# Initialize project
init(1)
setTempo(85)  # since R&B usually has a slower groove (80–90 BPM)

# Song structure
# Part 1:
# Intro 1-5 , Chorus: 5–9.5, bridge: 9-11, verse: 11-14, prechorus: 14-22
# Part 2:
# chrous: 22-31, verse: 32-43, outro: 43-51

# Variable list for general chorus
drums = AK_UNDOG_PERC_DRUMS
bass = HIPHOP_BASSSUB_001
pad = YG_HIP_HOP_ELECTRIC_PIANO_1
Riseup = AK_UNDOG_LEAD_VOCALS_BRIDGE_2
endvocal= AK_UNDOG_VOCAL_BELT_7

# Intro (smooth intro: drums + pad)
fitMedia(drums, 1, 1, 5)
fitMedia(pad, 2, 1, 5)

# Chorus number 1
fitMedia(drums, 1, 5, 9)
fitMedia(bass, 2, 5, 9)
fitMedia(pad, 3, 5, 9)
fitMedia(Riseup, 4, 5, 9)
fitMedia(endvocal, 6, 8.5, 9.5)

# variables for verse 1
bassv1 = KHALID_NORM_KEYS_JUNO_1
percv1 = AK_UNDOG_PERC_HATS_2
drumsv1 = AK_UNDOG_CLAPS_SNAPS_2


# verse 1 (more chilled)
fitMedia(bassv1, 1, 10.75, 22)
fitMedia(percv1, 2, 7, 22)
fitMedia(drumsv1,3, 7, 22)


# variables for prechorus
funkpc= YG_RNB_FUNK_SHAKER_2
shimpcc= RD_RNB_SFX_SHIMMER_1,
vocalspc= ENTREP_VOX_PHARRELL_VRS_2
vocals2pc= AK_UNDOG_VOCAL_BELT_6,


# prechorus (Pharrell)
fitMedia(funkpc, 6, 18, 19)
fitMedia(shimpcc[0], 7, 22, 23)
fitMedia(vocalspc, 8, 15, 22)
fitMedia(vocals2pc[0], 12, 22, 23)

# Chorus 2 
fitMedia(drums, 1, 23, 31)
fitMedia(bass, 2, 23, 31)
fitMedia(pad, 3, 23, 31)
fitMedia(Riseup, 4, 23, 31)
fitMedia(endvocal, 6, 30.5, 31.6)

# verse 2 variables
RNBv2 = RD_RNB_ACOUSTIC_NYLONSTRING_4
shimmerv2= RD_RNB_SFX_SHIMMER_1
whisperv2= ENTREP_VOX_PHARRELL_WHSP_2
vocalsv2= AK_UNDOG_LEAD_VOCALS_PRE_CHORUS_1

fitMedia(RNBv2, 10, 31.5, 43)
fitMedia(shimmerv2, 8,42, 43 )
fitMedia(whisperv2, 1, 39,43)
fitMedia(vocalsv2, 7, 35, 40)

# outro
fitMedia(pad, 3, 43, 51)

# effects for R&B vibe
setEffect(3, REVERB, REVERB_TIME, 200)    # Smooth pad reverb
setEffect(2, VOLUME, GAIN, -4)            # Slightly softer bass

# Volume fade-out on outro
setEffect(1, VOLUME, GAIN, -2, 9, -30)    # Drums fade out
setEffect(2, VOLUME, GAIN, -4, 9, -30)    # Bass fade out

# End project
finish(51)
