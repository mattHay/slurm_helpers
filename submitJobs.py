#!/usr/bin/env python
#Submits jobs to a server using the SLURM scheduler

import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", dest = "jobFile", type = "string", help = "file containing one job to be submitted per line", metavar = "JOBFILE")
parser.add_option("-n", dest = "numCores", type = "string", help = "number of cores", default="1")
parser.add_option("-N", dest = "numNodes", type = "string", help = "number of nodes", default="1")
parser.add_option("-t", dest = "timeLimit", type = "string", help = "time limit for job, where 10501, would be 1 day, 5 hours and 1 minute", default="00500", metavar = "INT")
parser.add_option("-p", dest = "priority", type = "string", help = "Queue based on number of jobs in file, either: " +
                                                  "'priority' (1 month, 1 or 2 jobs) " +
                                                  "'short' (12 hours, more then 2 jobs) " +
                                                  "'medium' (5 days, more then 2 jobs) " +
                                                  "'long' (1 month, more then 2 jobs)", default="short")
parser.add_option("-m", dest = "mem", type = "string", help = "Amount of memory in G, e.g 5G", default="5G")
(ops, args) = parser.parse_args()

time_opt = ops.timeLimit
time = ops.timeLimit[0] + "-" + ops.timeLimit[1:3] + ":" + ops.timeLimit[3:5]
    
for line in open(ops.jobFile, "r"):
    line = line.rstrip()
    
    output = open("tempJob", "w")

    output.write("#!/bin/bash\n")
    output.write("#SBATCH -n " + ops.numCores  + "\n")
    output.write("#SBATCH -N " + ops.numNodes + "\n")
    output.write("#SBATCH -t " + time  + "\n")
    output.write("#SBATCH -p " + ops.priority + "\n")
    output.write("#SBATCH --mem=" + ops.mem  + "\n")
    output.write("#SBATCH -o %j.out\n")
    output.write("#SBATCH -e %j.err\n")

    output.write(line)
    output.close()

    os.system("sbatch tempJob")
    os.remove("tempJob")
    
