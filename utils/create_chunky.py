from Audio_Compression.utils.audioutil import Audio
import sys

Handler= Audio()
Handler.make_chunks(sys.argv[1], sys.argv[2], sys.argv[3])