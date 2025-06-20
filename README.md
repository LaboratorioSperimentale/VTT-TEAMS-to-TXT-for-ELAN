Importing text into ELAN requires special formatting to support layer and time synchronization management. This script converts all .vtt files in a given folder to .txt format (all lowercase), adjusting the formatting of each transcription segment:

# FROM THIS: 
"""
e371828e-7f70-4cb4-a3fb-18243967b8ca/30-0
00:00:03.332 --> 00:00:12.192
<v Tommaso Pellin>Ti senti vero? Non sentiamo lei,
non sentiamo noi, però ***** c'ha primis.</v>
"""

# TO THIS:
"""
# tommaso pellin	00:00:03	00:00:09	ti senti vero? non sentiamo lei, non sentiamo noi, però ***** c'ha primis.
"""


