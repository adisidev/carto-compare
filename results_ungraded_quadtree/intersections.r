library(tidyverse)
library(janitor)

data <- read_csv("intersections.csv") |> clean_names()

basenames <- data |>
	# check if map_name has "5FCarto in it"
	filter(str_detect(map_name, "5FCarto")) |>
	select(map_name) |>
	# remove "_5FCarto.geojson" from end of map_name
	mutate(map_name = str_remove(map_name, "_5FCarto.geojson")) |>
	pull()

repeated_basenames <- rep(basenames, each = 3)
# pivot intersections.csv based on basenames

data <- data |>
	mutate(basename = repeated_basenames)


test <- data %>%
	# Step 1: Process each row individually
	rowwise() %>%
	# Step 2: Extract the suffix by removing the basename from the map_name
	mutate(
		suffix = gsub(paste0("^", basename, "_"), "", map_name)
	)  |>
	mutate(
		suffix = ifelse(grepl("^\\d\\.geojson$", suffix), "F4Carto.geojson", suffix)
	) |>
	mutate(
		suffix = sub("\\.geojson$", "", suffix)
	) |>
	ungroup() |>
	# Step 5: Pivot the table
	pivot_wider(
		id_cols = basename,
		names_from = suffix,
		values_from = c(self_intersections, overlap_intersections),
		names_sep = "_"
	)
