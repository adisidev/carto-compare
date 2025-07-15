# cartogram-algorithms-evaluation
Data used for our group's CaGiS 2025 paper on our densification algorithm

## Format

- Files in `input` folder are input GeoJSONs and CSVs. Files in `f4carto-input` are the corresponding input files converted `.shp` files so they may be used by Sun' `F4Carto`.
- CSV files found in the `inputs` folder are always the input target area files.
- Folder names containing `5FCarto` are the corresponding outputs from `cartogram-cpp`.
- Folder names containing `BFB` are the corresponding outputs from `cartogram-cpp` with densification and simplification turned off.
- File names ending in `F4Carto` are the corresponding outputs from Sun's program with default parameters.

In the current setup, you need to replace `_cartogram.geoson` with `_5Fcarto.geojson` or `_flow_based.geojson` respectively in your corresponding results directory.

## Scripts

-- `calculate_area_error.sh`: Script to calculate area error of directory based on `inputs`.

- Note: Similarity data should be based on raw results used for timing, not the best results out of 100 iterations.

```bash
bash calculate_similarity_and_intersections.sh <5FCarto-directory> <F4Carto-directory> <BFB-directory> <results-directory>
```

For example:
```bash
bash calculate_similarity_and_intersections.sh 5FCarto-JUL15-TIMING-QCLF09/ F4Carto-raw-10 BFB-JUL15-TIMING-QCLF09 J
UL15-similarity-and-intersections
```

### Note: The data is already processed, so you do not need to run the following script.

-- `process_raw_data_from_F4Carto.sh`: Script to convert F4Carto mapfile output to GeoJSON, `_nfo.txt` to `_F4Carto.csv`, and remove `.shp`, `.shx`, `.dbf`, `.prj` files. This also calculates the area errors of the `F4Carto` results, based on the target area already embedded as in the GeoJSON files.

depends on: `mapshaper`