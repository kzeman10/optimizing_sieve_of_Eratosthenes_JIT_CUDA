#!/bin/bash

# Print processor information
echo "script about to run on system with the following specs:"
processor_info=$(lscpu | grep 'Model name' | awk -F': ' '{print $2}')
echo "Processor: $processor_info"

# Print GPU information
gpu_info=$(lspci | grep -i 'VGA\|3D' | awk -F': ' '{print $2}')
echo "GPU: $gpu_info"
echo


echo "results:"
# Run optimized cupy implementation
# warmup run
python sieve_cupy_optimized.py > /dev/null
cupy_optimized_time=$( { time python sieve_cupy_optimized.py 2>&1; } 2>&1 | grep real | awk '{print $2}' )
echo "Sieve Cupy Optimized: ${cupy_optimized_time}"

# Run cupy implementation
# warmup run
python sieve_cupy.py > /dev/null
cupy_time=$( { time python sieve_cupy.py 2>&1; } 2>&1 | grep real | awk '{print $2}' )
echo "Sieve Cupy: ${cupy_time}"

# Run numpy implementation
numpy_time=$( { time python sieve_numpy.py 2>&1; } 2>&1 | grep real | awk '{print $2}' )
echo "Sieve NumPy: ${numpy_time}s"

# Run numba implementation
numba_time=$( { time python sieve_numba.py 2>&1; } 2>&1 | grep real | awk '{print $2}' )
echo "Sieve Numba: ${numba_time}s"

# Run naive python implementation and multiply by 4
naive_time=$( { time python sieve_naive.py 2>&1; } 2>&1 | grep real | awk '{print $2}' )
echo "Sieve Naive: ${naive_time}s -- size only 2**30, thus expected time would be at least 4 * longer"

# Compile sieve.c and run, capturing real time in seconds
gcc -o sieve sieve.c -lm
gcc_time=$( { time ./sieve 2>&1; } 2>&1 | grep real | awk '{print $2}' )
echo "Sieve GCC: ${gcc_time}s"

# Compile optimized sieve.c and run, capturing real time in seconds
gcc -o sieve_optimized sieve.c -lm -O3
optimized_time=$( { time ./sieve_optimized 2>&1; } 2>&1 | grep real | awk '{print $2}' )
echo "Sieve GCC Optimized: ${optimized_time}s"
rm sieve sieve_optimized
