# Convert shp files in each subdirectory to GeoJSON using mapshaper
# Remove the .shp, .shx, .dbf, and .prj files
# Rename the _nfo.txt file to _F4Carto.csv
# Calculate area errors for each GeoJSON file using carto

# Add colors
red=1
green=2
yellow=3
blue=4
magenta=5
cyan=6
white=7
color() {
  tput setaf $1
  cat
  tput sgr0
}

# Check if a directory argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Get the directory from the command-line argument
TARGET_DIR="$1"

# Check if the provided argument is a directory
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: $TARGET_DIR is not a directory."
  exit 1
fi

# Find all subdirectories in the specified directory, not including the top-level directory
find "$TARGET_DIR" -mindepth 1 -type d | while read -r dir; do

  cd "$dir" || continue

  # Inform user of the current directory, in magenta
  echo "Processing $dir..." | color $magenta

  # Convert each .shp file
  # Using ls to make sure _2 comes before _10
  for shp_file in $(ls *.shp | sort -V); do
    # output name should be the same as the input name, but with .geojson extension
    geojson_file="${shp_file%.shp}.geojson"
    mapshaper -i "$shp_file" -o format=geojson "$geojson_file"
  done

  echo "Removing *.shp, *.shx, *.dbf, and *.prj files in $dir: "
  # Remove the .shp, .shx, .dbf, and .prj files, if any

  rm -v *.shp *.shx *.dbf *.prj

  # Convert single _nfo.txt to _F4Carto.csv
  nfo_file=$(ls *_nfo.txt)
  if [[ -f "$nfo_file" ]]; then
    mv -v "$nfo_file" "${nfo_file%_nfo.txt}_F4Carto.csv"
  fi

  # Calculate area errors to accompany the `_nfo.txt` as a log file
  for geojson_file in $(ls *.geojson | sort -V); do
    if [[ -f "$geojson_file" ]]; then
      echo "Calculating area error for $geojson_file" | color $cyan
      carto --area_error --map "$geojson_file" > /dev/null 2>&1
      # --target_area_csv not needed as should be self-contained as property within GeoJSON
    fi
  done

  # Return to the parent directory
  cd - > /dev/null || exit
done