#!/usr/bin/env python

#Make a call to SLURM for an interactive node

import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", dest = "mem", type = "string", help = "How memory do you need?", metavar = "memory")
(ops, args) = parser.parse_args()

print("srun --pty -p interactive --mem " + ops.mem + "G -t 0-12:00 /bin/bash")
