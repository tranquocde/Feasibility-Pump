for i in {1..10}
do
    echo "Processing constraints_$i.json"
    start_time=$(date +%s.%N)
    python3 fp.py -i constraints_$i.json
    end_time=$(date +%s.%N)
    running_time=$(echo "$end_time - $start_time" | bc)
    echo "Running time for constraints_$i.json: $running_time seconds"
    echo "--------------------"
done