# cartogram-algorithms-evaluation
Data used for our group's CaGiS 2025 paper on our densification algorithm

## Format

- Files in `input` folder are input GeoJSONs and CSVs. Files in `f4carto-input` are the corresponding input files converted `.shp` files so they may be used by Sun' `F4Carto`.
- CSV files are always the input target area files.
- Files ending in `5FCarto` are the corresponding outputs from `cartogram-cpp`.
- Files ending in `F4Carto` are the corresponding outputs from Sun's program with default parameters.

## Scripts

-- `calculate_area_error.sh`: Script to calculate area error of directory based on `inputs`.

```bash
bash calculate_area_error.sh <results-directory>
```

-- `process_raw_data_from_F4Carto.sh`: Script to convert F4Carto mapfile output to GeoJSON, `_nfo.txt` to `_F4Carto.csv`, and remove `.shp`, `.shx`, `.dbf`, `.prj` files.

depends on: `mapshaper`

```bash
bash calculate_area_error.sh <results-directory>
```

First, run `copy_out.sh` like so:
```bash
bash copy_out.sh
```

This will copy the best result upto 10th iteration into the `output` directory. Note that the best result is actually one before the last iteration, because iterations stop when area error rises. That is why, we initially take the last iteration upto 11th, and copy the 2nd last iteration into the ouput directory.

Then, go to the `output` directory, and run:
```zsh
zsh convert_to_geojson.sh
```

This will convert all the integrations to geojson format, remove the integration number, append `_f4carto`, and finally move them to the `geojson` directory.

Make sure to use `zsh` instead of `bash`, unless you have `bash` > 4.2. Untested, just going off the internet.

You can now use the results in the `geojson` directory with `carto-tools`: https://github.com/nihalzp/carto-tools.