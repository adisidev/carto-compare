# Get 5FCarto directory, F4Carto directory and output directory
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <5FCarto-directory> <F4Carto-directory> <flow-based-data> <results-directory>"
    exit 1
fi

input_dir="inputs"

# Create output directory if it does not exist
mkdir -p "$4"

# cd into results directory
cd "$4"

# For each subdirectory in F4Carto-directory
for f4carto_dir in ../"$2"/*/; do
    mapname=$(basename "$f4carto_dir")

    # Find input map
    # i.e. map with pattern *_input.geojson in input directory
    input_map=$(ls -t ../"$input_dir"/"$mapname"_input.geojson | head -n 1)

    # Find F4Carto map
    # i.e. second last map with pattern *.geojson in F4Carto directory
    f4carto_map=$(ls -t "$f4carto_dir"*.geojson | sort -V | tail -n 2 | head -n 1)

    # Find 5FCarto map
    # i.e. map with pattern *_cartogram.geojson in 5FCarto directory
    _5FCarto_map=$(ls -t ../"$1"/"$mapname"_*.geojson)

    # Find flow_based map
    # i.e. map with pattern *_flow_based.geojson in flow_based directory
    flow_based_map=$(ls -t ../"$3"/"$mapname"_*.geojson)

    # Calculate similarity between input_map and each of the three maps
    carto --similarity --map_1 "$input_map" --map_2 "$f4carto_map"
    carto --similarity --map_1 "$input_map" --map_2 "$_5FCarto_map"
    carto --similarity --map_1 "$input_map" --map_2 "$flow_based_map"

    # Calculate intersections for all three cartograms
    carto --intersection --map "$f4carto_map"
    carto --intersection --map "$_5FCarto_map"
    carto --intersection --map "$flow_based_map"
done

# Copy all .svg files to `intersections` directory
mkdir -p intersections
find . -maxdepth 1 -type f -name '*.svg' -exec mv {} intersections \;